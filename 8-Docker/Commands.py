"""
*Comandos Essenciais do Docker*

1. Parar um container em execução:
   docker stop idcontainer

2. Interromper forçadamente um container:
   docker kill idcontainer

3. Iniciar um container:
   docker start idcontainer

4. Pausar temporariamente um container:
   docker pause idcontainer

5. Retomar a execução de um container pausado:
   docker unpause idcontainer

6. Reiniciar um container:
   docker restart idcontainer

7. Listar containers criados (executando ou não):
   docker ps -a

8. Listar apenas os containers em execução:
   docker ps

9. Verificar logs de um container:
   docker logs idcontainer

10. Excluir um container (parado):
    docker rm idcontainer

11. Forçar a exclusão de um container em execução:
    docker rm -f idcontainer

12. Construir um container com base no docker-compose:
    docker-compose build

13. Listar todas as imagens existentes na máquina:
    docker images

14. Acessar o terminal interativo de um container:
    docker exec -it idcontainer bash

15. Acessar uma URL dentro do container:
    curl localhost:3000
    > Não é um comando específico do Docker, mas pode ajudar!

16. Criar uma imagem Docker no diretório atual:
    docker build -t nomedaimagem .

17. Criar e rodar um container a partir de uma imagem:
    docker run nomedaimagem
"""
