from flask import Flask, render_template, request
from google import genai
import os
try:
    from dotenv import load_dotenv
except Exception:
    def load_dotenv():
        return None


# carrega um arquivo .env (se existir) para facilitar desenvolvimento local
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre_equipe')
def sobre_equipe():
    return render_template('sobre_equipe.html')

@app.route('/backend')
def carreira_backend():
    return render_template('back_end.html')

@app.route('/frontend')
def carreira_frontend():
    return render_template('front_end.html')

@app.route('/dados')
def carreira_dados():
    return render_template('dados.html')

@app.route("/gemini", methods=["GET", "POST"])
def gemini_page():
    response = None

    if request.method == "POST":
        pergunta = request.form.get("pergunta")
        if pergunta:
            response = get_response_from_gemini(pergunta)


    return render_template("gemini.html", response=response)


def get_response_from_gemini(user_message):
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        return ("Erro: a chave de API do Gemini não está configurada. "
                "Defina a variável de ambiente GEMINI_API_KEY.")

    client = genai.Client(api_key=api_key)

    prompt = f"""Voce é um professor de programação experiente e didático.
    sua missao é ajudar estudantes a aprender a programação de forma clara e objetiva.

           pergunta do aluno:{user_message}

    forneça uma resposta educativa, com exemplos praticos quando relevante.

    IMPORTANTE: para facilitar a renderização no front-end, responda APENAS com um SNIPPET HTML que contenha o conteúdo da resposta. Não forneça um documento HTML completo (sem <html>, <head> ou <body>). Use tags semânticas simples, por exemplo: <p>, <strong>, <em>, <ul>, <ol>, <li>, <code>, <pre>, <h2>, <h3>, e <a href="..."> para links.

    Não inclua <script>, event handlers inline (onclick, onmouseover, etc.) nem estilos inline (style="..."). Se precisar indicar código, use <pre><code>...</code></pre>.

    Exemplo de saída desejada (apenas um snippet):
    <p>Resposta curta introdutória.</p>
    <h3>Exemplo:</h3>
    <pre><code>print('hello')</code></pre>

    Retorne somente o HTML do snippet e nada mais.
    """

    return client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt
    ).text

if __name__ == '__main__':
    app.run(debug=True)
