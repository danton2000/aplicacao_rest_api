# Usando uma imagem base do Python
FROM python:3.8-slim

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando o arquivo de script para o container
COPY script.py /app

# Definindo o comando que será executado ao rodar o container
CMD ["python", "script.py"]