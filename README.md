# Emotion Correction with Shap API
This repository contains an API that detects toxic emotions in text.

## How to run

### Running locally (with reloading)
```commandline
git clone https://github.com/knmlprz/ShapEmotionsCorrectionAPI.git
cd ShapEmotionsCorrectionAPI
uvicorn src.main:app --reload
```

### Running from docker
```text
docker run -p 8000:8000 finloop/shap-emotions-correction-api:latest
```

## Documentation
All the documentation can be found here: [Documentation](https://knmlprz.github.io/ShapEmotionsCorrectionAPI/)
Unfortunately, you cannot make any requests from there, because the api is not 
hosted anywhere. To view interactive version of the docs go to [docs](localhost:8000/docs)  
endpoint.

## Benchmarking with locust
1. Run the api
2. Start locust
```commandline
locust -f benchmarks/benchmark_sentiment.py 
```
3. Go to http://0.0.0.0:8089