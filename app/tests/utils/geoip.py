from app.utils.geoip import get_ip_info


def test_get_geoip() -> None:
    response = get_ip_info('3.3.3.3')
    assert response
    assert response.status_code == '200'
