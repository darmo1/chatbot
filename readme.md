# 🚀 Chatbot Agent 

We are using FastApi for creating a  ecommerce chatbot 

## 🧱 Features

- ⚡️ Asynchronous API with FastAPI
- 🐘 PostgreSQL support via SQLAlchemy or SQLModel
- 🔐 JWT authentication
- 📦 Dependency management with `pip` and `venv`
- 🧪 Testing support with `pytest`
- 🧰 Docker-ready (optional)
- 🗂 Modular project structure

## 📁 Project Structure

```plaintext
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── agent
│   │   ├── __init__.py
│   │   └── routes.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## 🚀 Quick Start

1. Clone the repository:
   ```bash
   
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure your keys in `.env`.
5. Start the application:
   ```bash
   uvicorn app/main.py --reload
   ```
6. Access the API documentation at `http://localhost:8000/docs`.


## 📚 Documentation

Full API documentation is automatically generated and available at `/docs` once the app is running.
---

Ready to build something amazing