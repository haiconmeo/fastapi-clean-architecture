
from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware
from .router import api_router
from app.config import settings
app = FastAPI(
    title="GPT", openapi_url="/openapi.json",
    description="""
     """
)
if True:
    app.add_middleware(
        CORSMiddleware,
        # allow_origins=[str(origin)
        #                for origin in settings.BACKEND_CORS_ORIGINS],
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# if settings.ENV == 'development':
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


@app.get("/.well-known/live")
def live():
    return "OK"


app.include_router(api_router, prefix=settings.API_V1_STR)
