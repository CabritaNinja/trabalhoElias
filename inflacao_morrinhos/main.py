from fastapi import FastAPI
from app.rotas import produtos, inflacao

app = FastAPI(
    title="API Inflação Morrinhos-GO",
    description="Monitora e calcula índices de inflação no município de Morrinhos-GO.",
    version="0.1.0",
)

app.include_router(produtos.router)
app.include_router(inflacao.router)


@app.get("/", tags=["Status"])
def health_check():
    return {"status": "ok", "mensagem": "API Inflação Morrinhos-GO está rodando!"}

