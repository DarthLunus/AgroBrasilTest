
Car Insurance Simulator API - AgroBrasil

This project is a **Car Insurance Premium Simulator API** built using **FastAPI**, **SQLAlchemy**, and **SQLite** for storing vehicle data. It calculates insurance premiums based on various car attributes, including vehicle value, deductible percentage, and broker fees. The system runs in Docker for easier deployment and scalability.

Requirements
------------
- Docker
- Docker Compose
- Python 3.10 (optional if running without Docker)

Project Structure
-----------------
/Teste_seguro
│── .venv
│── api/
│   ├── __init__.py
│   ├── routes.py
│── core/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│── domain/
│   ├── __init__.py
│   ├── models.py
│   ├── service.py
│── tests/
│   ├── __init__.py
│   ├── test_premium.py
│── .env
│── Dockerfile
│── docker-compose.yml
│── main.py
│── requirements.txt

Environment Setup
-----------------
1. **Install Docker and Docker Compose**
Make sure that **Docker** and **Docker Compose** are installed on your system. If not, you can follow the installation guides here:
- [Install Docker](https://docs.docker.com/get-docker/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

2. **Clone the Repository**
Clone the project repository to your local machine:

```bash
git clone <repository-url>
cd Teste_seguro
```

3. **Create `.env` File**
The `.env` file contains necessary environment variables for the project. It should look like this:

```ini
COVERAGE_PERCENTAGE=1.0
DATABASE_URL=sqlite:///./database.db
BROKER_FEE_DEFAULT=50.0
```

4. **Configure Docker**
The project uses **Docker** to containerize the application. Verify that the following files are present and correctly configured:

#### `docker-compose.yml`
```yaml
services:
  app:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    volumes:
      - ./car_insurance.db:/app/car_insurance.db
```

#### `Dockerfile`
```dockerfile
FROM python:3.10

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Running the Application
-----------------------
1. **Build the Docker Image**
Once you have cloned the repository, run the following command to build the Docker image:

```bash
docker-compose build
```

2. **Start the Docker Container**
After building the image, you can start the Docker container:

```bash
docker-compose up
```

This will start the FastAPI application on port `8000`, and you can access the API at:

```
http://localhost:8000
```

3. **Check the Health Endpoint**
You can verify that the server is running by navigating to the following URL:

```
http://localhost:8000
```

You should see a response like this:

```json
{
  "status": "API is running"
}
```

Testing the Premium Calculation API
------------------------------------
1. **Test the `POST /calculate_premium` Endpoint**
You can test the premium calculation API endpoint by sending a `POST` request with the necessary car details in the request body. Here's an example using `curl`:

```bash
curl -X 'POST'   'http://localhost:8000/calculate_premium'   -H 'Content-Type: application/json'   -d '{
  "make": "Toyota",
  "model": "Corolla",
  "year": 2015,
  "value": 20000,
  "deductible_percentage": 0.1,
  "broker_fee": 50.0
}'
```

You should get a response with the calculated premium details, like this:

```json
{
  "car_details": {
    "make": "Toyota",
    "model": "Corolla",
    "year": 2015,
    "value": 20000,
    "deductible_percentage": 0.1,
    "broker_fee": 50.0
  },
  "applied_rate": 0.1,
  "policy_limit": 20000.0,
  "calculated_premium": 2100.0,
  "deductible_value": 2000.0
}
```

2. **Interactive API Documentation**
FastAPI provides interactive documentation for testing the API. To access it, navigate to:

```
http://localhost:8000/docs
```

Here you can interact with the API directly, sending requests and viewing responses.

Running Tests
-------------
1. **Run Tests with `pytest`**
To run the tests locally, execute the following command inside the Docker container:

```bash
docker-compose exec app pytest
```

This will run all the tests defined in the `tests` folder, and the results will be displayed in the terminal.

Stopping the Application
-------------------------
Once you're done testing or using the application, you can stop the Docker container with the following command:

```bash
docker-compose down
```

This will stop the container and remove any associated volumes and networks.

Troubleshooting
---------------
1. **Method Not Allowed Error**
If you encounter the `Method Not Allowed` error when testing the `/calculate_premium` endpoint, make sure you are sending a `POST` request and not a `GET` request. Use the following `curl` command to test it:

```bash
curl -X 'POST'   'http://localhost:8000/calculate_premium'   -H 'Content-Type: application/json'   -d '{
  "make": "Toyota",
  "model": "Corolla",
  "year": 2015,
  "value": 20000,
  "deductible_percentage": 0.1,
  "broker_fee": 50.0
}'
```

2. **Rebuild Docker Containers**
If you make changes to the code, ensure you rebuild the Docker containers to apply the changes:

```bash
docker-compose down
docker-compose up --build
```

Conclusion
----------
This project provides a simple yet powerful car insurance premium calculation API. You can use this API to calculate insurance premiums based on various car attributes and broker fees. With Docker, you can easily deploy the system in any environment.

If you have any questions or issues, feel free to reach out or create an issue in the repository.
