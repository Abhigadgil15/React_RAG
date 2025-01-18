Backend Setup (FastAPI + Qdrant + Poetry)
To get started with the backend, follow these steps:

Install dependencies:

Navigate to the backend folder and run the following command to install the required packages:
poetry install
To store the document collection in the Neo4j database, run the qdrant.py script. This script will populate the data into the Qdrant vector store.
If you encounter any "missing file" errors, ensure all dependencies are installed by running poetry install in the backend folder.
Uncomment the last two lines in qdrant.py to save the collection to the Qdrant vector store. Then, execute the script with:

python qdrant.py
Start the FastAPI Backend:

Run the FastAPI backend server using Uvicorn with the following command:
uvicorn src.app:app --reload
Once the server is running, you can access the API documentation at localhost:8000/docs.
