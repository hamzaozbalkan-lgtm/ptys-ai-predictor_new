from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="PTYS AI Predictor")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/predict")
def predict(metric: str = "default"):
    return JSONResponse(content={
        "metric": metric,
        "prediction": f"AI Insight: {metric} trendi %87 başarı ile öngörüldü.",
        "status": "ok"
    })
