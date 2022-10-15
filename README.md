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

* Cadastrar adotantes (adotante)
* Consultar adotantes (admin)
* Atualizar dados dos adotantes (adotante)
* Excluir cadastro de adotantes (adotante)
* Cadastrar endereço (adotante)
* Consultar endereço (adotante)
* Atualizar endereço (adotante)
* Excluir endereço (adotante)

### Gerenciar pedidos de adoção

* Cadastrar pedido de adoção (adotante)
* Consultar pedido de adoção (adotante)
* Listar pedidos de adoção (admin)
* Excluir pedidos de adoção (adotante)

### Gerenciar adoções

* Cadastrar adoção deferida (admin)
* Listar adoções deferidas (admin)
* Listar adoções indeferidas (admin)
* Atualizar status do pedido e da adoção (admin)
* Consultar adoção por email do adotante (admin)
* Consultar adoção por nome do pet (admin)

## Como acessar

### Swagger
  
  https://adotapets.onrender.com/docs

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
### Execução localhost
  ```
  $ uvicorn main:app --reload
   ```