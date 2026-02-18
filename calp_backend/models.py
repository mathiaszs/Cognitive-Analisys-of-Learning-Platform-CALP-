from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
# from sqlalchemy_utils.types import ChoiceType

# para rodar o banco de dados, digite no terminal os seguintes comandos:
# alembic revision --autogenerate -m "init"
# alembic upgrade head

# Cria a conexão do banco
db = create_engine("sqlite:///../banco.db")

# Cria a base do banco
Base = declarative_base()

# Criar as classes/tabelas do banco
class Usuario(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("name", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("activity", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


class Pedido(Base):
    __tablename__ = "pedidos"

    #    STATUS_PEDIDOS = (
    #        ("PENDENTE", "PENDENTE"),
    #        ("CANCELADO", "CANCELADO"),
    #        ("FINALIZADO", "FINALIZADO")
    #    )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String)
    user = Column("user", ForeignKey("users.id"))
    preco = Column("preco", Float)

    def __init__(self, status, user, preco=0):
        self.status = status
        self.user = user
        self.preco = preco
        

class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preo_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido


# Executa a criação dos metadados do banco (cria efetivamente o banco)
