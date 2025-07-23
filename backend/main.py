from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="VitaminD Health Coach API",
    description="AI-powered personalized health recommendations",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/")
async def root():
    return {"message": "VitaminD Health Coach API is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}

# Example data models
class HealthRecord(BaseModel):
    user_id: str
    metric_type: str
    value: float
    unit: str
    timestamp: str

class Recommendation(BaseModel):
    user_id: str
    title: str
    description: str
    confidence: float
    citations: list[str] = []

# Example endpoints
@app.get("/api/recommendations/{user_id}")
async def get_recommendations(user_id: str):
    """Get personalized health recommendations for a user"""
    # This will be replaced with actual AI processing
    return {
        "user_id": user_id,
        "recommendations": [
            {
                "title": "Increase Vitamin D intake",
                "description": "Based on your latest blood work, consider increasing your Vitamin D3 supplementation to 2000 IU daily.",
                "confidence": 0.85,
                "citations": ["NIH Vitamin D Guidelines", "Journal of Clinical Endocrinology"]
            }
        ]
    }

@app.post("/api/health-records")
async def create_health_record(record: HealthRecord):
    """Create a new health record"""
    # This will be replaced with database operations
    return {"message": "Health record created", "record": record}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
