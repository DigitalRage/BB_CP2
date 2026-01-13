import socket

# Configuration
HOST = '172.22.17.227'  # The server's hostname or IP address
PORT = 65432                # The port used by the server

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            print(f"Connected to server {HOST}:{PORT}")
            while True:
                # Get input from the user
                message = input("You: ")
                if message.lower() == 'quit':
                    break
                # Send the message encoded to utf-8
                s.sendall(message.encode('utf-8'))
        except ConnectionRefusedError:
            print("Connection failed. Ensure the server is running and the IP address is correct.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    start_client()