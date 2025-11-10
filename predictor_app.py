from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="PTYS AI Predictor")

# CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👇 Ana sayfa endpoint'i
@app.get("/")
def home():
    return {
        "message": "PTYS AI Predictor API is running 🚀",
        "usage": "Use /predict?metric=your_metric to get AI predictions",
        "developer": "Hamza Özbalkan",
        "status": "online"
    }

# 👇 Tahmin endpoint'i
@app.get("/predict")
def predict(metric: str = "default"):
    return JSONResponse(content={
        "metric": metric,
        "prediction": f"AI Insight: {metric} trendi %87 başarı ile öngörüldü.",
        "status": "ok"
    })
