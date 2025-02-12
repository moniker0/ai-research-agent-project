## 📌 AI-Powered Research Agent
🔍 A Web-Based AI Assistant for Research Queries
This project is an AI-powered research assistant that retrieves live web search results using Google Custom Search API and generates AI-powered insights using OpenAI's GPT-4-Turbo.

The application is built using Python, Streamlit, OpenAI API, and Google Custom Search API, and it provides an interactive web UI for users to enter research queries and receive AI-generated responses.

### 🚀 Features
✅ Live Web Search – Fetches the latest information from Google Custom Search API.
✅ AI-Powered Insights – Uses GPT-4-Turbo to summarize key points concisely.
✅ Interactive Web UI – Built using Streamlit for an intuitive user experience.
✅ Dynamic Response Generation – Merges AI insights with live search data.
✅ Rate Limit Handling – Implements API fallback strategies to ensure smooth operation.

### 🛠️ Tech Stack
Backend: Python, OpenAI GPT-4 API, Google Custom Search API
Frontend: Streamlit
APIs Used:
OpenAI GPT-4-Turbo (for AI-powered response generation)
Google Custom Search API (for fetching live web results)
Deployment: Localhost / Streamlit Cloud

### ⚡Here's How it Looks!
<img width="636" alt="image" src="https://github.com/user-attachments/assets/0937e37f-94fe-4a33-a368-769ab54ce07c" />


### 📝 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/AI-powered-Research-Agent.git
cd AI-powered-Research-Agent

2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Up API Keys
Create a .env file in the project directory and add your API keys:
OPENAI_API_KEY=your-openai-api-key
GOOGLE_API_KEY=your-google-api-key
GOOGLE_CSE_ID=your-google-cse-id

### 💡 Usage
Run the Streamlit Web App

streamlit run AI-Research-Agent.py

Open http://localhost:8501 in your browser.
Enter your research query in the text box.
Click "Generate Answer" to get AI-powered insights.

### 🛠️ Troubleshooting
Common Issues & Fixes
RateLimitError (429)	Reduce API calls, lower max_tokens, or upgrade OpenAI plan

### 🎯 Future Enhancements
🔹 Cache Responses – Store AI responses to reduce redundant API calls.
🔹 UI Improvements – Add search filters and better visualization.
🔹 Multi-Model Support – Allow users to choose GPT-4 or GPT-3.5.
🔹 Mobile-Friendly UI – Optimize for small screens.
