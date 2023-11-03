from typing import Union
from fastapi import APIRouter
from ..services.queryService import QueryService

router = APIRouter()

@router.get("/query")
async def get_query():
    return await QueryService.get_query()
