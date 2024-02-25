from fastapi import APIRouter

from src.routers.v1 import convert, auth

router = APIRouter()


router.include_router(convert.router,prefix='/model')
router.include_router(auth.router,prefix='/auth')