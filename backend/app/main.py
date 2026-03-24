# import asyncio

# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api import auth_routes, property_routes, agent_routes, user_routes, chat_routes
from app.utils.logger import logger
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles



app = FastAPI(
    title="Estate Scout API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# ✅ Routes
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(property_routes.router, prefix="/properties", tags=["Properties"])
app.include_router(agent_routes.router, prefix="/agent", tags=["Agent"])
app.include_router(user_routes.router, prefix="/user", tags=["User"])
app.include_router(chat_routes.router, prefix="/chat", tags=["Chat"])



# ✅ Startup Event (important for DB / logs)
@app.on_event("startup")
async def startup_event():
    logger.info("🚀 Server started successfully")


# ✅ Shutdown Event
@app.on_event("shutdown")
async def shutdown_event():
    logger.info("🛑 Server stopped")


# ✅ Global Exception Handler (IMPROVED)
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Error occurred: {str(exc)}")

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "details": str(exc)   # production में हटा सकते हो
        }
    )

@app.get("/test")
def test():
    print("✅ test route hit")
    return {"msg": "working"}


# ✅ Health Check Route (VERY IMPORTANT)
@app.get("/")
def home():
    return {"status": "OK", "message": "Estate Scout Backend Running"}


# ✅ Optional: Health route (DevOps useful)
@app.get("/health")
def health():
    return {"status": "healthy"}