import streamlit as st

# Título do relatório
st.title("Relatório de Informações de Teste")

# Informações de teste
st.subheader("Informações de Teste")
st.write("""
- Teste 1: Resultado A
- Teste 2: Resultado B
- Teste 3: Resultado C
""")

# Botão para realizar uma ação
if st.button("Clique aqui para realizar uma ação"):
    # Ação a ser realizada ao clicar no botão
    st.success("Ação realizada com sucesso!")
    # Você pode adicionar mais ações aqui, como salvar dados, chamar uma API, etc.
    print("Botão clicado! Ação realizada.")

# Adicione outros elementos do seu relatório, se necessário
