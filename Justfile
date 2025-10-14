# комментарии начинаются с #
# переменные
python := "python3"
venv := ".venv"

# рецепты
default:
    echo "Запусти 'just' с целью (например: just test)"

init:
    source {{venv}}/bin/activate

test:
    pytest --cov=src -vv -s

fmt:
	ruff format .
	ruff check . --fix

lint:
    mypy src
    flake8 src
    pyright src
run:
    PYTHONPATH=src uvicorn main:app --env-file .env

