# 🩺 Skin Disease Detection & LLM Advisor System

An end-to-end AI-powered system that analyzes skin images, predicts possible skin diseases using a deep learning model, and generates helpful recommendations using a Large Language Model (LLM).

This project demonstrates a **production-style ML system design** with a modular backend, real-time API, and AI-driven insights.

---

## 🚀 Project Overview

Users can upload a skin image, and the system will:

1. 🔍 Classify the skin disease using a trained deep learning model  
2. 📊 Provide prediction confidence  
3. 🤖 Generate structured recommendations using an LLM  
4. ⚡ Return results via a real-time API  

---

## 🧠 System Architecture
User (Frontend - Streamlit)
↓
FastAPI Backend (/analyze_skin)
↓
Image Preprocessing
↓
ML Model (DeiT-III)
↓
Prediction (Disease + Confidence)
↓
LLM (Gemini API)
↓
Structured Recommendations
↓
JSON Response


---

## 🏗️ Repository Structure
skin-disease-ai/
│
├── app/
│ ├── main.py # FastAPI entry point
│ ├── core/ # Config & logging
│ ├── api/ # API routes
│ ├── schemas/ # Request/response models
│ ├── services/ # Business logic (pipeline, LLM, inference)
│ ├── ml/ # ML model loading & inference
│ ├── utils/ # Helper utilities
│
├── models/ # Trained model weights (.pth)
├── training/ # Training pipeline
├── frontend/ # Streamlit UI
├── docker/ # Docker configs
├── tests/ # Unit tests
├── scripts/ # Utility scripts
│
├── .env # Environment variables
├── requirements.txt
├── README.md


---

## 🧪 Model Details

- **Architecture**: DeiT-III (Vision Transformer)
- **Training**: Transfer learning with fine-tuning
- **Dataset**: Kaggle Skin Disease Dataset  
- **Input Size**: 224 × 224  
- **Output**: Multi-class classification (skin diseases)

### ⚙️ Evaluation Metrics
- Accuracy
- Confusion Matrix
- Class-wise performance

---

## 🤖 LLM Integration

- **Model Used**: Gemini (Flash)
- Generates:
  - Recommendations
  - Next steps
  - Preventive tips

### 🔒 Safety Measures
- No medical diagnosis claims  
- Encourages consultation with a doctor  
- Controlled, structured output  

---

## 📡 API Documentation

### 🔹 Endpoint

POST /api/v1/skin/analyze

### 🔹 Request

- Content-Type: multipart/form-data  
- Body:
  - file: Image file (jpg/png/jpeg)

### 🔹 Response
{
"disease": "eczema",
"confidence": 0.92,
"recommendations": "...",
"next_steps": "...",
"tips": "..."
}


---

## 🖥️ Frontend (Streamlit)

A simple UI for testing:

- Upload image  
- View prediction  
- View AI-generated recommendations  

Run:
streamlit run frontend/app.py


---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
