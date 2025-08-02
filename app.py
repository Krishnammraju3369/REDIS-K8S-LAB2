from fastapi import FastAPI
import redis
import os

app = FastAPI()

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)

r = redis.Redis(
    host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True
)


@app.get("/set")
def set_key(key: str, value: str):
    r.set(key, value)
    return {"message": f"Set {key} = {value}"}


@app.get("/get")
def get_key(key: str):
    value = r.get(key)
    return {"value": value}
