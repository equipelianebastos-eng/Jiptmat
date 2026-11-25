from google import genai


client = genai.Client(api_key="AQ.Ab8RN6JJOm6CmURWB_Y5qElfauRvwo2-cInNzzknplk9BByV9Q")
chat = client.chats.create(model="gemini-3.5-flash-lite",)

print("chat iniciado digite sair para encerrar.\n")

while True:
        pergunta = input("Você: ")
        
        
        if pergunta.lower() == "sair":
            print("encerrando")
            break
            
        
        resposta = chat.send_message(pergunta)
        print("\nIA", resposta.text, "\n")