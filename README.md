# Central de IA para Vendedores Digitais

Ferramentas de IA simples para vendedores: responder cliente no WhatsApp (Quebra-Objeção X1), anúncios sem bloqueio, página de vendas, roteiro de vídeo e oferta com bônus.

## Rodar
```
pip install -r requirements.txt
export GEMINI_API_KEY=sua_chave   # grátis em aistudio.google.com/apikey
streamlit run app.py
```
No Streamlit Cloud, coloque `GEMINI_API_KEY = "..."` em Settings > Secrets. Se não houver chave, o app pede na tela inicial.

Modelo: variável `GEMINI_MODEL` (padrão no topo do `app.py`). Troque se o Google aposentar o modelo.
