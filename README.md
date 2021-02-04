# gigantesresenha (Aplicativo para controle de notas de jogadores)

Aplicativo Web desenvolvido para controlar frequencia de indivíduos em jogos de finais de semana. Durante as partidas (que são realizadas semanalmente), uma nota referente ao desenvolvimento individual é anotada, buscando ao final de cada mês, apresentar os melhores (e piores) jogadores do mês, consequentemente, ao final do ano será apresentado os melhores e os piores do ano.

## Informações sobre o desenvolvimento.

O conjunto de dados possui a extensão .csv, sendo alimentado ao final de cada partida e dividido por meses, tendo seu nome referenciado ao respectivo mês de anotação das notas.

O código foi desenvolvido na linguagem *Python* utilizando várias bibliotecas, principalmente a biblioteca [Streamlit](https://www.streamlit.io/). Após a conclusão do código, o mesmo foi hospedado no *Github* e seu *Dashboard* hospedado no site [Heroku](https://dashboard.heroku.com/). Para esse processo, é necessário a instalação de um pacote [pipreqs](https://pypi.org/project/pipreqs/) através do comando: *sudo pip3 install pipreqs*, em seguida executá-lo. Esse pacote será responsável pela criação do arquivo **requeriments.txt** que apresentará todas as bibliotecas utilizadas no desenvolvimento do código fonte. e necessário para o *dashboard*.
Será necessário a criação de mais outro arquivo, o **setup.sh** contendo as seguintes linhas de código:

'''
mkdir -p ~/.streamlit/

echo "[general]

email = \"**Seu endereço de e-mail**\"

" > ~/.streamlit/credentials.toml

echo "[server]

headless = true

port = $PORT

enableCORS = false

" > ~/.streamlit/config.toml
'''

## Acesso e contato:

O acesso ao *App* pode ser realizado através o [link](https://gigantesresenha.herokuapp.com/). Para contatos, enviar mensagem para [Clayton](https://www.linkedin.com/in/clayton-pereira-72491648/).
