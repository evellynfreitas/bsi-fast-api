from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dados import Disciplina, QuadroHorarios, Requisito, Base, Eixo


# Criar engine para conectar ao banco de dados
engine = create_engine('sqlite:///historico_escolar.db')  # Substitua pela URI correta do seu banco de dados

# Criar uma sessão
Session = sessionmaker(bind=engine)
session = Session()

disciplinas = session.query(Disciplina).all()

def imprime_disciplinas():
    # Imprimir os dados
    print("Disciplinas Cadastradas: ")
    for disciplina in disciplinas:
        print(f"{disciplina.nome_disciplina}")

def imprime_requisitos():
    print("Disciplinas e seus requisitos: ")

    for disciplina in disciplinas:
        requisitos = session.query(Requisito).filter(Requisito.codigo_disciplina == disciplina.codigo_disciplina).all()
        if requisitos:
            requisitos_nomes = [
                session.query(Disciplina).filter(Disciplina.codigo_disciplina == r.codigo_requisito).first().nome_disciplina for r in requisitos
            ]
            print(f"{disciplina.nome_disciplina}: {', '.join(requisitos_nomes)}")
        else:
            print(f"{disciplina.nome_disciplina}: Nenhum requisito")


imprime_disciplinas()
imprime_requisitos()
# Fechar sessão
session.close()