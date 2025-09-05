FROM python:3.12-slim

WORKDIR /app
ENV PIP_DISABLE_PIP_VERSION_CHECK=on PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir uv
COPY pyproject.toml /app/pyproject.toml
RUN uv sync --all-extras

COPY . /app
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
