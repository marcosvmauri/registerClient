
# RegisterClient

Aplicação orientada à eventos utilizando serviços AWS para cadastro de clientes.



## Tecnologias

- Python 3.10
- AWS Lambada
- AWS Chalice
- AWS SQS
- AWS SNS
- AWS S3
- AWS Dyanamo


## Documentação da API

#### Retorna todos os itens

```http
  POST /
```

| Parâmetro   | Tipo       | Descrição                                    |
| :---------- | :--------- | :--------------------------------------------|
| `dataClient` | `object` | **Obrigatório**. Dados de registro do cliente |

#### Retorna uma mensagem


## Desenho da aplicação

![Logo](https://i.ibb.co/tsT7JvW/Diagrama-AWS-Register-Client.jpg)

