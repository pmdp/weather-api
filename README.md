# weather-api

Weather API using FastAPI as HTTP server framework

## Installation

Dependencies (with poetry): `pip3 install poetry && poetry install`

Optional export to requirements.txt:
```
 poetry export --without-hashes --format=requirements.txt > requirements.txt
 poetry export --without-hashes --format=requirements.txt --dev > requirements.dev.txt
```

## Usage

Local server execution: `OPENWEATHERMAP_API_KEY=XXX uvicorn app.main:app --reload`

Debug with IDE with `run-debug.py`

API REST sample: `http://127.0.0.1:8000/api/v1/weather/now?public_ip=85.53.20.2`

### Scripts:
```
./scripts/format-import.sh - Format files with isort and autoflake
./scripts/lint.sh - Lint the code
./scripts/test.sh - Test the app
./scripts/test-cov-html.sh  - Coverage test report
```

### Docker

Build: `docker build -t weather-api .`

Execution: `docker run -p 8000:8000 -e OPENWEATHERMAP_API_KEY=XXX weather-api`

## Configuration
Config variables from env:
- OPENWEATHER_API_KEY: openweathermap API key
- BACKEND_CORS_ORIGINS: CORS allowed origins
- API_V1_STR: API V1 prefix
- IP_V4_REGEX
- GEO_IP_DATABASE_PATH: Path to local file with GeoLite2 database

## Useful URLs

API docs: http://127.0.0.1:8000/docs

Redocs: http://127.0.0.1:8000/redoc

OpenAPI: http://127.0.0.1:8000/openapi.json

