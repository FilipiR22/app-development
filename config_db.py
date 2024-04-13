from flask_mysqldb import MySQL
from app import app


app.config['MYSQL_HOST'] = 'localhost'  # Endereço do servidor MySQL
app.config['MYSQL_USER'] = 'seu_usuario'  # Nome de usuário do MySQL
app.config['MYSQL_PASSWORD'] = 'sua_senha'  # Senha do MySQL
app.config['MYSQL_DB'] = 'seu_banco_de_dados'  # Nome do banco de dados MySQL

mysql = MySQL(app)