import socket
import sys

IP = socket.gethostbyname(socket.gethostname())
PORT = int(sys.argv[1])
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():

    # connecting to server side
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    # sending data to server
    data = sys.argv[2]
    client.send(data.encode(FORMAT))

    # receiving data from server
    data = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER] {data}")

if __name__ == "__main__":
    main()