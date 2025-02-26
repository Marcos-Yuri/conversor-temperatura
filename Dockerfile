# Escolhe uma imagem base do Python
FROM python:3.9-slim

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . /app

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que a aplicação vai usar (flask por padrão usa a porta 5000)
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
