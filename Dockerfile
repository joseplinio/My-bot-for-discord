# Usansdo a imagem do python
FROM python:3.12.8 

# Diretoria para o conteiner
WORKDIR /app

# Copia o requirements.txt para o conteiner
COPY requirements.txt .

# Instalar as dependencias
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Executando o bot pela comando
CMD [ "python", "-m", "src.main" ]
