from fastapi import FastAPI, HTTPException
from main_api.util import fetch_async_from_multiple_urls
import aiohttp
from statistics import (
    mean,
    fmean,
    geometric_mean,
    harmonic_mean,
    median_high,
    median_low,
    median,
)

EXTERNAL_APIS = [
    "http://external-api1:8000/",
    "http://external-api2:8000/",
    "http://external-api3:8000/",
]

STRATEGIES = {
    "mean": mean,
    "fmean": fmean,
    "geometric_mean": geometric_mean,
    "harmonic_mean": harmonic_mean,
    "median": median,
    "median_high": median_high,
    "median_low": median_low,
    "min": min,
    "max": max,
}

app = FastAPI()


@app.get("/")
async def root(member_id: int, strategy: str):
    # request from the EXTERNAL_APIS list and return the result with the strategy applied
    if strategy not in STRATEGIES:
        raise HTTPException(status_code=400, detail="Invalid strategy")
    async with aiohttp.ClientSession() as session:
        urls = [f"{x}?member_id={member_id}" for x in EXTERNAL_APIS]
        responses = await fetch_async_from_multiple_urls(session, urls)
        results = dict(deductible=[], stop_loss=[], oop_max=[])
        for response in responses:
            [results[k].append(response.get(k, 0)) for k in results]
        return {k: STRATEGIES[strategy](v) for k, v in results.items()}
