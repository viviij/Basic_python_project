# Projeto feito junto a hashtag
# Tendo como objetivo fazer um programa que leia algumas
# planilhas do excel e avise via SMS quando alguem bater
# um total > que 55 mil vendas#

import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9d19a674adcdc3e43f1ff4002967a978"
# Your Auth Token from twilio.com/console
auth_token = "f12e70fb6655df4ce83a132cf6a6a9fd"

client = Client(account_sid, auth_token)

list_of_months = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for month in list_of_months:
    sales_table = pd.read_excel(f'{month}.xlsx')
    if (sales_table['Vendas'] > 55000).any():
        seller = sales_table.loc[sales_table['Vendas']
                                 > 55000, 'Vendedor'].values[0]
        sales = sales_table.loc[sales_table['Vendas']
                                > 55000, 'Vendas'].values[0]

        message = client.messages.create(
            to="+5511943756513",
            from_="+14407036750",
            body="No mês {} alguém bateu a meta! O vendedor {} fez um total de {}R$ em vendas".format(month, seller, sales))

        print(message.sid)
