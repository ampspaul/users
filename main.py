from fastapi import FastAPI, Request,Response
from routes import router 
import time
import logging 
from starlette.middleware.base import BaseHTTPMiddleware
from database import init_db

app =FastAPI()
init_db()
logging.basicConfig(level=logging.INFO)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        body_bytes= await request.body()
        body_str = body_bytes.decode("utf-8")
        logging.info(f"Incomming request {request.method} {request.url.path} ")
        logging.info(f" request body {body_str}")
        
        async def receive():
            return {"type": "http.request","body": body_bytes}
        
        request._receive= receive
        response =await call_next(request)
        return response 
        
class AddHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response: Response = await call_next(request)
        response.headers["X-App-Version"] = "1.0.0"
        response.headers["X-Powered-By"] = "FastAPI"
        response.headers["Cache-Control"] = "no-store"
        return response
        
    
# app.add_middleware(LoggingMiddleware)
# app.add_middleware(AddHeadersMiddleware)

app.include_router(router)
    