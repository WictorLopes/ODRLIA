import openai
from config import *
from flask import Flask, request, jsonify
import re


openai.api_key = api_key

app = Flask(__name__)

def read_file_odrl(file_path):
    try:
        with open(file_path, 'r') as file:
            odrl_info = file.read()
        return odrl_info
    except Exception as e:
        print(f"Error reading ODRL file: {e}")
        return None

def build_prompt(odrl_info):
    prompt = f"Extract the BUs from the ODRL document below:\n{odrl_info}\n\nExtracted BUs:"
    return prompt


def extract_bus_from_bnf_file(file_path):
    bu_pattern = r"BU_\d+\.bnf" 
    bus = [] 
   

    try:
        with open(file_path, 'r') as file:
            content = file.read()

            
            matches = re.findall(bu_pattern, content)

            
            for match in matches:
                bus.append(match)

        return bus

    except Exception as e:
        print(f"Erro na leitura do arquivo .bnf: {e}")
        return None

def process_odrl_file(file_path):
    odrl_info = read_file_odrl(file_path)
    
    prompt = build_prompt(odrl_info)
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150  
    )
    
    generated_text = response.choices[0].text
    
    extracted_bus = extract_bus_from_bnf_file(generated_text)
    
    return extracted_bus

@app.route('/generate-odrl-text', methods=['POST'])
def generate_odrl_text():
    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "The 'prompt' parameter is missing from the request body"}), 400

    return jsonify({"odrl_text": process_odrl_file(prompt)})


if __name__ == "__main__":
    odrl_file = "../Examples/expl1/BU_0.bnf"
    extracted_bu = process_odrl_file(odrl_file)

    
    if extracted_bu:
        print("Extracted BUs:")
        for bu in extracted_bu:
            print(bu)
    else:
        print("No BU was extracted.")

