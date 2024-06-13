- uvicorn src.app:app --reload
- poetry cmds - (init/shell/add)


### Run qdrant.py to store the document collection to vector database Qdrant. Check localhost:8000/docs to view the post request 

- uncomment last two lines of qdrant.py and save the collection to qdrant vector store by running python qdrant.py

To start the FASTAPI backend - run uvicorn src.app:app --reload
To start the react frontend - run npm start
(For loading animation run npm install react-spinners)
(For react - markdown run npm install react-markdown)