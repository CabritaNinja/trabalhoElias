# schemas/inflacao.py
# Define os modelos de request e response para os endpoints de inflação.

from pydantic import BaseModel
from typing import List
from app.schemas.produto import ItemConsumo


class CestaPersonalizadaRequest(BaseModel):
    itens: List[ItemConsumo]


class ResultadoInflacaoResponse(BaseModel):
    total_itens: int
    indice_inflacao_simulado: float
    descricao: str
