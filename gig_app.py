import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
import seaborn as sns






# função para carregar o dataset
#@st.cache
def get_data(files):
    return pd.read_csv(files)

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
    df = get_data("janeiro.csv")
    df['Freq'] = df.iloc[:,1:5].apply(lambda x: x!=0, axis=1).sum(axis=1)
    df['Media'] = df.iloc[:,1:5].mean(axis=1)

    # Lançamento das notas por sábado
    sab1 = pd.DataFrame(df,columns = ['JOGADOR',df.columns[1]])
    sab1 = sab1.loc[(sab1!=0).all(axis=1)]
    sab2 = pd.DataFrame(df,columns = ['JOGADOR',df.columns[2]])
    sab2 = sab2.loc[(sab2!=0).all(axis=1)]
    sab3 = pd.DataFrame(df,columns = ['JOGADOR',df.columns[3]])
    sab3 = sab3.loc[(sab3!=0).all(axis=1)]
    sab4 = pd.DataFrame(df,columns = ['JOGADOR',df.columns[4]])
    sab4 = sab4.loc[(sab4!=0).all(axis=1)]


    # Melhor jogador do mês na coluna média
    maior = pd.DataFrame(df,columns = ['JOGADOR',df.columns[6]])

    # Pior do mês na coluna média
    pior = pd.DataFrame(df,columns = ['JOGADOR',df.columns[6]])


   # verificando o dataset
    st.subheader("Notas por dia jogado")

    # atributos para serem exibidos por padrão
    defaultcols = ["JOGADOR","2/1/2021","9/1/2021","16/1/2021","30/1/2021","Media"] 
    st_ms = st.multiselect("Valores", df.columns.tolist(), default=defaultcols)
    
    st.sidebar.header('Configurações')
    if st.sidebar.checkbox('Mostrar Tabela'):
        st.markdown("Tabela de Jogadores e Notas")
        # exibindo os top 8 registro do dataframe
        st.dataframe(df[st_ms].sort_values(by=['Media'], ascending=False))
        
    

    # inserindo um botão na tela
    btn_dados = st.sidebar.button("Dados Gerais")

    # verifica se o botão foi acionado
    if btn_dados:
        #st.subheader("Média Geral:")
        st.write('Média geral =  %.2f' %df.Media.mean())
        st.write('Quantidade de Jogadores = ',len(df))
        

    btn_melhores = st.sidebar.button("Melhores Notas")
    if btn_melhores:
        st.write('Maior Nota sabado 1: ',sab1[sab1[df.columns[1]] >= 8])
        st.write('Maior Nota sabado 2: ',sab2[sab2[df.columns[2]] >= 8])
        st.write('Maior Nota sabado 3: ',sab3[sab3[df.columns[3]] >= 9])
        st.write('Maior Nota sabado 4: ',sab4[sab4[df.columns[4]] >= 9])

    btn_piores = st.sidebar.button("Nem na Facol")
    if btn_piores:
        st.write('Menor Nota sabado 1: ',sab1[sab1.iloc[:, 1] < 7])
        st.write('Menor Nota sabado 2: ',sab2[sab2.iloc[:, 1] <= 4])
        st.write('Menor Nota sabado 3: ',sab3[sab3.iloc[:, 1] <= 3])
        st.write('Menor Nota sabado 4: ',sab4[sab4.iloc[:, 1] <= 3])

    # inserindo um botão na tela
    btn_Melhor_mes = st.sidebar.button("Melhor jogador do mês")
    if btn_Melhor_mes:
        st.write('Melhores jogadorores de Janeiro: ',maior[maior[df.columns[6]] >= 6.5][:3])
    

    btn_Pior_mes = st.sidebar.button("Pior jogador do mês")
    if btn_Pior_mes:
        st.write('O importante é participar: ',pior[pior[df.columns[6]] <= 2][:3])
        


elif choice == 'Fevereiro-21':
    # criando um dataframe
    df = get_data("fevereiro.csv")

    df['Freq'] = df.iloc[:,1:5].apply(lambda x: x!=0, axis=1).sum(axis=1)
    #df['Media'] = df.iloc[:,1:5].sum(axis=1) / df['Freq']
    df['Media'] = df.iloc[:,1:5].mean(axis=1) 

    # Lançamento das notas por sábado
    sab1 = pd.DataFrame(df,columns = ['JOGADOR',df.columns[1]])
    sab1 = sab1.loc[(sab1!=0).all(axis=1)]
    sab2 = pd.DataFrame(df,columns = ['JOGADOR',df.columns[2]])
    sab2 = sab2.loc[(sab2!=0).all(axis=1)]
    sab3 = pd.DataFrame(df,columns = ['JOGADOR',df.columns[3]])
    sab3 = sab3.loc[(sab3!=0).all(axis=1)]
    sab4 = pd.DataFrame(df,columns = ['JOGADOR',df.columns[4]])
    sab4 = sab4.loc[(sab4!=0).all(axis=1)]

    # Melhor jogador do mês
    maior = pd.DataFrame(df,columns = ['JOGADOR',df.columns[6]])

    # Pior do mês
    pior = pd.DataFrame(df,columns = ['JOGADOR',df.columns[6]])
    
    
   # verificando o dataset
    st.subheader("Notas por dia jogado")

    # atributos para serem exibidos por padrão
    defaultcols = ["JOGADOR","6/2/2021","13/2/2021","20/2/2021","27/2/2021","Freq","Media"] 
    st_ms = st.multiselect("Valores", df.columns.tolist(), default=defaultcols)
    
    st.sidebar.header('Configurações')
    if st.sidebar.checkbox('Mostrar Tabela'):
        st.markdown("Tabela de Dados")
        # exibindo os top 8 registro do dataframe
        st.dataframe(df[st_ms].sort_values(by=['Media'], ascending=False))
        
    

    # inserindo um botão na tela
    btn_dados = st.sidebar.button("Dados Gerais")

    # verifica se o botão foi acionado
    if btn_dados:
        #st.subheader("Média Geral:")
        st.write('Média geral =  %.2f' %df.Media.mean())
        st.write('Quantidade de Jogadores = ',len(df))

    btn_melhores = st.sidebar.button("Melhores Notas")
    if btn_melhores:
        st.write('Maior Nota sabado 1: ',sab1[sab1[df.columns[1]] >= 8])
        st.write('Maior Nota sabado 2: ',sab2[sab2[df.columns[2]] >= 8])
        st.write('Maior Nota sabado 3: ',sab3[sab3[df.columns[3]] > 8])
        st.write('Maior Nota sabado 4: ',sab4[sab4[df.columns[4]] >= 9])

    btn_piores = st.sidebar.button("Nem na Facol")
    if btn_piores:
        st.write('Menor Nota sabado 1: ',sab1[sab1.iloc[:, 1] <= 4])
        st.write('Menor Nota sabado 2: ',sab2[sab2.iloc[:, 1] < 4])
        st.write('Menor Nota sabado 3: ',sab3[sab3.iloc[:, 1] <= 4])
        st.write('Menor Nota sabado 4: ',sab4[sab4.iloc[:, 1] < 3])


    # inserindo um botão na tela
    btn_Melhor_mes = st.sidebar.button("Melhor jogador do mês")
    if btn_Melhor_mes:
        st.write('Melhores jogadorores de Fevereiro: ',maior[maior[df.columns[6]] > 7][:3])

    btn_Pior_mes = st.sidebar.button("Pior jogador do mês")
    if btn_Pior_mes:
        st.write('O importante é participar: ',pior[pior[df.columns[6]] <= 4][:3])
        

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







