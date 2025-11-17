from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routes.get_token import router as token_router
from routes.push_logs import router as logs_router
from routes.get_latest_versions import router as versions_router

app = FastAPI(title="DEUS API Server")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(token_router)
app.include_router(logs_router)
app.include_router(versions_router)

@app.get("/")
async def root():
    return {"message": "DEUS API Server is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
