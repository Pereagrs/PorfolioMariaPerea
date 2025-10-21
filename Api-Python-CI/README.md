# Proyecto de Python + FastAPI con Azure DevOps CI/CD

Este proyecto es un ejemplo de cómo integrar **Python** y **FastAPI** con un **pipeline de Azure DevOps** para pruebas automáticas (CI/CD). Permite ejecutar tests automáticamente y generar reportes de cobertura de código cada vez que se sube código a la rama principal (`main`).

---

## Estructura del proyecto

```
mi-api-python-ci/
├── src/
│   └── main.py           # Código principal de la aplicación FastAPI
├── tests/
│   ├── test_main.py      # Tests automáticos con pytest
│   └── ...               # Puedes agregar más archivos de test
├── requirements.txt      # Dependencias del proyecto
├── azure-pipelines.yml   # Pipeline de Azure DevOps
└── README.md             # Este archivo
```

---

## Requisitos

- Python 3.10
- pip
- FastAPI
- pytest
- pytest-cov
- Azure DevOps account para CI/CD

Instala dependencias locales con:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Cómo funciona la aplicación

La aplicación está hecha con **FastAPI** y tiene endpoints de ejemplo:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola mundo"}

@app.get("/saludo/{nombre}")
def read_saludo(nombre: str):
    return {"saludo": f"Hola, {nombre}!"}
```

---

## Cómo ejecutar los tests localmente

1. Activar el entorno virtual (si lo tienes):

```bash
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate     # Windows
```

2. Ejecutar pytest:

```bash
pytest --cov=src --cov-report=term
```

Esto ejecuta todos los tests dentro de la carpeta `tests/` y muestra la cobertura de código.

---

## Pipeline en Azure DevOps

Cada vez que haces push a `main`, Azure DevOps ejecuta:

1. Configura Python 3.10.
2. Instala dependencias (`pip install -r requirements.txt`).
3. Ejecuta tests (`pytest`) y genera reportes:
   - `results.xml` → resultados de tests
   - `coverage.xml` → cobertura de código
4. Publica los resultados en Azure DevOps.
5. Publica los artefactos generados.

El pipeline está definido en `azure-pipelines.yml`.

---

## Añadir nuevos tests

1. Crear un archivo dentro de `tests/`, por ejemplo `tests/test_nuevo.py`.
2. Crear funciones que empiecen por `test_`:

```python
def test_ejemplo():
    assert 2 + 2 == 4
```

3. Subir los cambios a GitHub → Azure DevOps ejecutará los nuevos tests automáticamente.

---

## Beneficios de este proyecto

- Demuestra integración **Python + FastAPI + Azure DevOps CI/CD**.
- Permite **automatizar tests y cobertura de código**.
- Ideal para **portfolio profesional** mostrando habilidades de DevOps y Python.
- Fácil de extender con nuevos endpoints y tests.

---

## Contacto

Cualquier duda o sugerencia: www.linkedin.com/in/maría-pereagrs