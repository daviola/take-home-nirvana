# Nirvana Take-Home project

## Setting up the environment:

> Make sure you have python 3.11 or higher installed

> Make sure you have docker 20.10.17 or higher installed


Create the environment
```
python3 -m venv venv
```
Activate the environment:
```
source venv/bin/activate
```
Install de dependencies:
```
pip install -r requirements.txt
```

Build and run the containers
```console
docker-compose up
```

## Accessing the APIs
You can see the documentation of the main API accessing `http://localhost:8000/docs` or `http://localhost:8000/redoc`
You can see the documentation of the external APIs acessing `http://localhost:81/docs` or `http://localhost:81/redoc` ( this is for the first API, the other two, you can find on ports 82 and 83)

To run the main API, you can go to your browser and open: 
```
http://localhost:8000/?member_id=123&strategy=mean
```

You can choose between these strategies:
1. `mean`
1. `fmean`
1. `geometric_mean`
1. `harmonic_mean`
1. `median`
1. `median_high`
1. `median_low`
1. `min`
1. `max`


## Running the tests

> To run the tests you must have the containers running

Run on the project root folder:
```
pytest tests/*.py
```
or run this to see the coverage:
```
pytest tests/*.py --cov-report term-missing --cov .
```

## Implementation Details
I've built these APIs using [fastapi](https://fastapi.tiangolo.com/), to take advantage of its asynchronous nature, although 
is my first experience with this framework

My first approach was, to have it all running in a single same API, that would call itself in different routes to emulate 
multiple APIs, 
but I thought it would be closer to reality if we had multiple APIs running in different containers, 
and to achieve that, I used [Docker and docker compose](https://docs.docker.com/compose/), so it's possible to run all the APIs 
with a single command.


### Final considerations
I've had some problems with testing, for some reason, [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) 
is not considering async tasks on the coverage, 
this is something I would take a closer look at in a long-term project

I did not give much attention to the swagger docs, because of the time frame, but this is another thing that can be improved.