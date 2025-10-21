# Mi API FastAPI
Este proyecto es una API simple hecha con FastAPI, con tests incluidos y cobertura de código.
Cómo ejecutar
1. Activar entorno virtual:
    python -m venv .venv
    .venv\Scripts\activate
2. Instalar dependencias:
    pip install -r requirements.txt
3. Ejecutar la API:
    uvicorn src.main:app --reload
4. Ejecutar tests:
    python -m pytest --cov=src --cov-report=term
Estructura del proyecto
mi-api-python-ci/
├─ .venv/
├─ src/
│  ├─ __init__.py
│  └─ main.py
├─ tests/
│  └─ test_main.py
├─ requirements.txt
├─ .gitignore
└─ README.md
Notas
.venv/ está ignorado en Git gracias a .gitignore.
La cobertura se puede ver en la terminal o generando un reporte HTML.
