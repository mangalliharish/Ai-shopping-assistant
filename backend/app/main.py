from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import search

app = FastAPI()

# 🔥 CORS (VERY IMPORTANT for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include routes
app.include_router(search.router)

# ✅ Home route
@app.get("/")
def home():
    return {"message": "AI Shopping Assistant Running 🚀"}