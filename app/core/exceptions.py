from fastapi import FastApi, Request
from fastapi.responses import JSONResponse


def register_exception_handlers(app: FastApi):
    @app.exception_handler(Exception)
    async def unhandeled_exception_handler(request: Request, exc: Exception):
        return JSONResponse(status_code=500, content={"detail": str(exc)})
