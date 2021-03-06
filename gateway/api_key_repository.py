from gateway.models import ApiKey
from datetime import datetime
from app.cache import cache


@cache.memoize(0)
def get_active_by_hashed_key(hashed_key):
    return (
        ApiKey.query.filter_by(hashed_key=hashed_key, active=True)
        .filter(ApiKey.expires_at > datetime.now())
        .first()
    )
