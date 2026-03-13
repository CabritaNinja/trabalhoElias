from fastapi import APIRouter
from typing import List
from app.schemas.produto import Produto
from app.data.mock_produtos import PRODUTOS_MOCK

router = APIRouter(prefix="/produtos", tags=["Produtos"])


@router.get("/", response_model=List[Produto])
def listar_produtos():
    return PRODUTOS_MOCK

