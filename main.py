import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("Coke Store: Database Q&A 🥤")

question = st.text_input("Question: ")
clicked = st.button("Get Answer")

if clicked:
    if question:
        try:
            chain = get_few_shot_db_chain()
            response = chain.run(question)

            st.header("Answer")
            st.write(response)
        except Exception as e:

            st.error("Sorry, there was an error processing your request.")
            st.write("We will get back to you as soon as possible.")
            st.write(e)
    else:
        st.warning("Please enter a question.")