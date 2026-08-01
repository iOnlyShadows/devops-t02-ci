# devops-t02-ci

Exercício da disciplina de DevOps: um pipeline mínimo de **Integração Contínua (CI)** com Python, pytest e GitHub Actions.

## Estrutura

| Arquivo | Papel |
| --- | --- |
| `calculadora.py` | Código de negócio — calcula o total de uma compra com desconto |
| `test_calculadora.py` | Testes automatizados com pytest |
| `requirements.txt` | Dependências do projeto |
| `.gitignore` | Arquivos que não entram no controle de versão (`.venv/`, caches) |
| `.github/workflows/ci.yml` | Pipeline que roda os testes a cada push e pull request |

## Rodando localmente

O ambiente virtual reproduz na máquina local o mesmo ambiente que o runner do GitHub monta: Python 3.12 e as dependências do `requirements.txt`.

```bash
python -m venv .venv
.venv/Scripts/activate      # Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## O pipeline

O workflow em `.github/workflows/ci.yml` dispara a cada `push` e a cada `pull_request`. Ele sobe uma máquina Ubuntu limpa, instala o Python 3.12, instala as dependências e executa `pytest -q`.

Se algum teste falhar, o commit recebe um ✗ na aba **Actions** — o pipeline reprova a mudança antes de ela ser considerada pronta.
