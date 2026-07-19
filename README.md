# AI Travel Assistant using Azure OpenAI

An intelligent travel assistant built with **Python** and **Azure OpenAI Responses API** that answers questions using both **private travel brochures** and **real-time web information**.

The application demonstrates Retrieval-Augmented Generation (RAG) by combining Azure OpenAI Vector Stores with Web Search, allowing users to ask natural language questions about travel services and destinations.

---

# Features

* Uploads PDF travel brochures into an Azure OpenAI Vector Store
* Performs semantic search across uploaded documents
* Retrieves real-time travel information using Web Search
* Maintains conversation history for contextual responses
* Uses Microsoft Entra ID authentication (Azure AD)
* Simple command-line interface

---

# Architecture

```
                 User Question
                       │
                       ▼
             Azure OpenAI Responses API
                       │
        ┌──────────────┴──────────────┐
        │                             │
        ▼                             ▼
 File Search Tool              Web Search Tool
        │                             │
        ▼                             ▼
 Azure Vector Store          Live Internet Search
        │                             │
        └──────────────┬──────────────┘
                       ▼
               AI Generated Response
```

---

# Tech Stack

* Python
* Azure OpenAI
* Azure AI Foundry
* Azure OpenAI Responses API
* Azure Vector Stores
* File Search
* Web Search
* Microsoft Entra ID
* Azure Identity SDK
* python-dotenv

---

# Project Structure

```
.
├── Brochures/
│   ├── brochure1.pdf
│   ├── brochure2.pdf
│   └── ...
│
├── .env
├── main.py
├── requirements.txt
└── README.md
```

---

# Environment Variables

Create a `.env` file.

```env
AZURE_OPENAI_ENDPOINT=https://YOUR_PROJECT.services.ai.azure.com/api/projects/YOUR_PROJECT

MODEL_DEPLOYMENT=gpt-5
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ai-travel-assistant.git

cd ai-travel-assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

Login to Azure

```bash
az login
```

Run the application

```bash
python main.py
```

---

# How It Works

## Step 1

The application creates an Azure OpenAI Vector Store.

## Step 2

All PDF brochures located in the `Brochures/` folder are uploaded and indexed.

## Step 3

The user asks a question in natural language.

Example:

```
What travel packages are available for Spain?
```

## Step 4

The Responses API automatically chooses between:

* File Search (company brochures)
* Web Search (current destination information)

or combines both.

## Step 5

The assistant returns a grounded answer using private documents together with real-time information.

---

# Example Questions

* What tours does Margie's Travel offer?
* Which package includes flights?
* Tell me about Barcelona.
* What is the weather like in Rome?
* Are there any travel advisories for Japan?
* Which brochure includes Mediterranean cruises?

---

# Authentication

This project uses **Microsoft Entra ID** instead of API keys.

Authentication is handled using:

```python
DefaultAzureCredential()
```

This allows secure authentication in local development and Azure-hosted environments.

---

# Key Azure OpenAI Features Demonstrated

* Responses API
* Vector Stores
* File Search Tool
* Web Search Tool
* Conversation Memory
* Retrieval-Augmented Generation (RAG)

---

# Future Improvements

* Streamlit or React web interface
* Voice interaction
* Image understanding for travel brochures
* Hotel and flight booking integration
* Travel itinerary generation
* Multi-language support
* Citation display for retrieved documents

---

# Learning Outcomes

This project demonstrates how to:

* Build enterprise-grade RAG applications
* Integrate Azure OpenAI Vector Stores
* Combine private document retrieval with live web search
* Maintain conversational memory
* Authenticate securely using Microsoft Entra ID
* Develop AI assistants with the Azure OpenAI Responses API

---

# License

This project is licensed under the MIT License.
