# 🌱 Sustainable Smart City Assistant (Powered by IBM Watsonx Granite LLM)

## 🔍 Overview

The **Sustainable Smart City Assistant** is an AI-powered system designed to promote urban sustainability, enhance governance, and engage citizens using IBM Watsonx Granite LLM. It delivers intelligent dashboards, a natural language chatbot, document summarization, eco-friendly advice, forecasting, and anomaly detection to support smart city decision-making.

## 👥 Team

- **Team Leader**: Jakku Kumarswami  
- **Team Members**:  
  - Tripura Garikipati  
  - Kalavathi Gandham  
  - Kailash Gonam  

---

## 🎯 Objective

To develop a scalable, modular AI assistant that:

- Analyzes city data in real-time
- Improves citizen engagement
- Supports sustainable urban governance
- Provides predictive and actionable insights

---

## 🧠 Key Features

- ✅ AI-powered Chat Assistant for eco-advice and urban queries  
- 📈 Real-time sustainability dashboards (KPI monitoring)  
- 📝 Document summarization using LLM  
- 🔍 Anomaly detection and forecasting via ML  
- 🌍 Citizen feedback analysis using NLP  
- 🔁 Scalable and modular architecture  

---

## 🧰 Tech Stack

| Layer       | Tools / Technologies                         |
|-------------|----------------------------------------------|
| Frontend    | Streamlit / React                            |
| Backend     | FastAPI (Python)                             |
| AI/LLM      | IBM Watsonx Granite LLM via Hugging Face     |
| ML/NLP      | Scikit-learn, Statsmodels                    |
| Database    | PostgreSQL / MongoDB                         |
| Deployment  | IBM Cloud, Docker                            |

---

## 🏗️ Architecture

1. **User Access**: Login → Interact with dashboard or chat assistant  
2. **Input Processing**: Questions, documents, or data submitted  
3. **AI Inference**: Watsonx Granite LLM + ML models process input  
4. **Outputs**: Summaries, recommendations, forecasts, anomalies  
5. **UI/UX**: Responsive, multilingual, and mobile-friendly interface  

---

## 🚀 Modules & Functionality

| Module         | Functionality                                               |
|----------------|-------------------------------------------------------------|
| Chatbot        | Natural language interface for eco-advice & general queries |
| Summarizer     | Condenses city documents and feedback using LLM             |
| Forecasting    | Predicts KPI trends using Linear Regression                 |
| Anomaly        | Detects data outliers (e.g., energy/water consumption)      |
| Eco-Tips       | Provides environmentally friendly tips                      |

---

## 🧪 Testing & Validation

- ✅ Chatbot response correctness
- ✅ KPI dashboards – real-time updates
- ✅ Summarization accuracy
- ✅ Forecasting error margin < 10%
- ✅ Performance under 100+ concurrent users
- ✅ UI responsiveness and input validation

---

## 📅 Agile-Based Development Timeline

| Sprint | Focus                                        |
|--------|----------------------------------------------|
| 1      | Base architecture & LLM setup                |
| 2      | Dashboard UI + City Data Integration         |
| 3      | Chatbot, Summarizer, Feedback Modules        |
| 4      | Forecasting, Anomaly Detection, Integration  |
| 5      | Final testing, bug fixing, deployment        |

---

## 🛠 Challenges & Fixes

- LLM latency → Resolved with async + caching  
- Noisy data → Preprocessing & validation  
- Deployment → Docker + GitHub CI/CD  
- UI glitches → Modular Streamlit refactor  

---

## 📦 Running the Project

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
# Sustainable-Smart-City-Assistant-Using-IBM-Granite-LLM
