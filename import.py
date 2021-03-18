import mysql.connector
import random
import pandas as pd 
#connexion au serveur sql
config = {
  'user': 'root',
  'password': 'password',
  'host': 'localhost',
  'port':'3300',
  'database': 'downjones',
  'raise_on_warnings': True,
}

connection = mysql.connector.connect(**config)
cursor=connection.cursor()
#recuperation de la liste apprenant à partir de la base de donnees 
cursor.execute("""select * from trade5 """)
#creation d'un tableau avec la liste des apprenants
dataun=cursor.fetchall()
datadeux=pd.DataFrame(dataun)

print(datadeux)