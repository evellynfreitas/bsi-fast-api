from fastapi import FastAPI, Path, HTTPException
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dados import Disciplina, QuadroHorarios, Requisito, Base, Enum

# Criar engine para conectar ao banco de dados
engine = create_engine('sqlite:///historico_escolar.db')

# Criar uma sessão
Session = sessionmaker(bind=engine)
session = Session()

app = FastAPI()

disciplinas = {
    0:{
        "codigo_disciplina": "TIN0222",
        "nome_disciplina": "Algoritmos e Programação",
        "ementa": "",
        "professor": "Jobson",
        "carga_horaria": 60,
        "periodo": 1,
    },
    1:{
        "codigo_disciplina": "TIN0235",
        "nome_disciplina": "Arquitetura de Computadores",
        "ementa": "",
        "professor": "Jefferson",
        "carga_horaria": 60,
        "periodo": 1,
    },
    2:{
        "codigo_disciplina": "TMT0043",
        "nome_disciplina": "Fundamentos de Cálculo",
        "ementa": "",
        "professor": "Amâncio",
        "carga_horaria": 60,
        "periodo": 1,
    },
    3:{
        "codigo_disciplina": "TIN0206",
        "nome_disciplina": "Fundamentos de Sistemas de Informação",
        "ementa": "",
        "professor": "Rodrigo",
        "carga_horaria": 60,
        "periodo": 1,
    },
    4:{
        "codigo_disciplina": "TIN0208",
        "nome_disciplina": "Interação Humano-Computador",
        "ementa": "",
        "professor": "Simone",
        "carga_horaria": 60,
        "periodo": 1,
    },
    5:{
        "codigo_disciplina": "TIN0207",
        "nome_disciplina": "Informação e Sociedade",
        "ementa": "",
        "professor": "Sean",
        "carga_horaria": 60,
        "periodo": 1,
    },
    6:{
        "codigo_disciplina": "TIN0207",
        "nome_disciplina": "Informação e Sociedade",
        "ementa": "",
        "professor": "Pimentel",
        "carga_horaria": 60,
        "periodo": 1,
    },
    7:{
        "codigo_disciplina": "TMT0044",
        "nome_disciplina": "Álgebra Linear",
        "ementa": "",
        "professor": "Jutuca",
        "carga_horaria": 60,
        "periodo": 2,
    },
}

@app.get("/")
def index():
    return {"Data": "Bem vindo a API"}
 
@app.get("/banco")
def banco():
    total_disciplinas = session.query(Disciplina).count()
    return {"Total_Disciplinas_Cadastradas": total_disciplinas}


# Disciplinas

@app.get("/get-todas-disciplinas")
def get_disciplinas():

    disciplinas = session.query(Disciplina).all()
    if disciplinas:
        dicionario_disciplinas = {}

        for disciplina in disciplinas:
            dicionario = {
            'nome': disciplina.nome_disciplina,
            'codigo': disciplina.codigo_disciplina,
            'periodo': disciplina.periodo_ideal,
            'carga_horaria': disciplina.carga_horaria,
            'eixo': disciplina.eixo,
            'tipo': 'Obrigatória' if disciplina.obrigatoria else 'Optativa',
            'ementa': disciplina.ementa
            }
            dicionario_disciplinas[disciplina.codigo_disciplina] = dicionario

        return dicionario_disciplinas
    else:
        return {"Data": f"Não encontramos nenhuma disciplina no banco."}

@app.get("/get-disciplina-by-codigo")
def get_disciplina(codigo: str):

    disciplina = session.query(Disciplina).filter(Disciplina.codigo_disciplina == codigo).first()

    if disciplina:
        dicionario_disciplina = {
            'nome': disciplina.nome_disciplina,
            'codigo': disciplina.codigo_disciplina,
            'periodo': disciplina.periodo_ideal,
            'carga_horaria': disciplina.carga_horaria,
            'eixo': disciplina.eixo,
            'tipo': 'Obrigatória' if disciplina.obrigatoria else 'Optativa',
            'ementa': disciplina.ementa
        }
        return dicionario_disciplina
    else:
        return {"Data": f"Não encontramos a disciplina do código {codigo}"}
  
@app.get("/get-disciplinas-por-periodo")
def get_disciplinas(periodo: int):

    disciplinas = session.query(Disciplina).filter(Disciplina.periodo_ideal == periodo).all()

    if disciplinas:
        dicionario_disciplinas = {}

        for disciplina in disciplinas:
            dicionario = {
            'nome': disciplina.nome_disciplina,
            'codigo': disciplina.codigo_disciplina,
            'periodo': disciplina.periodo_ideal,
            'carga_horaria': disciplina.carga_horaria,
            'eixo': disciplina.eixo,
            'tipo': 'Obrigatória' if disciplina.obrigatoria else 'Optativa',
            'ementa': disciplina.ementa
            }
            dicionario_disciplinas[disciplina.codigo_disciplina] = dicionario

        return dicionario_disciplinas
    else:
        return {"Data": f"Não encontramos nenhuma disciplina do {periodo}° período"}
    
@app.get("/get-disciplinas-obrigatorias")
def get_disciplinas():
    disciplinas = session.query(Disciplina).filter(Disciplina.obrigatoria).all()

    if disciplinas:
        dicionario_disciplinas = {}

        for disciplina in disciplinas:
            dicionario = {
            'nome': disciplina.nome_disciplina,
            'codigo': disciplina.codigo_disciplina,
            'periodo': disciplina.periodo_ideal,
            'carga_horaria': disciplina.carga_horaria,
            'eixo': disciplina.eixo,
            'tipo': 'Obrigatória' if disciplina.obrigatoria else 'Optativa',
            'ementa': disciplina.ementa
            }
            dicionario_disciplinas[disciplina.codigo_disciplina] = dicionario

        return dicionario_disciplinas
    else:
        return {"Data": f"Não encontramos nenhuma disciplina obrigatória cadastrada."}
    
@app.get("/get-disciplinas-optativas")
def get_disciplinas():
    disciplinas = session.query(Disciplina).filter(Disciplina.obrigatoria == False).all()

    if disciplinas:
        dicionario_disciplinas = {}

        for disciplina in disciplinas:
            dicionario = {
            'nome': disciplina.nome_disciplina,
            'codigo': disciplina.codigo_disciplina,
            'periodo': disciplina.periodo_ideal,
            'carga_horaria': disciplina.carga_horaria,
            'eixo': disciplina.eixo,
            'tipo': 'Obrigatória' if disciplina.obrigatoria else 'Optativa',
            'ementa': disciplina.ementa
            }
            dicionario_disciplinas[disciplina.codigo_disciplina] = dicionario

        return dicionario_disciplinas
    else:
        return {"Data": f"Não encontramos nenhuma disciplina optativa cadastrada."}
     
@app.get("/get-disciplinas-por-eixo")
def get_disciplinas(eixo: str):
    
    disciplinas = session.query(Disciplina).filter(Disciplina.eixo == eixo).all()

    if disciplinas:
        dicionario_disciplinas = {}

        for disciplina in disciplinas:
            dicionario = {
            'nome': disciplina.nome_disciplina,
            'codigo': disciplina.codigo_disciplina,
            'periodo': disciplina.periodo_ideal,
            'carga_horaria': disciplina.carga_horaria,
            'eixo': disciplina.eixo,
            'tipo': 'Obrigatória' if disciplina.obrigatoria else 'Optativa',
            'ementa': disciplina.ementa
            }
            dicionario_disciplinas[disciplina.codigo_disciplina] = dicionario

        return dicionario_disciplinas
    else:
        return {"Data": f"Não encontramos nenhuma disciplina do eixo {eixo}."}
        

# Requisitos

@app.get("/get-requistos-por-disciplina")
def get_requisitos(codigo_disciplina: str):

    disciplina = session.query(Disciplina).filter(Disciplina.codigo_disciplina == codigo_disciplina).first()
    
    if disciplina:
        requisitos = session.query(Requisito).filter(Requisito.codigo_disciplina == codigo_disciplina).all()
        if requisitos:
            dicionario_requisitos = {}
            for requisito in requisitos:
                disciplina_requisito = session.query(Disciplina).filter(Disciplina.codigo_disciplina == requisito.codigo_requisito).first()
                dicionario = {
                'nome': disciplina_requisito.nome_disciplina,
                'codigo': disciplina_requisito.codigo_disciplina,
                'periodo': disciplina_requisito.periodo_ideal,
                'carga_horaria': disciplina_requisito.carga_horaria,
                'eixo': disciplina_requisito.eixo,
                'tipo': 'Obrigatória' if disciplina_requisito.obrigatoria else 'Optativa',
                'ementa': disciplina_requisito.ementa
                }
                dicionario_requisitos[disciplina_requisito.codigo_disciplina] = dicionario

            return dicionario_requisitos
        else:
            return {"Data": f"Não encontramos nenhum requisito para essa disciplina."}
    else:
        return {"Data": f"Não encontramos nenhuma disciplina com o código {codigo_disciplina}."}

