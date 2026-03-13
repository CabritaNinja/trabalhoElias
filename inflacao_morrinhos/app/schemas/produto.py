# schemas/produto.py
# Define os modelos de dados (contratos) relacionados a Produto.

from pydantic import BaseModel


class Produto(BaseModel):
    id: int
    nome: str
    categoria: str
    unidade: str


class ItemConsumo(BaseModel):
    produto_id: int
    quantidade: float
