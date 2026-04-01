# Automation

## О проекте

Проект автоматизирует разработку Python-приложений через Makefile. Создает воспроизводимый процесс для окружения, зависимостей и качества кода.

Включает:
- Исходники с ошибками (типы, форматирование, зависимости)  
- Makefile для всех этапов
- Пакет для Test PyPI
- Полную документацию

## До автоматизации: ручной процесс

### 1. Создание виртуального окружения
```bash
python -m venv .venv
```

### 2. Активация окружения
```bash
# Windows
.venv\Scripts\activate
# Linux/macOS  
source .venv/bin/activate
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Запуск приложения
```bash
python src/app.py
```

### 5. Проверка типов
```bash
pip install mypy
mypy src/
```

### 6. Форматирование кода
```bash
pip install black
black src/
```

### 7. Проверка стиля
```bash
pip install flake8
flake8 src/
```

### 8. Проверка зависимостей
```bash
python scripts/check_requirements.py
```

### 9. Очистка временных файлов
```bash
rm -rf .venv
find . -type d -name "__pycache__" -exec rm -rf {} +
```

**Недостатки:**
- Длинные команды наизусть
- Разные команды для ОС  
- Риск глобального окружения
- Нет стандарта в команде
- Сложно воспроизвести

## После автоматизации: Makefile

Единый интерфейс команд вместо 9 шагов.

### Структура Makefile
```makefile
VENV := .venv
PYTHON := $(VENV)/Scripts/python
PIP := $(VENV)/Scripts/pip

$(VENV)/Scripts/python:
	python -m venv $(VENV)
	$(PIP) install --upgrade pip

install: $(VENV)/Scripts/python
	$(PIP) install -r requirements.txt

run: install
	$(PYTHON) src/app.py

check-deps: install
	$(PYTHON) scripts/check_requirements.py

typecheck: install
	$(PYTHON) -m mypy src/

format: install
	$(PYTHON) -m black src/

lint: install
	$(PYTHON) -m flake8 src/

check: typecheck check-deps lint
	@echo "All checks passed"

clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
```

### Доступные таргеты

| Таргет | Описание | Пример вывода |
|--------|----------|---------------|
| `make install` | Создание .venv + зависимости | Установка из requirements.txt |
| `make run` | Запуск приложения | HTTP статус приложения |
| `make check-deps` | Проверка импортов | "Missing: numpy" или "OK" |
| `make typecheck` | Mypy типы | Ошибки типов |
| `make format` | Black форматирование | Исправленный код |
| `make lint` | Flake8 стиль | Нарушения PEP8 |
| `make check` | Все проверки | "All checks passed" |
| `make clean` | Очистка | Удалены .venv, pycache |

## Пример использования

```bash
# Первый запуск
make install

# Разработка
make run
make check

# Исправления
make format

# Перезапуск чистый
make clean
make install
```

## Архитектура решения

**Stateless окружение**  
Makefile использует явные пути:
```makefile
PYTHON := $(VENV)/Scripts/python
```
Нет `source activate` — каждая команда в своем shell.

**Композиция таргетов**  
`check` запускает цепочку:
```
check → typecheck → install
     → check-deps → install  
     → lint → install
```

## Модули проекта

**src/app.py** — HTTP запросы через requests

**src/calc.py** — была ошибка:
```python
result: int = add(2, "3")  # → add(2, 3)
```

**src/service.py** — отсутствовали numpy, fastapi в requirements

**src/example.py** — плохое форматирование:
```python
def foo( x,y ): return x+y  # → def foo(x, y): return x + y
```

**scripts/check_requirements.py** — парсит импорты, сравнивает с requirements.txt

## Публикация на Test PyPI

```bash
pip install --index-url https://test.pypi.org/simple/ fossdev-tools
```

### CLI команды
```bash
fossdev check
fossdev typecheck  
fossdev lint
fossdev format
fossdev info
```

[Пакет на TestPyPI](https://test.pypi.org/project/fossdev-tools/)

## Воспроизводимость

```bash
make clean
git status --porcelain  # чисто

make check              # все проходит
```

## Требования
- Python 3.8+
- Make (Git Bash на Windows)
- Интернет

***
