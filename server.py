import socket
import threading
import sys

IP = socket.gethostbyname(socket.gethostname())
PORT = int(sys.argv[1])
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DATA = []

def handle_client(conn, addr):

    # receiving data from client
    data = conn.recv(SIZE).decode(FORMAT)

    # adding data to DATA array
    DATA.append(data)

    # displaying metric from specific client
    print(f"[MONITORING] {data.upper()} had {DATA.count(data)} attempt")

    # sending back data with metric to client
    data = f"{DATA.count(data)} ssh log-in attempts were made at {data.upper()}"
    conn.send(data.encode(FORMAT))
    
    # closing connection with client
    conn.close()

def main():

    # binding server
    print("[STARTING] AlphaServer is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)

    # listening for client's connection
    server.listen()
    print(f"[LISTENING] AlphaServer is listening on {IP}:{PORT}")

    # multithreading for handle multiple client
    # running handle_client function
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()