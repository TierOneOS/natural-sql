from typing import Any

from langchain.agents import create_sql_agent, AgentType
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.llms.openai import OpenAI
from langchain.utilities import SQLDatabase
from langchain.chat_models import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain

from api.const import (
    LLM_MODEL,
    PG_URI
)


class QueryService:
    async def get_query(self, question, pg_uri = PG_URI) -> Any:
        llm = OpenAI(temperature=0, model_name=LLM_MODEL)

        db = SQLDatabase.from_uri(pg_uri)
        db_chain = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=True, top_k=3)

        prompt = """ 
           Given an input question, first create a syntactically correct postgresql query to run,  
            then look at the results of the query and return the answer.  
            The question: {question}
           """

        # use db_chain.run(question) instead if you don't have a prompt
        return db_chain.run(prompt.format(question=question))

    async def get_agent_query(self, question, pg_uri=PG_URI) -> Any:
        gpt = OpenAI(temperature=0, model_name=LLM_MODEL)
        db = SQLDatabase.from_uri(pg_uri)
        toolkit = SQLDatabaseToolkit(db=db, llm=gpt)

        agent_executor = create_sql_agent(
            llm=gpt,
            toolkit=toolkit,
            verbose=True,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        )

        # use db_chain.run(question) instead if you don't have a prompt
        return agent_executor.run(question)