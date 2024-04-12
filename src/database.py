import sqlite3

# Função para conectar ao banco de dados SQLite
def ConnectDB():
    return sqlite3.connect('company.db')

# Função para criar as tabelas
def CreateTables():
    conn = ConnectDB()
    cursor = conn.cursor()

    # Tabela de departamentos
    cursor.execute('''CREATE TABLE IF NOT EXISTS departamento (
                        id INTEGER PRIMARY KEY,
                        nome TEXT NOT NULL
                    )''')

    # Tabela de colaboradores
    cursor.execute('''CREATE TABLE IF NOT EXISTS colaborador (
                        id INTEGER PRIMARY KEY,
                        nome_completo TEXT NOT NULL,
                        departamento TEXT NOT NULL,
                        FOREIGN KEY (departamento) REFERENCES departamento(nome)
                    )''')

    # Tabela de dependentes
    cursor.execute('''CREATE TABLE IF NOT EXISTS dependente (
                        id INTEGER PRIMARY KEY,
                        nome TEXT NOT NULL,
                        colaborador TEXT NOT NULL,
                        FOREIGN KEY (colaborador) REFERENCES colaborador(nome_completo)
                    )''')

    conn.commit()
    conn.close()

# Função para inserir dados de exemplo
def InsertData():
    conn = ConnectDB()
    cursor = conn.cursor()

    # Inserir departamentos
    cursor.execute("INSERT INTO departamento (nome) VALUES ('Financeiro')")
    cursor.execute("INSERT INTO departamento (nome) VALUES ('RH')")
    cursor.execute("INSERT INTO departamento (nome) VALUES ('TI')")

    # Inserir colaboradores
    cursor.execute("INSERT INTO colaborador (nome_completo, departamento) VALUES ('João Silva', 'Financeiro')")
    cursor.execute("INSERT INTO colaborador (nome_completo, departamento) VALUES ('Maria Souza', 'RH')")
    cursor.execute("INSERT INTO colaborador (nome_completo, departamento) VALUES ('Pedro Santos', 'TI')")
    cursor.execute("INSERT INTO colaborador (nome_completo, departamento) VALUES ('Lucas Oliveira', 'Financeiro')")
    cursor.execute("INSERT INTO colaborador (nome_completo, departamento) VALUES ('Ana Santos', 'RH')")
    cursor.execute("INSERT INTO colaborador (nome_completo, departamento) VALUES ('Fernanda Silva', 'TI')")

    # Inserir dependentes
    cursor.execute("INSERT INTO dependente (nome, colaborador) VALUES ('Ana Silva', 'João Silva')")
    cursor.execute("INSERT INTO dependente (nome, colaborador) VALUES ('Carlos Souza', 'Maria Souza')")
    cursor.execute("INSERT INTO dependente (nome, colaborador) VALUES ('Gabriel Souza', 'Ana Santos')")
    cursor.execute("INSERT INTO dependente (nome, colaborador) VALUES ('Isabella Silva', 'Fernanda Silva')")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    CreateTables()
    InsertData()