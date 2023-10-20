import pandas as pd
import uuid
import re
# Extração de Dados do arquivo .csv
df = pd.read_csv('SDW2023.csv',sep=';',engine='python')
user_ids = df['ID'].tolist()
user_names = df['NOME'].tolist()
user_emails = df['EMAIL'].tolist()
birth_date = df['DATA NASCIMENTO'].tolist()
#print(user_ids) // TESTE PARA VERIFICAR OS IDs
#print(user_names) // TESTE PARA VERIFICAR OS NOMES
#print(user_emails) // TESTE PARA VERIFICAR OS EMAILS
#print(birth_date) // TESTE PARA VERIFICAR AS DATAS DE ANIVERSARIOS

## Transformação e Carga
print('\n')
i=0
while i < len(birth_date):
    if birth_date[i].startswith("20/10/"):
        print("*========================================================*")
        print("CLIENTE: ", user_names[i], birth_date[i], '\n')
        print(f"Parabéns pelo seu aniversário, como presente você ganhou um código de desconto exclusivo para usar com o que quiser no nosso Shopping da Santander!\nSegue o código: {uuid.uuid4()} \n")
    i += 1
