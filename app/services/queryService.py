from typing import List, Dict, Union


class QueryService:
    async def get_query() -> List[Dict[str, Union[int, str]]]:
        return [{"item_id": 1, "q": "test"}]
