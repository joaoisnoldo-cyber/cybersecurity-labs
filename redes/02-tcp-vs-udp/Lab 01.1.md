## Laboratório prático

Foi desenvolvido um exemplo de comunicação utilizando sockets TCP em Python.

##Servidor

O servidor foi configurado para utilizar o endereço 127.0.0.1 e a porta 5000.

O servidor aguarda uma conexão de um cliente utilizando o método accept().

Após a conexão, os dados enviados pelo cliente são recebidos utilizando recv() e posteriormente convertidos de bytes para texto utilizando decode().

## Cliente

O cliente estabelece uma conexão com o servidor utilizando o endereço 127.0.0.1 e a porta 5000.

Após estabelecer a conexão, uma mensagem de texto é convertida para bytes utilizando encode() e enviada ao servidor através do método send().

## Fluxo da comunicação

Cliente → connect() → Servidor

Cliente → encode() → send() → Servidor

Servidor → recv() → decode() → mensagem

## Resultado observado

Durante o teste, o servidor identificou a conexão do cliente através do endereço:

127.0.0.1:53664

A porta 53664 foi atribuída automaticamente pelo sistema operacional ao cliente, enquanto a porta 5000 foi definida manualmente para o servidor.

A mensagem enviada pelo cliente foi recebida e exibida corretamente pelo servidor.
