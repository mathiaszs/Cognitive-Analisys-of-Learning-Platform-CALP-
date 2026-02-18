from fastapi import APIRouter, Depends
from models import Usuario
from dependencies import pegar_sessao

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
    """
    Essa é a rota padrão para autenticação
    """
    return {"mensagem": "Só kapa"}

# Rota do tipo post, para criar usuário
@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str, session = Depends(pegar_sessao)):
    
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        # já existe um usuario
        return {"mensagem": "já existe"}
    else:
        novo_usuario = Usuario(nome, email, senha, True)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": "usuário cadastrado com sucesso"}


