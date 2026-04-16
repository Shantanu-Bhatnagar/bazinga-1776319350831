from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="MyProject Multiplier API",
    description="An API to multiply a list of numbers.",
    version="1.0.0"
)

class NumbersInput(BaseModel):
    numbers: List[float]

@app.get("/", tags=["Root"])
async def read_root():
    """
    Welcome message for the API.
    """
    return {"message": "Welcome to MyProject Multiplier API! Visit /docs for API documentation."}

@app.post("/multiply", tags=["Multiplier"])
async def multiply_numbers(input_data: NumbersInput):
    """
    Multiplies a list of numbers provided in the request body.

    - **numbers**: A list of floating-point numbers to be multiplied.
    """
    if not input_data.numbers:
        raise HTTPException(status_code=400, detail="No numbers provided for multiplication.")
    
    product = 1.0
    for number in input_data.numbers:
        product *= number
    
    return {"result": product}
