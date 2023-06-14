from twilio.rest import Client

account_sid = 'SUA_ACCOUNT_SID'
auth_token = 'SEU_AUTH_TOKEN'

client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Olá! Esta é uma mensagem de teste do Twilio.',
    from_='SEU_NUMERO_TWILIO',
    to='NUMERO_DESTINATARIO'
)

print(message.sid)