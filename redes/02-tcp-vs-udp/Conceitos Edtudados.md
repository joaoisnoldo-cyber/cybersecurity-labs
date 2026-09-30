# Lab 02 — TCP vs UDP

## Objetivo

Compreender as principais diferenças entre os protocolos TCP e UDP, observando suas características, funcionamento e utilização no transporte de dados entre aplicações.

##Conceitos estudados

1. O que é TCP?

Protocolo de transmissão de dados que atua na camada 4 do modelo OSI. É considerado um protocolo confiável, pois busca garantir a ordem, o recebimento e a integridade dos dados, utilizando recursos como FEC e ARQ.

2. O que é UDP?

Protocolo de transmissão de dados que atua na camada 4 do modelo OSI. É considerado um protocolo não confiável, pois verifica a integridade dos dados através de checksum, mas não garante o recebimento nem a ordem de recebimento dos dados.

3. Qual é a principal diferença entre eles?

O TCP busca garantir a confiabilidade da comunicação, enquanto o UDP apenas realiza a verificação de integridade dos dados através de checksum. Caso um dado não chegue ao destino, o UDP não possui um mecanismo próprio para garantir sua retransmissão ou sua entrega em ordem.

## Prática

Nesta prática serão observadas as diferenças entre TCP e UDP por meio de uma comunicação entre processos.
