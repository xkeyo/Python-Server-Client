# Assignment #2
# Written by: Pratham Patel 40227835
# For COMP 348 Section U - Fall 2022
# 11/24/2022

import socket
import sys

HOST, PORT = "localhost", 9999

# Create a socket 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server
    sock.connect((HOST, PORT))

    program_track = True
    while program_track:
      option = input(

"""

Python DB Menu

1. Find customer
2. Add customer
3. Delete customer
4. Update customer age
5. Update customer address
6. Update customer phone
7. Print report
8. Exit

Select: """)
      # checks if the option inputed is an integer or not
      if not option.isdigit():
          print("Please enter an integer!")
          continue
      option = int(option)

      # if option == 1 will send the option concatenated/seperated with a comma to the customer's name without space to the server
      if option == 1:
        name = input("Customer Name: ").lstrip().rstrip()
        data = str(option) + "," + name
        sock.send(bytes(data, 'utf-8')) # Send data to the server
        received = sock.recv(1024)  # Receive data from the server
        print(received.decode("utf-8")) # Prints data received from the server

      # if option == 2 will send the option concatenated/seperated with a comma to the customer's name, age, address, phone without space to the server
      elif option == 2:
        while True:
          name = input("Customer Name: ").lstrip().rstrip()
          if not name == "":
            break
          else:
            continue

        age = input("Please Enter Customer Age: ").lstrip().rstrip()
        address = input("Please Enter Customer Address: ").lstrip().rstrip()
        phone = input("Please Enter Customer Phone Number: ").lstrip().rstrip()

        data = str(option) + "," + name + "|" + age + "|" + address + "|" + phone
        sock.send(bytes(data, 'utf-8')) # Send data to the server
        received = sock.recv(1024)  # Receive data from the server
        print(received.decode("utf-8")) # Prints data received from the server

      # if option == 2 will send the option concatenated/seperated with a comma to the customer's name without space to the server
      elif option == 3:
        while True:
          name = input("Please Enter Customer's Name You Wish To Delete: ").lstrip().rstrip()
          if not name == "":
            break
          else:
            continue
          
        data = str(option) + "," + name
        sock.send(bytes(data, 'utf-8')) # Send data to the server
        received = sock.recv(1024)  # Receive data from the server
        print(received.decode("utf-8")) # Prints data received from the server

      # if option == 4 will send the option concatenated/seperated with a comma to the customer's name and age without space to the server
      elif option == 4:
        while True:
          name = input("Please Enter Customer's Name Whose Age You Wish To Update: ").lstrip().rstrip()
          if not name == "":
            break
          else:
            continue

        age = input("Please Enter Customer Newly Updated Age: ").lstrip().rstrip()
        data = str(option) + "," + name + "," + age
        sock.send(bytes(data, 'utf-8')) # Send data to the server
        received = sock.recv(1024)  # Receive data from the server
        print(received.decode("utf-8")) # Prints data received from the server

      # if option == 5 will send the option concatenated/seperated with a comma to the customer's name and address without space to the server
      elif option == 5:
        while True:
          name = input("Please Enter Customer's Name Whose Address You Wish To Update: ").lstrip().rstrip()
          if not name == "":
            break
          else:
            continue

        address = input("Please Enter Customer Newly Updated Address: ").lstrip().rstrip()
        data = str(option) + "," + name + "," + address
        sock.send(bytes(data, 'utf-8')) # Send data to the server
        received = sock.recv(1024)  # Receive data from the server
        print(received.decode("utf-8")) # Prints data received from the server

      # if option == 6 will send the option concatenated/seperated with a comma to the customer's name and phone without space to the server
      elif option == 6:
        while True:
          name = input("Please Enter Customer's Name Whose Phone Number You Wish To Update: ").lstrip().rstrip()
          if not name == "":
            break
          else:
            continue

        phone = input("Please Enter Customer Newly Updated Phone Number: ").lstrip().rstrip()
        data = str(option) + "," + name + "," + phone
        sock.send(bytes(data, 'utf-8')) # Send data to the server
        received = sock.recv(1024)  # Receive data from the server
        print(received.decode("utf-8")) # Prints data received from the server

      # if option == 7 will send the option to the server
      elif option == 7:
        data = str(option)
        sock.send(bytes(data, 'utf-8')) # Send data to the server
        received = sock.recv(1024)  # Receive data from the server
        print(received.decode("utf-8")) # Prints data received from the server

      # if option == 8 will send the option concatenated/seperated with a comma to "Good bye" the server
      elif option == 8:
        data = str(option) + "," + "Good bye"
        sock.send(bytes(data, 'utf-8')) # Send data to the server
        received = sock.recv(1024)  # Receive data from the server
        print(received.decode("utf-8")) # Prints data received from the server
        program_track = False  
        sock.close()   

      # checks if input option is an integer between 1-8
      else:
        print("\nInput must be an integer between 1-8. Please try again!")         