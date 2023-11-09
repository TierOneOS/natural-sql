from fastapi import APIRouter
from ..services.queryService import QueryService

router = APIRouter()
query_service = QueryService()


@router.get("/query")
async def get_query(query:str, pg_uri):
    return await query_service.get_query(query, pg_uri)

@router.get("/agent")
async def get_agent_query(query:str, pg_uri):
    return await query_service.get_agent_query(query, pg_uri)