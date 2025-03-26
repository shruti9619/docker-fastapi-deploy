FROM python:3.9-slim
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-dev
COPY src/ ./src/
COPY src/docker_fastapi_deploy/model.pkl .
CMD ["poetry", "run", "uvicorn", "src.docker_fastapi_deploy.main:app", "--host", "0.0.0.0", "--port", "80"]