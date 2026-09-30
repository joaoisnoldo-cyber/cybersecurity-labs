import socket
cliente = socket.socket()
cliente.connect(("127.0.0.1", 5000))
cliente.send("Oi Tudo bem?".encode())
