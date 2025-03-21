# Docker na Prática

"""
O Docker é uma plataforma que permite criar, distribuir e executar aplicações em containers,
garantindo um ambiente isolado e portátil para execução do software.
"""

# Instalação do Docker
# Acesse a documentação oficial para instalar o Docker no seu sistema operacional:
# https://docs.docker.com/get-docker/

# Criando um Container para uma Aplicação
# O Dockerfile contém instruções para criar um container com todas as dependências necessárias.

DOCKERFILE_EXEMPLO = """
FROM node:16
WORKDIR /usr/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "run", "dev"]
"""

# Docker Compose
# Facilita a execução de múltiplos containers.

DOCKER_COMPOSE_EXEMPLO = """
version: '3'

services:
  web:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - db
    environment:
      DATABASE_URL: "postgres://postgres:postgres@db:5432/mydatabase"
    networks:
      - app-network

  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: "postgres"
    ports:
      - "5432:5432"
    networks:
      - app-network

networks:
  app-network:
    driver: bridge
"""

# Comandos Úteis do Docker
COMANDOS_UTEIS = {
    "Construir a imagem": "docker build -t minha-app .",
    "Rodar o container": "docker run -p 3000:3000 minha-app",
    "Ver containers ativos": "docker ps",
    "Parar um container": "docker stop <container_id>",
    "Remover um container": "docker rm <container_id>",
    "Executar comando dentro do container": "docker exec -it <container_id> bash",
    "Subir containers com Docker Compose": "docker-compose up -d",
    "Parar os containers do Compose": "docker-compose down",
}

# Conclusão
"""
O Docker permite criar ambientes consistentes e escaláveis para aplicações, eliminando problemas
 de configuração entre diferentes máquinas. Com Docker Compose, podemos gerenciar múltiplos
 serviços facilmente.
"""
