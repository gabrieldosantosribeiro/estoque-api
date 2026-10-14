# API de Estoque

API REST para controle de estoque de uma loja de roupas, desenvolvida com **FastAPI**.

> Projeto de estudo em andamento. Atualmente os dados ficam **em memória** (reiniciar o servidor reseta tudo).

## Tecnologias

- Python 3
- FastAPI
- Pydantic

## Como rodar

```bash
# clonar o repositório
git clone <url-do-seu-repositorio>
cd estoque-api

# criar e ativar o ambiente virtual
python -m venv .venv
source .venv/bin/activate      # Linux/Mac
# .venv\Scripts\activate       # Windows

# instalar as dependências
pip install -r requirements.txt

# iniciar o servidor
fastapi dev app/main.py
```

A API fica disponível em `http://127.0.0.1:8000`.
A documentação interativa (Swagger) fica em `http://127.0.0.1:8000/docs`.

## Rotas

| Método | Rota                  | Descrição                | Status de sucesso |
|--------|-----------------------|--------------------------|-------------------|
| GET    | `/`                   | Verifica se a API está no ar | 200           |
| GET    | `/produtos`           | Lista todos os produtos  | 200               |
| GET    | `/produtos/{id}`      | Busca um produto pelo id | 200               |
| POST   | `/produtos`           | Cria um produto          | 201               |
| PUT    | `/produtos/{id}`      | Atualiza um produto      | 200               |
| DELETE | `/produtos/{id}`      | Remove um produto        | 204               |

Erros possíveis: `404` (produto não encontrado) e `422` (dados inválidos).

## Exemplo de requisição

**POST** `/produtos`

```json
{
  "nome": "Moletom Cinza",
  "categoria": "moletom",
  "preco": 159.90,
  "quantidade": 12
}
```

**Resposta** (`201 Created`)

```json
{
  "id": 5,
  "nome": "Moletom Cinza",
  "categoria": "moletom",
  "preco": 159.9,
  "quantidade": 12
}
```

## Estrutura do projeto

```
estoque-api/
├── app/
│   ├── __init__.py
│   ├── main.py        # rotas da API
│   ├── schemas.py     # validação dos dados de entrada (Pydantic)
│   └── storage.py     # dados mockados em memória
├── tests/
├── requirements.txt
└── README.md
```

## Próximos passos

- [ ] Validações com `Field` (preço maior que zero, nome não vazio)
- [ ] Schema de resposta (`response_model`)
- [ ] Separar as rotas com `APIRouter`
- [ ] Transformar o storage em uma classe (POO)
- [ ] Entrada e saída de estoque, com bloqueio de quantidade negativa
- [ ] Filtros na listagem e alerta de estoque baixo
- [ ] Persistência em arquivo JSON
- [ ] Testes com `pytest`