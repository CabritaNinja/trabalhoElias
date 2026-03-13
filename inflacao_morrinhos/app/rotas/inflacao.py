from fastapi import APIRouter, HTTPException
from app.schemas.inflacao import CestaPersonalizadaRequest, ResultadoInflacaoResponse
from app.data.mock_produtos import PRODUTOS_MOCK

router = APIRouter(prefix="/inflacao", tags=["Inflação"])


@router.post("/personalizada", response_model=ResultadoInflacaoResponse)
def calcular_inflacao_personalizada(cesta: CestaPersonalizadaRequest):
    ids_validos = {p.id for p in PRODUTOS_MOCK}

    for item in cesta.itens:
        if item.produto_id not in ids_validos:
            raise HTTPException(status_code=404, detail=f"Produto id={item.produto_id} não encontrado.")

    total_itens = len(cesta.itens)
    total_quantidade = sum(item.quantidade for item in cesta.itens)
    indice = round(min(total_quantidade * 0.15, 100.0), 2)

    return ResultadoInflacaoResponse(
        total_itens=total_itens,
        indice_inflacao_simulado=indice,
        descricao=f"Índice simulado: {indice}% para {total_itens} item(s) na cesta.",
    )

