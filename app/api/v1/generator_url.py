from hashids import Hashids
from app.schemas.setting import settings

hashids = Hashids(salt=settings.salt, min_length=6)

def generate_short_url(id):
    short_url = hashids.encode(id)
    return short_url

def decode_url(short_url):
    decoded = hashids.decode(short_url)
    if decoded:
        bd_id = decoded[0]
        return bd_id
    return None
