# FastAPI Data Receiver

A simple FastAPI application for receiving and storing data.

## Project Structure

```
getdata_method/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py       # Pydantic models
│   ├── routers/
│   │   ├── __init__.py
│   │   └── data.py          # Data endpoints
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py        # Configuration
│   │   └── auth.py          # Authentication
│   └── utils/
│       ├── __init__.py
│       └── file_handler.py  # File operations
├── data/                    # Data storage directory
├── .env                     # Environment variables
├── requirements.txt         # Python dependencies
├── main.py                  # Entry point (current file)
└── README.md               # This file
```

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file with your configuration:
   ```bash
   cp .env.example .env
   ```

3. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints

- `PUT /api/v1/ingest` - Receive and store data (requires authentication)
- `GET /api/v1/health` - Health check endpoint
- `GET /docs` - API documentation (Swagger UI)

## Authentication

The API uses Bearer token authentication. Set the `API_TOKEN` environment variable.