# import asyncio

# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api import auth_routes, property_routes, agent_routes
from app.utils.logger import logger

app = FastAPI(
    title="Estate Scout API",
    version="1.0.0"
)

# ✅ Routes
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(property_routes.router, prefix="/properties", tags=["Properties"])
app.include_router(agent_routes.router, prefix="/agent", tags=["Agent"])



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