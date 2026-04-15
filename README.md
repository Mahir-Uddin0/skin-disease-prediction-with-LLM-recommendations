# 🩺 Skin Diseases Prediction with LLM Recommendations

An end-to-end AI-powered system that analyzes skin images, predicts possible skin diseases using a Vision Transformer model, and generates helpful recommendations using a Large Language Model (LLM).

---

## 🚀 Project Overview

Users can upload a skin image, and the system will:

1. 🔍 Classify the skin disease using Data efficient image Transformer (DeiT) model
2. 📊 Provide prediction confidence  
3. 🤖 Generate structured recommendations using an LLM  
4. ⚡ Return results via a real-time API  

---

### Project Demonstration Video Link: https://www.youtube.com/watch?v=F_P59tSAT-4

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
LLM (Gemini 2.5 Flash API)  
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

- **Model Used**: Gemini 2.5 Flash
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
git clone https://github.com/Mahir-Uddin0/skin-disease-prediction-with-LLM-recommendations.git  
cd skin-disease-ai


---

### 2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows


---

### 3️⃣ Install Dependencies
pip install -r requirements.txt


---

### 4️⃣ Add Environment Variables

Create `.env`:
GEMINI_API_KEY=your_api_key_here


---

### 5️⃣ Run Backend
uvicorn app.main:app --reload

Open API docs:
http://127.0.0.1:8000/docs


---

## 🐳 Docker (Optional)

Build the docker image: docker build -t skin-ai .  
Run the container: docker run -p 8000:8000 skin-ai  

or,

Pull the Docker image from Docker Hub: `docker pull mahiruddin/skin-ai:latest`    
Run the container: `docker run mahiruddin/skin-ai:latest`  

---

## 🔍 Design Highlights

### 🔹 Modular Pipeline
Preprocessing → Inference → LLM → Response

### 🔹 Clean Architecture
- API layer separated from business logic  
- ML logic isolated from backend  

### 🔹 Production-Oriented
- Model loaded once at startup  
- Environment-based configuration  
- Ready for Docker deployment  

---

## ⚠️ Disclaimer

This system is for educational and demonstration purposes only.  
It is not a medical diagnostic tool. Always consult a qualified healthcare professional for medical advice.

---

## 📈 Future Improvements
 
- Model optimization for faster inference  
- Deployment on AWS (EC2/ECS)   
- Logging and monitoring system  