# Apis Adota Pets
Microsserviços para app de adoção de pets, desenvolvidos em Python, FastAPI, MongoDB, Motor Asyncio e Uvicorn, com Basic Auth.

Por meio dos endpoints, é possível:

### Gerenciar cadastro de pets

* Cadastrar pets (admin)
* Consultar pets por nome
* Listar todos os pets disponíveis para adoção
* Listar todos os pets adotados (admin)
* Atualizar dados e status dos pets (admin)
* Excluir cadastro de pets (admin)

### Gerenciar cadastro de adotantes

* Cadastrar adotantes
* Consultar adotantes
* Atualizar dados dos adotantes
* Excluir cadastro de adotantes
* Cadastrar endereço
* Consultar endereço
* Atualizar endereço
* Excluir endereço

### Gerenciar pedidos de adoção

* Cadastrar pedido de adoção
* Consultar pedidos de adoção
* Atualizar status do pedido de adoção (admin)
* Excluir pedidos de adoção 

### Gerenciar adoções

* Cadastrar adoção deferida (admin)
* Consultar adoção deferida (admin)
* Atualizar adoção (admin)

## Como acessar

### Swagger
  ```
  http://{url}/docs
  ```

### Níveis de acesso
* admin
* adotante

#### Usuário admin para teste
| email  | senha |
|------------|------------|
|admin@adotapets.com.br|SenhaSecreta@123|

#### Usuário adotante
Para criar um usuário adotante, acesse o endpoint /adotantes, método POST.
Utilize o e-mail e a senha cadastrados para acessar as APIs permitidas aos adotantes

## Como executar localmente

#### Variável de ambiente:
| name_env | value |
|------------|------------|
|KEY|connection string Atlas|

#### Instalação
* Create venv
    ```
    $ virtualenv venv --python=3.10
    ```
    Linux
    ```
    $ source venv/bin/activate
   ```
   Windows
    ```
    $ .\venv\Scripts\activate
   ```
* Instalar bibliotecas
     ```
     $ pip install -r requirements.txt
     ```
### Execução
  ```
  $ uvicorn.run("main:app", port=8000, reload=True, access_log=False)
   ```