# Execultar Spark no Docker

### Descrição
Este repositório contem as configurações necessárias para execultar arquivos pyspark dentro de um container Docker.

### Estrutura do Repositório
Este repositório contém os arquivos para utilizar o spark docker no ambiente local

### Configuração do Ambiente
Em primeiro lugar você deve baixar e instalar os programas necessários para rodar esse código, estou utilizando o Windows para programar:

* Python: https://www.python.org/downloads/
* Visua Studio Code: https://code.visualstudio.com/download
* Docker: https://www.docker.com/products/docker-desktop/

### Como Executar
Para execultar o docker container com o spark, siga esses passos:

1. Baixe o repositório no seu computador e coloque o arquivo em alguma pasta
2. Abra a pasta no VS Code
3. Abra o terminal para execultar alguns comandos
4. Inicie os contêineres:
    ```bash
    docker-compose up
    ```
    
2. Para acessar o contêiner do Spark:
    ```bash
    docker exec -it nome-do-container /bin/bash
    ```

### Uso do Jupyter Notebook
1. Após iniciar os contêineres, acesse o Jupyter Notebook no navegador:
    ```
    http://localhost:8888
    ```
2. Utilize os notebooks na pasta `notebooks` para executar scripts PySpark.

### Scripts e Códigos de Exemplo
- Exemplos de scripts PySpark podem ser encontrados na pasta `scripts`.
- Para executar um script PySpark:
    ```bash
    spark-submit scripts/exemplo.py
    ```

### Contribuição
Para contribuir com este projeto, por favor, siga os passos abaixo:
1. Fork o repositório
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Faça um push para a branch (`git push origin feature/nova-feature`)
5. Crie um novo Pull Request

### Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE.md para mais detalhes.

