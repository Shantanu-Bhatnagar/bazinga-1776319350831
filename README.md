# MyProject - Multiplier API

This is a simple FastAPI project that provides an API endpoint to multiply a list of numbers.

## Project Structure


.
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md


## How to Run

### 1. Locally (without Docker)

1.  **Clone the repository (if applicable):**
    bash
    git clone <repository-url>
    cd MyProject
    
2.  **Create a virtual environment:**
    bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    
3.  **Install dependencies:**
    bash
    pip install -r requirements.txt
    
4.  **Run the application:**
    bash
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    
    The API will be available at `http://127.0.0.1:8000`.
    The interactive API documentation (Swagger UI) will be at `http://127.0.0.1:8000/docs`.

### 2. Using Docker

1.  **Ensure Docker is installed and running.**
2.  **Build and run the Docker containers:**
    bash
    docker-compose up --build
    
    This will build the Docker image and start the FastAPI application.
    The API will be available at `http://127.0.0.1:8000`.
    The interactive API documentation (Swagger UI) will be at `http://127.0.0.1:8000/docs`.

3.  **To stop the containers:**
    bash
    docker-compose down
    

## API Endpoints

### `GET /`

*   **Description:** Root endpoint, returns a welcome message.
*   **Response:**
    
    {"message": "Welcome to MyProject Multiplier API! Visit /docs for API documentation."}
    

### `POST /multiply`

*   **Description:** Multiplies a list of numbers.
*   **Request Body:**
    
    {
      "numbers": [1.0, 2.5, 3.0]
    }
    
    *   `numbers` (array of floats, required): A list of numbers to be multiplied.
*   **Response (Success):**
    
    {
      "result": 7.5
    }
    
*   **Response (Error - No numbers provided):**
    
    {
      "detail": "No numbers provided for multiplication."
    }
    
    *   Status Code: `400 Bad Request`

## Example Usage (using `curl`)

bash
# Health check
curl http://localhost:8000/

# Multiply numbers
curl -X POST "http://localhost:8000/multiply" \
     -H "Content-Type: application/json" \
     -d '{"numbers": [2, 3, 4]}'

# Multiply with floats
curl -X POST "http://localhost:8000/multiply" \
     -H "Content-Type: application/json" \
     -d '{"numbers": [1.5, 2.0, 3.0]}'

# Error case: empty list
curl -X POST "http://localhost:8000/multiply" \
     -H "Content-Type: application/json" \
     -d '{"numbers": []}'

