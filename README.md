# bsi-fast-api

Este projeto consiste no desenvolvimento de uma API para o curso de Bacharelado em Sistemas de Informação (BSI) da UNIRIO. A API fornecerá informações detalhadas sobre a ementa curricular das disciplinas oferecidas no curso, incluindo conteúdo programático, carga horária e pré-requisitos. 

Além disso, a API também permitirá o acesso ao quadro de horários do período atual, facilitando a visualização das disciplinas oferecidas, seus horários, professores responsáveis e locais das aulas. 

O objetivo do projeto é centralizar e disponibilizar esses dados de forma organizada e acessível, facilitando a consulta tanto para alunos quanto para professores.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas: FastAPI, Uvicorn, SQLAlchemy, Flask

## Rodando localmente

Clone o projeto

```bash
git clone https://gitlab.com/evellynfreitas/bsi-fast-api.git
```

Entre no diretório do projeto

```bash
git cd bsi-fast-api
```

Crie um ambiente virtual
```bash
python -m venv venv
```

Ative o ambiente virtual
```bash
venv\scripts\activate
```

## Instalação

Instale as dependências utilizando o comando

```bash
  pip install -r requirements.txt
```  

## Teste e Execução

Para fazer o deploy desse projeto rode

```bash
uvicorn bsi_api:app --reload
```

## License
For open source projects, say how it is licensed.