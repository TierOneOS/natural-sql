from fastapi import APIRouter
from ..services.queryService import QueryService

router = APIRouter()
query_service = QueryService()


@router.get("/query")
async def get_query(query:str):
    return await query_service.get_query(query)
