# Assignment #2
# Written by: Pratham Patel 40227835
# For COMP 348 Section U - Fall 2022
# 11/24/2022

import socket

HOST,PORT = "localhost", 9999

# opens file to read the data and puts the data inside a tuple seperated by a comma for each instance of a "|"
file = open("data.txt", "r")
data_holder = []

for t in file:
  file_tuple = tuple((x.rstrip("\n") for x in t.split('|')))
  data_holder.append(file_tuple)

file.close()

# Creates a server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    # Binding to localhost on port 9999 and listening with sockets 
    server.bind((HOST, PORT))
    server.listen()
    conn, addr = server.accept()

    # current connection
    with conn:
        print(f"Connection Established by {addr}")

        while True:
            data = conn.recv(1024)  # receive data from the client 
            data = data.decode("utf-8")

            # checks if data received from the client is not empty 
            if data == "":
                option = 0
            else:
                data_received = data.split(",")
                option = int(data_received[0])
                
            # if option provided by client is 1 and the name is in the tuples inside the data_holder it will return that its inside the database otherwise it will say its not
            if option == 1:
                client_info = ""
                client_name = str(data_received[1])
                found = False
                for x in data_holder:
                    if client_name == x[0]:
                        found = True
                        client_info = x[0] + "|" + x[1] + "|" + x[2] + "|" + x[3]

                if found == True:
                    conn.send(bytes("Server response: " + client_info, 'utf-8'))
                    
                if found == False:
                    conn.send(bytes("Server response: " + client_name + " not found in database", 'utf-8'))

            # if option provided by client is 2 and the name is not in the tuples inside the data_holder it will add the client in the database otherwise it will say that customer exists
            elif option == 2:
                client_info = str(data_received[1]).split("|")
                tup = client_info[0], client_info[1], client_info[2], client_info[3]

                found = False
                for x in data_holder:
                    if client_info[0] == x[0]:
                        found = True
                
                if found == True:
                    conn.send(bytes("Server response: Customer already exists", 'utf-8'))

                if found == False:
                    data_holder.append(tup)
                    # add the new info to the file
                    f = open("data.txt", 'a')
                    f.write("\n" + client_info[0] + "|" + client_info[1] + "|" + client_info[2] + "|" + client_info[3])
                    f.close()
                    conn.send(bytes("Server response: " + client_info[0] + " has been successfully added to the database", 'utf-8'))

            # if option provided by client is 3 and the name is in the tuples inside the data_holder it will remove the client from the database otherwise it will say that customer does not exists
            elif option == 3:
                client_name = str(data_received[1])
                found = False
                for x in data_holder:
                    if client_name == x[0]:
                        found = True
                        data_holder.remove(x)

                # removes the client from the file
                if found == True:
                    old_info = ""
                    read_file = open("data.txt", 'r')
                    for line in read_file:
                        if client_name in line.strip("\n"):
                            arr = line.split("|")
                            if client_name == arr[0]:
                                old_info += ""
                                continue
                        old_info += line
                    read_file.close()
                    write_file = open("data.txt", 'w')
                    write_file.write(old_info)
                    write_file.close()

                    conn.send(bytes("Server response: " + client_name + " has been removed from the database", 'utf-8'))

                if found == False:
                    conn.send(bytes("Server response: Customer does not exist", 'utf-8'))

            # if option provided by client is 4 or 5 or 6 and the name is in the tuples inside the data_holder it will remove the client from the database otherwise it will say that customer does not exists
            elif option == 4 or option == 5 or option == 6:
                client_name = str(data_received[1])
                found = False
                for x in data_holder:
                    if client_name == x[0]:
                        found = True
                        client_data = list(x)
                        
                        # replaces the changed value inside the client_data with the new info
                        if option == 4:
                            client_data[1] = data_received[2]
                        if option == 5:
                            client_data[2] = data_received[2]
                        if option == 6:
                            client_data[3] = data_received[2]

                        # replaces client old info with new info inside the array of tuple
                        new_tup = tuple(client_data)
                        data_holder.remove(x)
                        data_holder.append(new_tup)
                        new_info = client_data[0] + "|" + client_data[1] + "|" + client_data[2] + "|" + client_data[3] + "\n"

                # replaces client old info with new info inside the file
                if found == True:
                    old_info = ""
                    read_file = open("data.txt", 'r')
                    for line in read_file:
                        if client_name in line.strip("\n"):
                            arr = line.split("|")
                            if client_name == arr[0]:
                                old_info += new_info
                                continue
                        old_info += line
                    read_file.close()
                    write_file = open("data.txt", 'w')
                    write_file.write(old_info)
                    write_file.close()
                        
                    if option == 4:
                        conn.send(bytes("Server response: " + client_name + "'s age has been updated in the database", 'utf-8'))
                    if option == 5:
                        conn.send(bytes("Server response: " + client_name + "'s address has been updated in the database", 'utf-8'))
                    if option == 6:
                        conn.send(bytes("Server response: " + client_name + "'s phone number has been updated in the database", 'utf-8'))
                        

                if found == False:
                    conn.send(bytes("Server response: Customer not found", 'utf-8'))

            # if option provided by client is 7 it will return the info stored inside the data_holder which was retrieved from the file in a alphabetical order by the names
            elif option == 7:
                sorted_data = sorted(data_holder)
                clients = ""
                for x in sorted_data:
                    clients += x[0] + "|" + x[1] + "|" + x[2] + "|" + x[3]
                    clients += "\n"

                conn.send(bytes("\n** Python DB contents ** \n" + clients , 'utf-8'))

            # if option provided by client is 8 it will close the connection with the current client and open other requests for clients.
            elif option == 8:
                string = str(data_received[1])
                if string == "Good bye":
                    conn.send(bytes("Server response: " + string, 'utf-8'))
                    conn.close()
                    conn, addr = server.accept()
                    print(f"Connection Established by {addr}")
            else:
                pass


