# AutoU - Filtro Inteligente de E-mails

Este projeto é uma solução para o Case Prático de Desenvolvimento da AutoU. Trata-se de uma aplicação web que utiliza a IA do Google (gemini-1.5-flash - escolha pessoal) para classificar e-mails como "Produtivo" ou "Improdutivo" e sugerir respostas automáticas.

## 🔗 Link da Aplicação

**É possivel testar a aplicação ao vivo aqui:** [https://filtro-email-ia.vercel.app/](https://filtro-email-ia.vercel.app/)

## ✨ Funcionalidades Principais

-   **Classificação com IA:** Classifica o conteúdo de e-mails em categorias (Produtivo/Improdutivo).
-   **Sugestão de Resposta:** Gera uma resposta automática e contextualizada com base na classificação.
-   **Interface Web Simples:** Permite que qualquer usuário cole o texto de um e-mail e receba a análise instantaneamente.
-   **Deploy Contínuo:** Integrado com a Vercel para deploys automáticos e simplificado para cada atualização no código.

## 🛠️ Tecnologias Utilizadas

-   **Backend:** Python 3, Flask
-   **Inteligência Artificial:** Google Gemini API (gemini-1.5-flash)
-   **Frontend:** HTML5, CSS3, JavaScript (puro)
-   **Hospedagem:** Vercel

## 🏁 Como Executar Localmente

Siga os passos abaixo para rodar o projeto na sua máquina.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/elmojuh/filtro-email-ia.git](https://github.com/elmojuh/filtro-email-ia.git)
    cd filtro-email-ia
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Crie o ambiente
    python -m venv .venv
    # Ative o ambiente (Windows - Git Bash)
    source .venv/Scripts/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    - Crie um arquivo chamado `.env` na raiz do projeto.
    - Adicione sua chave da API do Gemini:
      ```
      GEMINI_API_KEY="SUA_CHAVE_DE_API_AQUI"
      ```
    - Se usar outra LMM como GPT ou outra, deve-se substituir a biblioteca ```google.generativeai``` usada com o ```gemini```

5.  **Execute a aplicação:**
    ```bash
    python app.py
    ```

6.  Abra `http://127.0.0.1:5000` no seu navegador.