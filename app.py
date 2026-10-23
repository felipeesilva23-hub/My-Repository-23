import streamlit as st
import google.generativeai as genai

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Central de IA para Vendedores Digitais",
    page_icon="⚡",
    layout="wide"
)

# Título da Aplicação
st.title("⚡ Central de Inteligência para Vendedores Digitais")
st.caption("Aumente as suas vendas e otimize o seu tempo com ferramentas especializadas de IA.")

# Configuração da API Key do Gemini no Painel Lateral
st.sidebar.header("⚙️ Configuração")
api_key = st.sidebar.text_input("Insira a sua API Key do Gemini (Gratuita):", type="password")

if api_key:
    genai.configure(api_key=api_key)
else:
    st.sidebar.warning("⚠️ Insira a sua API Key do Google AI Studio para ativar as ferramentas.")

# Menu de Navegação entre os 5 Módulos
st.sidebar.markdown("---")
st.sidebar.header("🛠️ Ferramentas Disponíveis")
modulo = st.sidebar.radio(
    "Escolha o Módulo:",
    [
        "1. Recuperador de WhatsApp (X1)",
        "2. Gerador de Ads Anti-Bloqueio",
        "3. Auditor de Páginas (CRO)",
        "4. Roteirista de Vídeos Curtos",
        "5. Arquiteto de Oferta & Bónus"
    ]
)

# Função auxiliar para chamar a API do Gemini
def gerar_resposta(system_prompt, user_input):
    if not api_key:
        st.error("Por favor, insira a sua API Key no painel lateral.")
        return None
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt_completo = f"{system_prompt}\n\n[DADOS DO USUÁRIO]:\n{user_input}"
        with st.spinner("A gerar resposta com Inteligência Artificial..."):
            response = model.generate_content(prompt_completo)
            return response.text
    except Exception as e:
        st.error(f"Erro ao conectar com a API: {e}")
        return None

# ==========================================
# MÓDULO 1: WHATSAPP X1
# ==========================================
if modulo == "1. Recuperador de WhatsApp (X1)":
    st.header("💬 Recuperador de Vendas no WhatsApp (X1)")
    st.write("Gere respostas persuasivas para quebrar objeções de clientes no atendimento individual.")
    
    col1, col2 = st.columns(2)
    with col1:
        nicho = st.text_input("Nicho ou Nome do Produto:", placeholder="Ex: Curso de Inglês / E-book de IA")
        preco = st.text_input("Preço do Produto:", placeholder="Ex: R$ 25,00")
    with col2:
        objecao = st.text_area("Mensagem ou Objeção do Cliente:", placeholder="Ex: 'Está muito caro' ou 'Vou falar com a minha esposa'")
        
    if st.button("🚀 Gerar Respostas para o WhatsApp", type="primary"):
        if objecao and nicho:
            system_prompt = f"""
            Tu és um Especialista de Elite em Vendas Diretas e Fechamento no WhatsApp (X1).
            Analisar a objeção: "{objecao}", Produto: "{nicho}", Preço: "{preco}".
            Gera exatamente 3 opções de respostas de alta conversão formatadas para mensagens de WhatsApp (uso de emojis estratégicos, frases curtas e quebras de linha).
            Estrutura:
            ### 🛡️ Análise da Objeção
            ### 💬 Opção 1: Empática e Prova Social
            > [Texto pronto]
            ### ⚡ Opção 2: Foco em Escassez e Urgência
            > [Texto pronto]
            ### 🎯 Opção 3: Inversão de Risco e Garantia
            > [Texto pronto]
            """
            resultado = gerar_resposta(system_prompt, f"Objeção: {objecao}")
            if resultado:
                st.markdown(resultado)
        else:
            st.warning("Preencha pelo menos o nicho e a objeção do cliente.")

# ==========================================
# MÓDULO 2: ADS ANTI-BAN
# ==========================================
elif modulo == "2. Gerador de Ads Anti-Bloqueio":
    st.header("📢 Gerador de Anúncios com Verificador Anti-Bloqueio")
    st.write("Crie copys de anúncios para Meta Ads ou TikTok Ads reduzindo o risco de bloqueio.")
    
    produto = st.text_input("Nome do Produto / Serviço:")
    dor = st.text_input("Dor ou Desejo Principal do Público:")
    canal = st.selectbox("Plataforma de Anúncios:", ["Meta Ads (Facebook/Instagram)", "TikTok Ads"])
    
    if st.button("🚀 Gerar Anúncios & Auditar Risco", type="primary"):
        if produto and dor:
            system_prompt = f"""
            Tu és um Gestor de Tráfego Pago e Copywriter Sênior especializado nas diretrizes de políticas de anúncios do Meta e TikTok.
            Produto: {produto}, Dor: {dor}, Canal: {canal}.
            Gera 3 variações de copys e uma auditoria de risco de bloqueio (Anti-Ban Audit).
            Estrutura:
            ### ⚠️ Auditoria Anti-Bloqueio (Anti-Ban Check)
            - Nível de Risco (🟢 Baixo | 🟡 Médio | 🔴 Alto) e Termos Sensíveis
            ### 📢 Variação 1: Foco na Dor Principal
            ### 📢 Variação 2: Foco no Desejo / Transformação
            ### 📢 Variação 3: Foco em Curiosidade / Quebra de Mito
            """
            resultado = gerar_resposta(system_prompt, f"Produto: {produto}, Dor: {dor}")
            if resultado:
                st.markdown(resultado)

# ==========================================
# MÓDULO 3: AUDITOR CRO
# ==========================================
elif modulo == "3. Auditor de Páginas (CRO)":
    st.header("📊 Auditoria de Páginas de Vendas (CRO)")
    st.write("Identifique falhas na sua Landing Page e receba reescritas de alto impacto.")
    
    texto_pagina = st.text_area("Cole aqui o texto da Headline ou da Promessa Principal da sua página:", height=150)
    preco_formato = st.text_input("Preço e Formato do Produto (ex: E-book de R$ 25):")
    
    if st.button("🚀 Auditar Página de Vendas", type="primary"):
        if texto_pagina:
            system_prompt = f"""
            Tu és um Especialista em Otimização de Taxa de Conversão (CRO) e Vendas Digitais.
            Analisa o texto: "{texto_pagina}" para o produto de preço/formato: "{preco_formato}".
            Estrutura a resposta:
            ### 📊 Diagnóstico da Página (Nota de 0 a 10 para Clareza e Força)
            ### 🚨 Top 3 Falhas Críticas de Conversão
            ### ✏️ Reescrita de Alto Impacto (2 Headlines Otimizadas + 1 Botão CTA)
            """
            resultado = gerar_resposta(system_prompt, texto_pagina)
            if resultado:
                st.markdown(resultado)

# ==========================================
# MÓDULO 4: ROTEIRISTA DE VÍDEOS
# ==========================================
elif modulo == "4. Roteirista de Vídeos Curtos":
    st.header("🎬 Roteirista de Vídeos Curtos (Reels / TikTok / Shorts)")
    st.write("Crie roteiros dinâmicos focados nos primeiros 3 segundos para reter o público.")
    
    tema = st.text_input("Tema do Vídeo:")
    objetivo = st.selectbox("Objetivo Principal:", ["Atração Orgânica / Viral", "Venda Direta / Conversão"])
    
    if st.button("🚀 Criar Roteiro de Vídeo", type="primary"):
        if tema:
            system_prompt = f"""
            Tu és um Criador de Conteúdo Viral e Estrategista para vídeos curtos na vertical.
            Tema: {tema}, Objetivo: {objetivo}.
            Gera um roteiro estruturado em tabela com:
            - 00-03s (Gancho/Hook)
            - 03-15s (Conteúdo/Retenção)
            - 15-25s (Chamada para Ação / CTA)
            Inclui também Dicas de Edição e Música Sugerida.
            """
            resultado = gerar_resposta(system_prompt, tema)
            if resultado:
                st.markdown(resultado)

# ==========================================
# MÓDULO 5: ARQUITETO DE OFERTAS
# ==========================================
elif modulo == "5. Arquiteto de Oferta & Bónus":
    st.header("🎁 Arquiteto de Oferta Irresistível & Bónus")
    st.write("Crie bónus de alto valor percebido e ideias de Order Bumps para o checkout.")
    
    prod_principal = st.text_input("Nome/Descrição do Produto Principal:")
    preco_oferta = st.text_input("Preço Pretendido (ex: R$ 25,00):")
    
    if st.button("🚀 Arquitetar Oferta Irresistível", type="primary"):
        if prod_principal:
            system_prompt = f"""
            Tu és um Estrategista de Lançamentos e Arquitetura de Ofertas Irresistíveis (Estilo Alex Hormozi).
            Produto: {prod_principal}, Preço: {preco_oferta}.
            Estrutura:
            ### 🎁 Estrutura da Oferta Irresistível (Nome Comercial + Valor Percebido)
            ### 📦 3 Bónus de Alto Valor Percebido
            ### 💰 Ideia de Order Bump para o Checkout
            """
            resultado = gerar_resposta(system_prompt, prod_principal)
            if resultado:
                st.markdown(resultado)
