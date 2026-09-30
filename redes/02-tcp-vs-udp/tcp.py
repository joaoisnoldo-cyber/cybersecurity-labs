import socket
servidor = socket.socket()
servidor.bind(("127.0.0.1", 5000))
servidor.listen()
conexao, endereco = servidor.accept()

print("Cliente Conectado:", endereco)

dados = conexao.recv(1024)

mensagem = dados.decode()

print("Isto foi enviado:", mensagem)
