import sqlite3

conexao = sqlite3.connect('nocoes_de_banco_de_dados/atividade_avaliativa_21-03/dados.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pratos (
                   
               
               
               )


''')