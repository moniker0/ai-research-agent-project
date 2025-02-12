#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import openai
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# In[2]:


# Retrieve API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

# Initialize OpenAI Client
client = openai.Client(api_key=OPENAI_API_KEY)

# Function to fetch search results from Google Custom Search API
def fetch_google_search_results(query, num_results=5):
    """Fetch web search results using Google Custom Search API."""
    search_url = "https://www.googleapis.com/customsearch/v1"

    params = {
        "q": query,
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_CSE_ID,
        "num": num_results
    }

    response = requests.get(search_url, params=params)

    if response.status_code == 200:
        search_data = response.json()
        search_snippets = []

        if "items" in search_data:
            for item in search_data["items"]:
                title = item.get("title", "No Title")
                snippet = item.get("snippet", "No Snippet")
                link = item.get("link", "#")

                search_snippets.append(f"**[{title}]({link})**\n{snippet}")

        return "\n\n".join(search_snippets)

    else:
        return "⚠️ No relevant search results found."

# Function to generate AI-powered response
def generate_ai_response_with_search(query):
    """Generate an AI-powered research response with web search results."""
    
    search_results = fetch_google_search_results(query)

    prompt = f"""
    You are an AI-powered research assistant. Answer the following query in a structured and detailed manner.

    **Query:** {query}

    Below are some relevant search results:
    {search_results}

    Summarize the key insights and provide an accurate, well-structured answer.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "system", "content": "You are a helpful AI research assistant."},
                      {"role": "user", "content": prompt}],
            max_tokens=300
        )
        return response.choices[0].message.content

    except openai.RateLimitError:
        return "❌ You have exceeded your OpenAI API quota. Please check your billing plan."

# Streamlit UI
st.title("🔍 AI-Powered Research Agent")
st.write("Ask a question, and I will fetch live search results and generate an AI-powered answer!")

query = st.text_input("Enter your research query:")

if st.button("Generate Answer"):
    if query:
        with st.spinner("Fetching information..."):
            response = generate_ai_response_with_search(query)
            st.subheader("🔹 AI Research Response")
            st.markdown(response)
    else:
        st.warning("⚠️ Please enter a query to search.")


# In[ ]:




