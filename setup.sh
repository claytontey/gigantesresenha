mkdir -p ~/.streamlit/
echo "[general]
email = \"claytontey@gmail.comcom\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
