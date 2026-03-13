# API Inflação Morrinhos-GO

API FastAPI para monitorar e calcular índices de inflação no município de Morrinhos-GO.

## Estrutura

```
inflacao_morrinhos/
├── main.py                   # Ponto de entrada da aplicação
├── requirements.txt          # Dependências Python
├── .gitignore
└── app/
    ├── data/
    │   └── mock_produtos.py  # Dados mockados em memória
    ├── rotas/
    │   ├── inflacao.py       # Endpoints /inflacao/
    │   └── produtos.py       # Endpoints /produtos/
    └── schemas/
        ├── inflacao.py       # Modelos de request/response de inflação
        └── produto.py        # Modelos de Produto e ItemConsumo
```

## Como rodar

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Acesse a documentação em: http://127.0.0.1:8000/docs
