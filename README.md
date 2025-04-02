# **Nigerian ICT Law Assistant**  

## **Project Overview**  

The **Nigerian ICT Law Assistant** is a **Retrieval-Augmented Generation (RAG) system** designed to provide answers to questions related to **Nigerian ICT laws**. It leverages a **pre-built knowledge base**, a **Large Language Model (LLM) via Groq API**, and **FAISS vector database** to retrieve relevant information efficiently.  

This chatbot helps legal professionals, policymakers, researchers, and the general public quickly access information on Nigerian ICT regulations, policies, and challenges.  

---

## **Test Questions**  

To evaluate the chatbot's accuracy in answering legal questions, use the following test cases based on the document  
*"ICT Laws in Nigeria: Planning and Regulating a Societal Journey into the Future"*.  

### **1. What is the primary objective of the *Wireless Telegraphy Act* in Nigeria?**  
   *Expected Answer:* The *Wireless Telegraphy Act* (WTA), enacted in 1961, aims to regulate the use of wireless telegraphy apparatus and ensure proper management of the radio frequency spectrum in Nigeria.  

### **2. Which agency is responsible for implementing ICT policies in Nigeria?**  
   *Expected Answer:* The National Information Technology Development Agency (NITDA) is tasked with implementing ICT policies in Nigeria, focusing on fostering the development and growth of information technology within the country.  

### **3. Identify one major challenge associated with regulating ICT in Nigeria as discussed in the document.**  
   *Expected Answer:* One significant challenge is the rapid technological convergence, which complicates the regulatory framework and necessitates continuous adaptation to effectively oversee the evolving ICT landscape.  

### **4. What is the vision outlined in Nigeria's National ICT Policy?**  
   *Expected Answer:* The vision is to transform Nigeria into a knowledge-based and globally competitive society by fully integrating Information and Communication Technologies into all facets of socio-economic development.  

### **5. According to the document, why is it necessary to regulate ICT services in Nigeria?**  
   *Expected Answer:* Regulating ICT services is essential to ensure fair competition, protect consumers, manage the radio frequency spectrum effectively, and promote national security and socio-economic development.  

These questions will help **assess the chatbot's accuracy** and its ability to retrieve relevant legal information.  

---

## **Project Structure**  

- **ICT_Law_Assistant.py** – The main **Streamlit application** that serves as the chatbot interface.  
- **llm_retrieval.py** – Handles the retrieval process and defines the **LLM-powered QA system**.  
- **vector_database.py** – Manages the **FAISS vectorstore**, including database loading and querying.  
- **vectorstore/** – Stores the FAISS vector database created from the knowledge source.  
- **Knowledge_Source/** – Contains the source documents used to build the vector database.  
- **Dockerfile** – Configuration file for containerizing the chatbot with **Docker**.  
- **Pipfile** / **Pipfile.lock** – Defines project dependencies using **pipenv**.  

---

## **Setup Instructions**  

### **1. Clone the Repository**  
```sh
git clone https://github.com/your-repo/Nigerian-ICT-Law-Assistant.git
cd Nigerian-ICT-Law-Assistant
```

### **2. Install Dependencies with pipenv**  
Ensure you have `pipenv` installed. If not, install it first:  
```sh
pip install pipenv
```

Then, install dependencies from the `Pipfile`:  
```sh
pipenv install
```

### **3. Set Up Environment Variables**  
Create a **.env** file in the project directory and add your **Groq API key** 


### **4. Run the Application**  
Activate the pipenv virtual environment:  
```sh
pipenv shell
```
Then, start the **Streamlit chatbot**:  
```sh
streamlit run ICT_Law_Assistant.py
```

---

## **Running with Docker**  

To run the chatbot using **Docker**, first build the image:  
```sh
docker build -t nigerian-ict-law-assistant .
```
Then, run the container:  
```sh
docker run -p 8501:8501 -v $(pwd)/vectorstore:/app/vectorstore nigerian-ict-law-assistant
```
The chatbot will be available at: **http://localhost:8501**