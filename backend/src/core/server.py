from fastapi import FastAPI, status, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from src.api.endpoints import routers

# origins = [
#     "http://localhost:3000",  # Адрес вашего React приложения
#     "http://127.0.0.1:3000"
# ]


class Server:

    def __init__(self, debug: bool = True) -> None:

        self._app = FastAPI(debug=debug)
        self.__init_routers()
        self.__init_events()
        # self._app.add_middleware(
        #     CORSMiddleware,
        #     allow_origins=origins,
        #     allow_credentials=True,
        #     allow_methods=["*"],
        #     allow_headers=["*"],
        # )

    @property
    def app(self):
        return self._app

    @classmethod
    async def __validation_error_handler(
        cls, req: Request, exc: RequestValidationError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder({"detail": exc.errors()}),
        )

    def __init_routers(self):
        for router in routers:
            self._app.include_router(router)

    def __init_events(self):
        self._app.exception_handler(RequestValidationError)(
            self.__validation_error_handler
        )
