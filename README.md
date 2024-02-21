# Coke Store Bot
## Helps to search product information, prices, discounts from the inventory

This is a project using Google Palm and Langchain technologies to build a system that can talk to a MySQL database. Imagine a store called Coke Store that sells beverages and keeps track of inventory and discounts in this database. The system will understand questions asked in natural language by users and convert them into SQL queries, which it will then run on the MySQL database to fetch answers. For example, a store manager might ask things like:

- "How much does a case of Sprite 300ml CAN cost?"
- "What promotions are available for Coca Cola 600 ml with discounts greater than 10%?"
  
The system will be smart enough to understand these questions (few shot learning) and fetch accurate information from the database.

![](atliq_tees.png)


## Project Highlights

- Coke Store is a beverage store that sells Coca-Cola, Sprite, Fanta and Kinley Water etc brands 
- Their inventory, promotions and discounts data is stored in a MySQL database
- We will build an LLM based question and answer system that will use following,
  - Google Palm LLM
  - Hugging face embeddings
  - Streamlit for UI
  - Langchain framework
  - Chromadb as a vector store
  - Few shot learning
- In the UI, store manager will ask questions in a natural language and it will produce the answers
