from google import genai
client = genai.Client(api_key=*AQ.Ab8RN60J0m6CmURWB_Y5qElfauRvwo2-
cInNzzknp1k9BByV9QiẠồ)
chat = client.chats.create(model="gemini-3.5-flash-lite",)
print ("chat iniciado digite sair para encerrar. \n")
while True:
pergunta = input ("Você: *)
if pergunta.lower () ==
*sair":
print ("encerrando")
break
resposta = chat.send_message(pergunta)
print(*\nIA*, resposta,text, \n")
