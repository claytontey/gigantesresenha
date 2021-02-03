import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
import seaborn as sns





# função para carregar o dataset
#@st.cache
def get_data():
    return pd.read_csv("janeiro.csv")

def get_image():
    return st.image('gigantes.png', output_format="PNG")
    


# título
st.title("Gigantes da Resenha WebApp")

# subtítulo
st.markdown("Seja bem vindo e acompanhe com a gente o comportamento de nossos atletas rss! Jogos aos Sábados as 9:00")

menu = ['Janeiro-21','Fevereiro-21','Março-21','Abril-21','Maio-21','Junho-21','Julho-21','Agosto-21','Setembro-21','Outubro-21','Novembro-21','Dezembro-21']
choice = st.sidebar.selectbox("Menu",menu)

if choice == 'Janeiro-21':

    # criando um dataframe
    df = get_data()
    df['Media'] = df.iloc[:,1:5].mean(axis=1)
   
   # verificando o dataset
    st.subheader("Notas por dia jogado")

    # atributos para serem exibidos por padrão
    defaultcols = ["JOGADOR","2/1/2021","9/1/2021","16/1/2021","30/1/2021","Media"] 
    st_ms = st.multiselect("Valores", df.columns.tolist(), default=defaultcols)
    
    st.sidebar.header('Configurações')
    if st.sidebar.checkbox('Mostrar Tabela'):
        st.markdown("Tabela de Dados")
        # exibindo os top 8 registro do dataframe
        st.dataframe(df[st_ms].head(10))
        
    

    # inserindo um botão na tela
    btn_predict = st.sidebar.button("Melhores Resultados")

    # verifica se o botão foi acionado
    if btn_predict:
        #st.subheader("Média Geral:")
        st.write('Média geral =  %.2f' %df.Media.mean())
        st.write('Maior Nota: ',df[df['30/1/2021'] > 9])
        st.write('Top 3 Gigantes: ',df[df['Media'] > 5][:3])
        st.write('Nem na Facol: ',df[df['Media'] < 5][:3])


elif choice == 'Fevereiro-21':
    st.title('Arquivo com os dados ainda não disponível!')
    st.subheader('**Enquanto isso, curta a foto do atual campeão :-)**')
    get_image()

elif choice == 'Março-21':
    st.title('Arquivo com os dados ainda não disponível!')
    st.subheader('**Enquanto isso, curta a foto do atual campeão :-)**')
    get_image()

elif choice == 'Abril-21':
    st.title('Arquivo com os dados ainda não disponível!')
    st.subheader('**Enquanto isso, curta a foto do atual campeão :-)**')
    get_image()

elif choice == 'Maio-21':
    st.title('Arquivo com os dados ainda não disponível!')
    st.subheader('**Enquanto isso, curta a foto do atual campeão :-)**')
    get_image()

elif choice == 'Junho-21':
    st.title('Arquivo com os dados ainda não disponível!')
    st.subheader('**Enquanto isso, curta a foto do atual campeão :-)**')
    get_image()

elif choice == 'Julho-21':
    st.title('Arquivo com os dados ainda não disponível!')
    st.subheader('**Enquanto isso, curta a foto do atual campeão :-)**')
    get_image()

elif choice == 'Agosto-21':
    st.title('Arquivo com os dados ainda não disponível!')
    st.subheader('**Enquanto isso, curta a foto do atual campeão :-)**')
    get_image()

elif choice == 'Setembro-21':
    st.title('Arquivo com os dados ainda não disponível!')
    st.subheader('**Enquanto isso, curta a foto do atual campeão :-)**')
    get_image()

elif choice == 'Outubro-21':
    st.title('Arquivo com os dados ainda não disponível!')
    st.subheader('**Enquanto isso, curta a foto do atual campeão :-)**')
    get_image()

elif choice == 'Novembro-21':
    st.title('Arquivo com os dados ainda não disponível!')
    st.subheader('**Enquanto isso, curta a foto do atual campeão :-)**')
    get_image()

else:
    st.title('Arquivo com os dados ainda não disponível!')
    st.subheader('**Enquanto isso, curta a foto do atual campeão :-)**')
    get_image()




# mapeando dados do usuário para cada atributo



