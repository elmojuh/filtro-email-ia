# app.py
import os
import json
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)

try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    print(f"ERRO: Falha ao configurar a API do Gemini. Verifique sua chave. Erro: {e}")
    model = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_email():
    if not model:
        return jsonify({"error": "O modelo de IA não foi configurado corretamente."}), 500
        
    request_data = request.json
    email_text = request_data.get('text')

    if not email_text:
        return jsonify({"error": "Nenhum texto de email foi fornecido."}), 400

    prompt = f"""
    Analise o e-mail abaixo e retorne um objeto JSON com duas chaves: "category" e "suggested_response".

    1.  **"category"**: Deve ser "Produtivo" se o e-mail exigir uma ação (ex: resposta, tarefa, atualização).
        Deve ser "Improdutivo" se o e-mail não exigir uma ação clara (ex: agradecimento, felicitação, spam).

    2.  **"suggested_response"**: Crie uma sugestão de resposta curta e profissional em português, apropriada para cada categoria.

    O formato da resposta DEVE ser apenas o objeto JSON, sem nenhum texto adicional.

    E-mail para análise:
    ---
    {email_text}
    ---
    """

    try:
        api_response = model.generate_content(prompt)
        json_text = api_response.text.strip().replace("```json", "").replace("```", "").strip()
        print(f"JSON gerado: {json_text}")
        result = json.loads(json_text)
        return jsonify(result)

    except Exception as e:
        print(f"ERRO: Falha ao processar a requisição ou analisar o JSON. Erro: {e}")
        return jsonify({"error": "Ocorreu um erro ao se comunicar com a IA."}), 500

if __name__ == '__main__':
    app.run(debug=True)