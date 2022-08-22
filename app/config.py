from pydantic import BaseSettings


class Settings(BaseSettings):
    OPENWEATHERMAP_API_KEY: str = "XXXXXXXXXXXXXXXXXXXXXX"
    OPENWEATHER_CURRENT_API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'
    API_V1_STR = '/api/v1'
    BACKEND_CORS_ORIGINS: list = ['http://127.0.0.1:8000', 'http://localhost:8000']
    GEO_IP_DATABASE_PATH = './GeoLite2-City.mmdb'
    IP_V4_REGEX = '^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'


settings = Settings()
