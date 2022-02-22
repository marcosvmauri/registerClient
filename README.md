
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

![Logo](https://fileclientbucket.s3.us-east-1.amazonaws.com/Diagrama%20AWS%20Register%20Client.jpeg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXNhLWVhc3QtMSJHMEUCIQCcayFSGnGCaDu0i5e3QFGS6G9K687JkPjq0cGkBg%2FjzwIgVgjzYWDKaLL3%2FYPx1zbnjEW7Xr%2F6nP8ztJCMTNohtrUq5AIIUBAAGgwxNDY0NDg1MDc4NTQiDLaIX9i4GeHTjF%2FSsCrBAjXgLI361m65DedNtd5X5a%2FDmezpK4lZLPulRzp6u63jNPY2aO1OWQdhqnHUw2Wsjgi8sDjs5EvcNiRMzZewpOMMKATJvQAOhOXUzFJPn9IhvKF9DkeACiNyhFSVhk9p%2BLMkaFjCyA4riX91ChGXNmeAuDyrYhPQ8JH7SObUGcgCe7Oqvnmpv2JxgH5Vfp3HtuGFboqlend0tCBD%2FhDBWmNlv671em77Q0j4dEEgHL8FIu2uNwB7%2BTOEJ6UKhUGR6Mv3tP8i3KBeuHY6TGUekupGC30dklximCT33twGYHT1QWvIfQshrJ8bAt05uDyTLpvC2jtK1BIs93g4ZrzWRENXpavqYhABI9z1XEFhgI4Kgz8V6nV0uB1FEP5E%2FYOe4yp9z8Z95P6ICkr0iQANfAyLsvM2bW7c4sI5wPNoGIVIqDD2sdCQBjqzAqg7b4i6zRH550GA2EV4zypaluM%2Fs%2B%2F8FvaGuj2JMVATkY9MKnbIEQCTcahI0QxmDHenqBE8E94ItrhzKGOvjqH0megBMMI78qqAu9dt3nR%2F0H0FO67x50225yMDuwqmWnBoWpiG6RfaB%2Fg16%2Bw4Tw5I%2FXNw727YNg7VPb8S0DlU%2B50QfPhQoooVRshbVp8h6bQkxvBSQiLOQwJyBqG8B2jKLMpHDUCx5BEEL1ZWi8SLDQDD%2BjyiTA%2F%2FhfXnQXPZA2zRIy0iO6%2FZLvJLa%2Bp48J1AXUGX5Bf%2BpqJQ%2FF%2FO73bGX0UYEzDGXn%2BFscp5g6AMmj%2B8XYyR7NjTjwM%2B0uUIRrnSchteY8YAso53EoPkxe3miUYxxME9GVAMWU5VTdyxOGa6MYgx%2BpAARAZU8I0CwS%2BEPV8%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220222T104127Z&X-Amz-SignedHeaders=host&X-Amz-Expires=604800&X-Amz-Credential=ASIASEGIC4PHEACK772Z%2F20220222%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=9ebc2c705ac62f158a9323eab9f9089000a51e3a7c809a3e866bb264bb2931d5)

