# aws-bedrock-er-dashboard-agent
RAG-based chat agent for ABC Hospital ER dashboard using AWS Bedrock, S3, Pinecone vector store, Lambda, and API Gateway. 

# AWS Bedrock ER Dashboard Chat Agent
A RAG-based conversational AI agent built for the ABC Hospital Emergency Room dashboard using AWS Bedrock, S3, Pinecone, Lambda, and API Gateway.

## 🏗️ Architecture

User → Chat UI (HTML) → API Gateway → Lambda → Bedrock Agent → Knowledge Base → Pinecone → S3

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| LLM | Amazon Nova Lite (AWS Bedrock) |
| Embedding Model | Amazon Titan Embed Text v2 |
| Vector Store | Pinecone (free tier) |
| Knowledge Base | AWS Bedrock Knowledge Base |
| Backend | AWS Lambda (Python 3.12) |
| API | AWS API Gateway (HTTP API) |
| Storage | Amazon S3 |
| Frontend | HTML/CSS/JavaScript |

## 📊 What it does

Answers natural language questions about ER metrics including:
- Patient wait times by department
- Satisfaction scores
- Admission rates
- Patient demographics
- Operational bottlenecks

## 💡 Key Concepts

- **RAG** (Retrieval Augmented Generation)
- **Vector embeddings** and semantic search
- **Serverless architecture**





<img width="1913" height="869" alt="image" src="https://github.com/user-attachments/assets/e7b6d615-739b-4c06-b0f9-5f91a79ff8b9" />

