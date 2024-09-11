How to run application:

1. Install Dependencies
In the terminal, install the necessary Python packages:

pip install fastapi uvicorn sqlalchemy python-jose[cryptography] passlib[bcrypt] psycopg2

-------

2. Running the FastAPI Backend
Start the FastAPI server:

In the terminal, run the following command to start the server with auto-reload:

uvicorn main:app --reload

Visit the interactive API documentation at:

http://127.0.0.1:8000/docs

--------

3.Running the Frontend

Navigate to the frontend directory:

cd path/to/frontend

Start a simple HTTP server:

python3 -m http.server

Access the frontend at:

http://localhost:8000/


------------

4.PostgreSQL Database Setup

Log into PostgreSQL:

psql -U postgres

Connect to your database:

\c your_database_name

View the cadastro table data:

SELECT * FROM cadastro;



