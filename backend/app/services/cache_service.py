import json
from app.core.redis_client import redis_client


class CacheService:

    async def get(self, key: str):
        data = await redis_client.get(key)

        if data:
            return json.loads(data)

        return None

    async def set(self, key: str, value: dict, ttl: int = 3600):
        await redis_client.set(
            key,
            json.dumps(value),
            ex=ttl
        )