from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def message():
    return {'msg': 'Acesse /docs para utilizar as APIs no Swagger'}