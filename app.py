#Bibliotecas necessárias:
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#ler planilha, colocar o tipo (por exemplo csv):
clientes = pd.read_csv('./clientes.csv')

#percorrer linha por linha da planilha com o for:
for index, cliente in clientes.iterrows():
    #criar objeto e-mail:
    msg = MIMEMultipart()
    #Quem esta enviando:
    msg['From'] = 'SEU E-MAIL CORPORATIVO/PESSOAL ENTRE AS ASPAS'#EXEMPLO 'FULANO@GMAIL.COM'
    #quem recebe (está lendo a coluna do e-mail do cliente):
    msg['To'] = cliente['E-MAIL']
    #assunto (neste caso esta lendo o ID e nome do cliente):
    msg['subject'] = f"COBRANÇA - {cliente['ID']} - {cliente['NOME']}"
    #corpo do e-mail e tipo (lendo nome, vencimento, valor):
    message = f"Olá {cliente['NOME']},\n\n" \
          f"O boleto de vencimento {cliente['VENCIMENTO']} e valor R$ {cliente['VALOR']} está em aberto.\n\n" \
          f"Poderia verificar?\n\n"\
          f"Atenciosamente - Equipe Cordeiros"
    msg.attach(MIMEText(message,'plain'))

    #conectando e desconectando no servidor com a senha de app(pesquise como adquirir essa senha):
    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.starttls()
    server.login('SEU E-MAIL CORPORATIVO/PESSOAL ENTRE AS ASPAS', 'SENHA DE APLICAÇÃO ENTRE AS ASPAS')#EXEMPLO 'SAKDKNASJ524DASDJHAIH')
    server.sendmail(msg['From'], msg ['To'], msg.as_string())
    server.quit()
    
