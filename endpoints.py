import fastapi
from fastapi import Response, status


router = fastapi.APIRouter()

@router.get("/", tags=['health_check'])
async def health_check():
    return Response(status_code=status.HTTP_200_OK)