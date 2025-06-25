from groq import Groq
import os
# Singleton decorator for caching
def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    def destroy_instance():
        if cls in instances:
            del instances[cls]
    wrapper.destroy_instance = destroy_instance
    return wrapper

@singleton
class agent:
    def __init__(self):
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)
    # Function to detect SQL dialect
    def detect_sql_dialect(self, sql_query: str) -> str:
        prompt = f"""
        You are a SQL expert. Analyze the following SQL query and identify the most likely SQL dialect used.
        The options are: MySQL, PostgreSQL, SQL Server, Oracle, BigQuery, SQLite.

        SQL Query:
        {sql_query}

        Respond with only the name of the dialect.
        """

        response = self.client.chat.completions.create(
            model="llama3-8b-8192",  # or "mixtral-8x7b-32768"
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        return response.choices[0].message.content.strip()
    

    def detect_sql_type(self, sql_query: str) -> str:
        prompt = f"""
        You are an expert SQL analyst. Classify the following SQL query into one of these categories:

        - DDL (Data Definition Language) – e.g., CREATE, ALTER, DROP
        - DML (Data Manipulation Language) – e.g., SELECT, INSERT, UPDATE, DELETE
        - DCL (Data Control Language) – e.g., GRANT, REVOKE
        - TCL (Transaction Control Language) – e.g., COMMIT, ROLLBACK

        SQL Query:
        {sql_query}

        Respond with only one of the following: DDL, DML, DCL, or TCL.
        """

        response = self.client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        return response.choices[0].message.content.strip()

