# 🌌 API de Gerenciamento de Departamentos e Colaboradores

Este é um exemplo de uma API Flask que permite gerenciar departamentos e colaboradores de uma empresa usando um banco de dados SQLite.

## 🚀 Configuração
1. Certifique-se de ter o Python instalado. Se não tiver, você pode baixá-lo [aqui](https://www.python.org/downloads/).
2. Instale as dependências executando o seguinte comando no terminal: `pip install -r requirements.txt` ou `pip install flask flasgger`
3. Crie o banco de dados e insira dados de exemplo executando:`python database.py`
                            
## 🚀 Uso
1. Para iniciar o servidor Flask e acessar a API, execute: `python app.py`

## 🚀 Rotas Disponíveis

### 🌍 Listar Departamentos
URL: /departamentos

Método: GET

Descrição: Retorna uma lista de todos os departamentos disponíveis.

### 🌍 Listar Colaboradores de um Departamento
URL: /colaboradores/department

Método: GET

Parâmetros:
1. department (obrigatório): Nome do departamento para o qual deseja-se listar os colaboradores.
   
Descrição: Retorna uma lista de colaboradores pertencentes a um departamento específico, indicando se possuem dependentes.

### 🚀 Testando a API
1. Após iniciar o servidor Flask, você pode acessar a documentação da API em http://localhost:5000/apidocs.
2. Use ferramentas como Postman ou cURL para enviar solicitações HTTP para as rotas da API e verificar as respostas.
