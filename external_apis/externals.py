from fastapi import FastAPI, Request
import random

external_app = FastAPI()

response_choices = [
    dict(deductible=1000, stop_loss=10000, oop_max=5000),
    dict(deductible=1200, stop_loss=13000, oop_max=6000),
    dict(deductible=1000, stop_loss=10000, oop_max=6000),
]


@external_app.get("/")
async def root(request: Request, member_id: int):
    # Let's use the url and query params as a seed for random responses
    random.seed(str(request.url))
    return random.choice(response_choices)
