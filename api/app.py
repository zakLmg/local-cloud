"""
Main script.
"""

# Required external packages
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Launch the FastAPI server
app = FastAPI() 

# Routes
@app.get('/')
def read_root():
    """
    Hello world route example.
    """
    # Output content
    output = {"Hello": "World"}
    return JSONResponse(status_code=200, content=output)

@app.get('/date')
def get_nowdate():
    """
    Get today's date timestamp.
    """
    # Output content
    output = {"date": datetime.now().__str__()}
    return JSONResponse(status_code=200, content=output)
