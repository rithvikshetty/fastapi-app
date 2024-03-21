import uvicorn
from endpoints import router
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]
app = FastAPI(
    docs_url=None, # Disable docs (Swagger UI)
    redoc_url=None, # Disable redoc
    middleware=middleware
)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=80)