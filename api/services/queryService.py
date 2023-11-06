from typing import Any

from langchain.utilities import SQLDatabase
from langchain.chat_models import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain

from api.const import (
    LLM_MODEL,
    PG_URI
)


class QueryService:
    async def get_query(self, question) -> Any:
        llm = ChatOpenAI(temperature=0, model_name=LLM_MODEL)

        db = SQLDatabase.from_uri(PG_URI)
        db_chain = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=True, top_k=3)

        prompt = """ 
           Given an input question, first create a syntactically correct postgresql query to run,  
            then look at the results of the query and return the answer.  
            The question: {question}
           """

        # use db_chain.run(question) instead if you don't have a prompt
        return db_chain.run(prompt.format(question=question))