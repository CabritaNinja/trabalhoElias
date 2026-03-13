from app.schemas.produto import Produto

PRODUTOS_MOCK: list[Produto] = [
    Produto(id=1, nome="Arroz Tipo 1",    categoria="Alimentação", unidade="kg"),
    Produto(id=2, nome="Feijão Carioca",  categoria="Alimentação", unidade="kg"),
    Produto(id=3, nome="Óleo de Soja",    categoria="Alimentação", unidade="litro"),
]

