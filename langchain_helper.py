from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX,_mysql_prompt
from langchain.prompts.prompt import PromptTemplate

from few_shots import few_shots
import os
# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st



def get_few_shot_db_chain():
    db_user=st.secrets["DB_USER"]
    db_password=st.secrets["DB_PASSWORD"]
    db_host=st.secrets["DB_HOST"]
    db_name=st.secrets["DB_NAME"]
    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
                              sample_rows_in_table_info=3)
    
    llm=GooglePalm(google_api_key=st.secrets["GOOGLE_API_KEY"],temperature=0.1)
    embeddings=HuggingFaceEmbeddings(model_name=st.secrets["MODEL_NAME"])

    to_vectorize=[" ".join(example.values()) for example in few_shots]

    vectorstore=Chroma.from_texts(to_vectorize,embeddings,metadatas=few_shots)
    example_selector=SemanticSimilarityExampleSelector(
        vectorstore=vectorstore,
        k=2,
    )

    mysql_prompt = """You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question.Use joins for query columns. Wrap each column name in backticks (`) to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist or have spelling mistakes. Also, pay attention to which column is in which table.
    Pay attention to cases and bottles, if the question involves "bottle" then do not use price per case.
    
    Use the following format:
    
    Question: Question here
    SQLQuery: Query to run with no pre-amble
    SQLResult: Result of the SQLQuery
    Answer: Final answer here
    
    No pre-amble.
    """

    example_prompt=PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult","Answer",],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

    few_shot_prompt=FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=['input','table_info','top_k'],

    )
    chain=SQLDatabaseChain.from_llm(llm,db,verbose=True,prompt=few_shot_prompt)
    return chain



