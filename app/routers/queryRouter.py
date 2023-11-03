from typing import Union
from fastapi import APIRouter
from ..services.queryService import QueryService

router = APIRouter()
query_service = QueryService()


@router.get("/query")
async def get_query():
    return await query_service.get_query()
