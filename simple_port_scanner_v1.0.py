# Make a "Simple Port Scanner" using Python

import socket   # for using "Socket Programming"
import sys      # for accessing "System-specific parameters and functions"

# Create a simple banner
print('-' * 23)
print("| Simple Port Scanner |")
print('-' * 23)

# Initialise two variables for counting scanned and open ports
count_scanned_ports = 0
count_open_ports = 0

# Created a function to print the number of ports scanned and opened
def scanned_and_open_ports():
  print(f'Number of scanned ports: {count_scanned_ports}')
  print(f'Number of open ports: {count_open_ports}')

# Use try-except to handle errors
try:
  # Take input the target IP and port range
  ip = input("\nPlease Enter An Valid IP Address: ")
  start_port = int(input("Enter Starting Port: "))
  end_port = int(input("Enter ending port: "))

  # Starting message
  print("\nStart scanning...\n")

  # Scan port on the target IP
  for port in range(start_port, end_port+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    count_scanned_ports+=1
    
  # Check if port is open
    check = s.connect_ex((ip, port))
    if check == 0:
      print(f'[+] Port {port} is open.')
      s.close()
      count_open_ports+=1
      
except KeyboardInterrupt:
  # Ctrl+C pressed messages
  print("\nExitting Porgram !!!")
  scanned_and_open_ports()
  sys.exit()
  
except socket.error:
  # Error message
  print("\nServer not responding !!!")
  sys.exit()

# Ending messages
print("\nScanning Completed !!!")
scanned_and_open_ports()
