import openai
from config import *

openai.api_key = api_key

# Função para gerar texto relacionado ao ODRL
def generate_odrl_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text

# Exemplo de uso
if __name__ == "__main__":
    prompt = "Gere uma descrição do ODRL:"
    odrl_text = generate_odrl_text(prompt)
    print(odrl_text)
