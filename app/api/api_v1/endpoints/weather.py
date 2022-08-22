import logging

from fastapi import APIRouter, Query
from fastapi_cache.decorator import cache

from app.config import settings
from app.utils.geoip import get_ip_info
from app.utils.httpx import do_request_to_current_weather

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/now")
@cache(expire=60)
async def weather_now_from_public_ip(public_ip: str = Query(min_length=4, max_length=50, regex=settings.IP_V4_REGEX)):
    logger.info(f"Requesting IP info from local database for IP: {public_ip}")
    ip_info = get_ip_info(public_ip)
    latitude = ip_info.location.latitude
    longitude = ip_info.location.longitude
    weather_data = await do_request_to_current_weather(
        {'lat': latitude, 'lon': longitude, 'appid': settings.OPENWEATHERMAP_API_KEY, 'units': 'metric'})
    return weather_data
