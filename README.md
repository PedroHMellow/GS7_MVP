# Assistente de semáforo para pedestres

Este repositório é o **MVP do software da câmera ESP32-CAM** do projeto CitizenTech (Global Solution FIAP 2026.2).
No produto final, uma câmera vestível ESP32-CAM filma a rua à frente de uma pessoa cega ou com baixa visão.
O software reconhece faixa de pedestre e semáforo e transforma o que viu em um aviso simples.

Para esta demonstração, **a imagem da ESP32-CAM foi substituída por um vídeo público do YouTube** gravado em
uma rua de São Paulo. O vídeo passa pelo mesmo caminho que a câmera faria: cada quadro é enviado ao modelo
de visão computacional, e o resultado vira uma das mensagens abaixo. Trocar o vídeo pela câmera exige mudar
só a fonte da imagem; a análise e as regras continuam as mesmas.

O projeto tem duas partes:

- **`main.py` + `utility/`**: o núcleo em Python, que analisa o vídeo com o modelo do Roboflow.
- **`frontend/`**: uma página em React + Tailwind para apresentar o MVP. Ela toca o mesmo vídeo com as
  detecções do modelo por cima e mostra o aviso em tela, por voz e por vibração. A página não tem back-end:
  usa detecções já geradas e salvas em `frontend/public/dados/deteccoes-video.json`.


## Funcionalidades
- Reproduz um vídeo do YouTube em uma janela.
- A cada meio segundo, envia o frame atual ao modelo do Roboflow
  (classes: `pedestrian_crossing`, `green_light`, `red_light`, `vehicle`).
- A cada análise imprime no terminal uma das mensagens:
    - "Faixa de pedestre e semáforo verde a frente"
    - "Faixa de pedestre e semáforo vermelho a frente"
    - "Faixa de pedestre sem semáforo a frente"
    - "Semáforo verde a frente (sem faixa de pedestre)"
    - "Semáforo vermelho a frente (sem faixa de pedestre)"
    - "----------Nada relevante pode ser detectado----------"
    > Se houver semáforo verde e vermelho no mesmo frame, vale o de maior confiança.
- Os frames em que algo foi detectado (com as caixas desenhadas) aparecem
  numa SEGUNDA janela única, que é atualizada no mesmo instante da mensagem
  do terminal (não abre uma janela nova a cada detecção).
- Teclas: Q ou ESC para sair.


## Requisitos
- [Python 3.13](https://www.python.org/downloads/) ou mais recente
- [Node.js 20.19](https://nodejs.org/) ou mais recente (só para o front-end)
- Chave de API Roboflow
    - é necessário criar uma conta na plataforma de gerenciamento de sistemas de visão computacional [ROBOFLOW](https://roboflow.com/)
    - gerar sua chave de API em:
        ```
        Settings > API Keys > Generate New Key
        ```
- URL pública do Youtube (opcional)
    - utilize seu vídeo de preferência para ser analisado através de uma url pública do Youtube ou utilize o [vídeo padrão](https://www.youtube.com/watch?v=zIIIr0ZFQY4) ao **não definir essa variável**


## Como instalar e executar

### 1. Núcleo em Python (análise do vídeo)

1. Na pasta do projeto, crie e ative um ambiente virtual:
    ``` powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```
    > Se o PowerShell bloquear a ativação, rode antes:
    > `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

2. Instale as bibliotecas:
    ``` powershell
    python -m pip install -r .\requirements.txt
    ```

3. Crie um arquivo `.env` na pasta do projeto com a sua chave do Roboflow
   (e, se quiser, outro vídeo):
    ```
    ROBOFLOW_API_KEY=sua_chave_de_api_roboflow
    VIDEO_URL=https://youtu.be/seu_video_de_preferencia
    ```
    > O `.env` guarda a sua chave: não envie esse arquivo para o repositório.

4. Execute:
    ``` powershell
    python main.py
    ```
    Abrem duas janelas: o vídeo e as detecções. As mensagens aparecem no terminal.
    Para sair, aperte **Q** ou **ESC**.

### 2. Front-end (página de apresentação)

O front-end não precisa do Python nem da chave do Roboflow para rodar.

1. Entre na pasta e instale as dependências:
    ``` powershell
    cd frontend
    npm install
    ```

2. Rode em modo de desenvolvimento:
    ``` powershell
    npm run dev
    ```
    Abra http://localhost:5173 no navegador e aperte **Iniciar**.

3. Para gerar a versão de publicação (pasta `frontend/dist/`):
    ``` powershell
    npm run build
    ```

Mais detalhes da página em [frontend/README.md](frontend/README.md).
