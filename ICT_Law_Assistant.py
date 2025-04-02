import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

# Load env variables
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

DB_FAISS_PATH = "vectorstore/db_faiss"

@st.cache_resource
def get_vectorstore():
    embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    db = FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)
    return db

def set_custom_prompt(custom_prompt_template):
    prompt = PromptTemplate(
        template=custom_prompt_template, 
        input_variables=["context", "question"]
    )
    return prompt

def load_llm():
    return ChatGroq(
        model="deepseek-r1-distill-llama-70b",
        temperature=0.5,
        groq_api_key=os.environ.get("GROQ_API_KEY")
    )

def main():
    st.title("ICT Law Assistant Chatbot")

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        st.chat_message(message['role']).markdown(message['content'])

    prompt = st.chat_input("Ask your question about Nigerian ICT laws...")

    if prompt:
        st.chat_message('user').markdown(prompt)
        st.session_state.messages.append({'role': 'user', 'content': prompt})

        CUSTOM_PROMPT_TEMPLATE = """
        Use only the given context to answer the user's question.
        If the answer is not in the context, say "I don't know."
        Do not include any additional explanations.

        Context: {context}
        Question: {question}

        Provide only the answer.
        """
        
        try: 
            vectorstore = get_vectorstore()
            if vectorstore is None:
                st.error("Failed to load the knowledge base")

            qa_chain = RetrievalQA.from_chain_type(
                llm=load_llm(),
                chain_type="stuff",
                retriever=vectorstore.as_retriever(search_kwargs={'k': 3}),
                return_source_documents=True,
                chain_type_kwargs={'prompt': set_custom_prompt(CUSTOM_PROMPT_TEMPLATE)}
            )

            response = qa_chain.invoke({'query': prompt})

            result = response["result"]
            source_documents = response["source_documents"]
            
            # Format sources to display only unique documents
            unique_sources = set(
                f"{doc.metadata.get('source', 'Unknown')} (page {doc.metadata.get('page', 'N/A')})"
                for doc in source_documents
            )
            sources = "\n\n**Sources:**\n" + "\n".join(f"- {src}" for src in unique_sources)
            
            st.chat_message('assistant').markdown(result + sources)
            st.session_state.messages.append({'role': 'assistant', 'content': result + sources})

        except Exception as e:
            st.error(f"Error processing your request: {str(e)}")
            st.session_state.messages.append({'role': 'assistant', 'content': f"Error: {str(e)}"})

if __name__ == "__main__":
    main()
