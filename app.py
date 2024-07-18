from flask import Flask, jsonify, request, render_template
import openai

app = Flask(__name__)

# Chave da API do OpenAI
openai.api_key = '********'

# IDs do assistente e da thread já criados
ASSISTANT_ID = 'asst_cRH4OVd2OCLbpRqDtkvtmFCC'
THREAD_ID = 'thread_UboNcnC7fGNnv7pFEuyKunI1'

# Rota: página de login
@app.route('/')
def login():
    return render_template('login.html')

# Rota: página inicial com o chatbot
@app.route('/chat')
def home():
    return render_template('index.html')

# Rota para lidar com a solicitação do frontend
@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']

    try:
        # Adiciona uma mensagem à thread existente
        message_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        # Recupera a mensagem do assistente
        bot_response = message_response['choices'][0]['message']['content']

        return jsonify({'response': bot_response})

    except Exception as e:
        print(f"Erro na solicitação para o assistente: {str(e)}")
        return jsonify({'response': 'Desculpe, ocorreu um erro na solicitação.'})

if __name__ == '__main__':
    app.run(debug=True)
