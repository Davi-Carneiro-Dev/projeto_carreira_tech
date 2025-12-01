# Project Tech Python

Pequeno projeto Flask que integra com o modelo Gemini (via `google-genai`). Este README explica como instalar dependências, configurar a variável de ambiente `GEMINI_API_KEY` e testar o endpoint `/gemini`.

## Visão geral
- Backend: Flask (`main.py`)
- Templates em `templates/` e arquivos estáticos em `static/`
- A integração com o Gemini usa a variável de ambiente `GEMINI_API_KEY`

## Dependências (conferir `requirements.txt`)
- Flask
- python-dotenv
- google-genai

> O arquivo `requirements.txt` na raiz contém as versões mínimas que o projeto espera.

## Pré-requisitos
- Python 3.8+
- Git (opcional)

1. Instale as dependências:

```powershell
pip install -r requirements.txt
```

2. Configure a chave da API do Gemini (`GEMINI_API_KEY`). Você pode definir temporariamente na sessão do PowerShell ou criar um arquivo `.env` na raiz.

- Definir temporariamente (válido somente para a sessão atual):

```powershell
$env:GEMINI_API_KEY = 'sua_chave_aqui'
```

- Definir permanentemente para o usuário atual (PowerShell):

```powershell
setx GEMINI_API_KEY "sua_chave_aqui"
```

> Alternativa: criar um arquivo `.env` (na raiz do projeto) com o conteúdo:
>
> GEMINI_API_KEY=sua_chave_aqui
>
> Se o arquivo `.env` não existir no seu sistema por algum motivo, crie-o na raiz do projeto com a linha acima. O projeto carrega automaticamente `.env` durante o desenvolvimento via `python-dotenv`.

3. Execute a aplicação:

```powershell
python main.py
```

4. Abra no navegador:

```
http://127.0.0.1:5000/gemini
```

## Uso e comportamento do endpoint `/gemini`
- Envie uma pergunta pelo formulário na página `/gemini`.
- O backend (`main.py`) envia um prompt ao modelo Gemini pedindo explicitamente um *snippet HTML* (sem `<html>`, `<head>`, `<body>` nem `<script>`).
- Se o modelo devolver um snippet HTML, o template tentará inseri-lo diretamente (o template já trata possíveis fences de código como ```html ... ``` e remove esses blocos).
- Se a resposta não for HTML, o template exibirá o texto cru.

Observação: o código atual torna a renderização mais simples (o template insere HTML se detectar tags); para projetos em produção recomendo sanitizar o HTML no servidor ou com DOMPurify no cliente.

## Comandos Git úteis
- Adicionar e commitar mudanças:

```powershell
git add .
git commit -m "Atualiza README e configura integração Gemini"
git push
```

- Ignorar a pasta `.idea/`: já existe `.gitignore` com essa regra. Se você já cometeu `.idea/` e quer removê-la do repositório:

```powershell
# remove do índice (sem apagar localmente) e commita a remoção
git rm -r --cached .idea
git commit -m "Remove .idea do repositório"
git push
```

## Segurança
- Nunca comite chaves de API no repositório.
- Se você já cometeu a chave, diga que eu te guio para removê-la do histórico (BFG ou git filter-repo).
- Em produção, não confie em HTML fornecido por modelos sem sanitização.




