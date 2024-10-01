from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import enum

# Configurações da base de dados
DATABASE_URL = "sqlite:///historico_escolar.db"  # Use SQLite para simplicidade
Base = declarative_base()

# Definindo os Eixos a partir do Enum
class Eixo(enum.Enum):
    fundamentos_matematica = "Fundamentos da Matemática"
    gestao_empreendedorismo = "Gestão de Sistemas e Tecnologias da Informação, e Empreendedorismo e Inovação"
    programacao_algoritmos = "Programação e Algoritmos"
    engenharia_software = "Engenharia de Software"
    engenharia_dados = "Engenharia de Dados e Informação"
    infraestrutura = "Infraestrutura em Sistemas de Informação"
    sistemas_informacao = "Sistemas de Informação"
    desenvolvimento_pessoal = "Desenvolvimento Pessoal e Profissional"
    formacao_complementar = "Formação Complementar"
    atividades_extensao = "Atividades de Extensão"
    atividades_complementares = "Atividades Complementares"
    trabalho_conclusao = "Trabalho de Conclusão de Curso"

# Definindo a tabela Disciplina
class Disciplina(Base):
    __tablename__ = 'disciplina'

    codigo_disciplina = Column(String(7), primary_key=True)  # Identificador único da disciplina (TIN0206)
    nome_disciplina = Column(String(255), nullable=False)  # Nome completo da disciplina
    periodo_ideal = Column(Integer)  # Período ideal, exemplo: 1, 2, 3
    carga_horaria = Column(Integer)  # Carga horária em horas
    ementa = Column(String(500))  # Ementa da matéria, se disponível
    obrigatoria = Column(Boolean, default=True) # Se a matéria é obrigatória ou optativa
    eixo = Column(Enum(Eixo), nullable=False)

# Definindo a tabela Requisito
class Requisito(Base):
    __tablename__ = 'requisito'

    codigo_disciplina = Column(String(7), ForeignKey('disciplina.codigo_disciplina'), primary_key=True)  # Identificador da disciplina que possui requisitos
    codigo_requisito = Column(String(7), ForeignKey('disciplina.codigo_disciplina'), primary_key=True)  # Identificador do requisito (disciplina que é um requisito)

    disciplina = relationship("Disciplina", foreign_keys=[codigo_disciplina])  # Relacionamento com Disciplina
    requisito_disciplina = relationship("Disciplina", foreign_keys=[codigo_requisito])  # Relacionamento com Disciplina

class QuadroHorarios(Base):
    __tablename__ = 'quadro-horarios-2024'

    id_disciplina = Column(Integer, autoincrement=True, primary_key=True)
    codigo_disciplina = Column(String(7), ForeignKey('disciplina.codigo_disciplina'))  # Identificador da disciplina que possui requisitos
    professor = Column(String(255))
    dias = Column(String(255))
    horario = Column(String(255))
    sala = Column(String(255))

    disciplina = relationship("Disciplina", foreign_keys=[codigo_disciplina])  # Relacionamento com Disciplina


# Criando a engine e as tabelas
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Criando uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Inserindo dados de exemplo
def insert_data():
    #d = Disciplina(codigo_disciplina="", nome_disciplina="",periodo_ideal=,carga_horaria=,ementa="",obrigatoria=,eixo=)

    d1 = Disciplina(codigo_disciplina="TMT0043", nome_disciplina="Fundamentos de Cálculo",periodo_ideal=1,carga_horaria=60,ementa="Teoria dos Conjuntos, relações e funções. Função do 1º grau, função do 2º grau, função modular. Composição de funções e função inversa. Função exponencial e função logarítmica. Funções trigonométricas. Números inteiros e divisibilidade. Aplicações em Sistemas de Informação.",obrigatoria=True,eixo=Eixo.fundamentos_matematica)
    d2 = Disciplina(codigo_disciplina="TMT0044", nome_disciplina="Álgebra Linear",periodo_ideal=2,carga_horaria=60,ementa="Sistemas de equações lineares. Determinantes. Matrizes. Subespaços vetoriais Euclidianos. Transformações lineares. Autovalores e autovetores; diagonalização. Produto interno",obrigatoria=True,eixo=Eixo.fundamentos_matematica)
    d3 = Disciplina(codigo_disciplina="TMT0045", nome_disciplina="Cálculo Diferencial e Integral I",periodo_ideal=2,carga_horaria=60,ementa="Limites e continuidade. Definição de derivada. Aplicações das derivadas. Integral indefinida e aplicações. Integral Definida e aplicações. Teorema Fundamental do Cálculo e aplicações. Aplicações em Sistemas de Informação.",obrigatoria=True,eixo=Eixo.fundamentos_matematica)
    d4 = Disciplina(codigo_disciplina="HDI0142", nome_disciplina="Língua Brasileira de Sinais",periodo_ideal=6,carga_horaria=60,ementa="Língua Brasileira de Sinais e suas singularidades lingüísticas. Vivência da LIBRAS a partir do contato direto com um(a) professor(a) surdo(a). Implicações do Decreto n° 5.626 para a prática escolar e formação do(a) professor(a).",obrigatoria=False,eixo=Eixo.desenvolvimento_pessoal)

    session.add_all([d1, d2, d3, d4])
    session.commit()

    # Inserindo requisitos
    r1 = Requisito(codigo_disciplina=d2.codigo_disciplina, codigo_requisito=d1.codigo_disciplina)  # 
    r2 = Requisito(codigo_disciplina=d3.codigo_disciplina, codigo_requisito=d1.codigo_disciplina)  # 
    session.add_all([r1, r2])
    session.commit()

    # Inserindo as materias do quadro de horarios
    h1 = QuadroHorarios(codigo_disciplina="TMT0043", professor="Jutuca",dias="Segunda,Quarta",horario="14:00-16:00")
    h2 = QuadroHorarios(codigo_disciplina="TMT0043", professor="Amâncio",dias="Terça,Quinta",horario="14:00-16:00")

    session.add_all([h1,h2])
    session.commit()


# Consultando e imprimindo as disciplinas e seus requisitos
def print_disciplinas_e_requisitos():
    disciplinas = session.query(Disciplina).all()
    for disciplina in disciplinas:
        requisitos = session.query(Requisito).filter(Requisito.codigo_disciplina == disciplina.codigo_disciplina).all()
        if requisitos:
            requisitos_nomes = [
                session.query(Disciplina).filter(Disciplina.codigo_disciplina == r.codigo_requisito).first().nome_disciplina for r in requisitos
            ]
            print(f"{disciplina.nome_disciplina}: {', '.join(requisitos_nomes)}")
        else:
            print(f"{disciplina.nome_disciplina}: Nenhum requisito")

# Rodando as funções
#insert_data()  # Insere os dados apenas uma vez
#print_disciplinas_e_requisitos()  # Imprime as disciplinas e requisitos
