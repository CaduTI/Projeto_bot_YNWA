import pyodbc

conn = pyodbc.connect(Driver ='SQL Server',Server = 'DESKTOP-2RPK1J7',Database = 'Base_bot')
print("Deu certo! Estamos conectado")
'''Get = "SELECT* FROM Usuario WHERE ID="
#inserir_usuário= 'INSERTO INTO () VALUES('{Classes.Usuario}')'
#agendar_consulta= 'INSERTO INTO () VALUES()'
#CRUD
#cursor = conn.cursor()
#CREATE
inserir_usuario=(f'INSERTO INTO Usuario(Nome,cpf,email) VALUES()')
cursor.execute(inserir_usuario)#Execute o comando
conn.commit()#confirma a informação no banco, usar somente em caso de edição no banco
result = cursor.fetchall()# lê o banco de dados
#READ
busca_consulta= 'SELECT* FROM "{}" WHERE ID='
cursor.execute(busca_consulta)#Execute o comando
result = cursor.fetchall()# lê o banco de dados
#UPDATE
#DELETE
'''