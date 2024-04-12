from flask import Flask, request, jsonify
import sqlite3
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# Função para conectar ao banco de dados SQLite
def ConnectDB():
    return sqlite3.connect('company.db')

# Função para verificar se um colaborador possui dependentes
def ValidDependents(conn, CollaboratorName):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM dependente WHERE colaborador = ?", (CollaboratorName,))
    count = cursor.fetchone()[0]
    return count > 0

# Rota para listar todos departamento
@app.route('/departamentos')
def GetDepartments():
    """
    Essa rota retorna uma lista de todos os departamentos disponíveis.
    ---
    tags:
      - Departamentos
    responses:
      200:
        description: Retorna uma lista de departamentos.
        schema:
          type: array
          items:
            type: object
            properties:
              departamento:
                type: string
                description: Nome do departamento.
    """
    conn = ConnectDB()
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM departamento")

    Departments = [row[0] for row in cursor.fetchall()]
    conn.close()

    # Transformar a lista de nomes de departamentos em uma lista de dicionários
    list = [
        {
            "Departamento": DepartmentList
        } for DepartmentList in Departments
      ]
    return jsonify(list)


# Rota para listar colaboradores de um departamento
@app.route('/colaboradores/<department>')
def listar_colaboradores(department):
    """
    Esta rota retorna uma lista de colaboradores pertencentes a um departamento específico.
    ---
    tags:
      - Colaboradores
    parameters:
      - name: departamento
        in: path
        type: string
        required: true
        description: Nome do departamento para o qual deseja-se listar os colaboradores.
    responses:
      200:
        description: Retorna uma lista de colaboradores do departamento.
        schema:
          type: array
          items:
            type: object
            properties:
              nome_completo:
                type: string
                description: Nome completo do colaborador.
              have_dependents:
                type: boolean
                description: Indica se o colaborador possui dependentes.
      400:
        description: O departamento fornecido não existe no banco de dados.
        schema:
          type: object
          properties:
            error:
              type: string
              description: Mensagem de erro indicando que o departamento não existe.
    """
    conn = ConnectDB()
    cursor = conn.cursor()

    # Verificar se o departamento fornecido existe no banco de dados
    cursor.execute("SELECT nome FROM departamento WHERE nome = ?", (department,)) 
    DepartmentExists = cursor.fetchone()

    if not DepartmentExists:
        conn.close()
        return jsonify(
            {
                'error': 'Departamento não existe'
            }), 400

    cursor.execute("SELECT nome_completo FROM colaborador WHERE departamento = ?", (department,))

    CollaboratorData = [
        {
            "Nome_Completo": row[0], 
            "Have_Dependents": ValidDependents(conn, row[0])
        } for row in 
    
    cursor.fetchall()
    ]

    conn.close()
    return jsonify(CollaboratorData)


if __name__ == '__main__':
    app.run(debug=True)