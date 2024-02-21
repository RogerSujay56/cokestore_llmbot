# Coke Store Bot
## Helps to search product information, prices, discounts from the inventory

This is a project using Google Palm and Langchain technologies to build a system that can talk to a MySQL database. Imagine a store called Coke Store that sells beverages and keeps track of inventory and discounts in this database. The system will understand questions asked in natural language by users and convert them into SQL queries, which it will then run on the MySQL database to fetch answers. For example, a store manager might ask things like:

- "How much does a case of Sprite 300ml CAN cost?"
- "What promotions are available for Coca Cola 600 ml with discounts greater than 10%?"
  
The system will be smart enough to understand these questions (few shot learning) and fetch accurate information from the database.

## Results
<div style="display: flex; justify-content: space-around;">
    <img src="https://github.com/RogerSujay56/cokestore_llmbot/blob/main/success1.png" alt="Image 1" style="width: 30%;">
    <img src="https://github.com/RogerSujay56/cokestore_llmbot/blob/main/success2.png" alt="Image 2" style="width: 30%;">
    <img src="https://github.com/RogerSujay56/cokestore_llmbot/blob/main/success3.png" alt="Image 3" style="width: 30%;">
</div>


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
