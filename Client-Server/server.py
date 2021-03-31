
import socket


def server_program():

    host = '127.0.0.1'
    port = 2004  # initiate port

    server_socket = socket.socket()  # get instance

    server_socket.bind((host, port))

    print("Looking for a client to connect...")
    server_socket.listen(2) # The number is the max connections
    conn, address = server_socket.accept()  # Accepts a new connection
    print("Connection from: " + str(address))

    while True:
        # Receive data
        data = conn.recv(2048).decode()
        if not data:
            # If no data
            break
        print("From a connected computer: " + str(data))
        data = input('> ')
        conn.sendall(str.encode(data))  # Send data

    conn.close()  # Close connection


if __name__ == '__main__':
    server_program()