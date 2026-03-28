import redis.asyncio as redis

redis_client = redis.Redis(
    host='localhost',
    port=6379, 
    decode_responses=True
)

# decode_responses=True → returns string instead of bytes
# Async Redis → matches FastAPI async flow