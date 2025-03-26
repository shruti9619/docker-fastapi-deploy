FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml poetry.lock README.md ./
COPY src/ ./src/
RUN pip install poetry && poetry install
COPY src/docker_fastapi_deploy/model.pkl .
CMD ["poetry", "run", "uvicorn", "src.docker_fastapi_deploy.main:app", "--host", "0.0.0.0", "--port", "80"]