# Import FastAPI to create the API
# Path is used to add validation/documentation for path parameters
# HTTPException is used to return custom HTTP errors
# Query is used to add validation/documentation for query parameters
from fastapi import FastAPI, Path, HTTPException, Query

# Import json module to work with JSON files
import json


# Create a FastAPI application instance
app = FastAPI()


# Function to load patient data from the JSON file
def load_data():
    # Open patient.json in read mode
    with open("patient.json", "r") as f:
        # Convert JSON data into a Python dictionary
        data = json.load(f)

    # Return the loaded patient data
    return data


# Root/Home endpoint
# URL: http://127.0.0.1:8000/
@app.get("/")
async def root():
    # Return a welcome message
    return {"message": "Patient Management System API"}


# About endpoint
# URL: http://127.0.0.1:8000/about
@app.get('/about')
async def about():
    # Return information about the API
    return {
        "message": "A fully functional API to manage patient records, appointments, and medical history."
    }


# View all patients
# URL: http://127.0.0.1:8000/view
@app.get("/view")
def view():
    # Load patient data from patient.json
    data = load_data()

    # Return all patient records
    return data


# View a specific patient using their patient ID
# Example URL: http://127.0.0.1:8000/patient/P001
@app.get('/patient/{patient_id}')
def view_patient(
    patient_id: str = Path(
        ...,
        description="The ID of the patient in the database",
        example="P001"
    )
):
    # Load all patient data
    data = load_data()

    # Check whether the given patient ID exists in the data
    if patient_id in data:
        # Return the details of the requested patient
        return data[patient_id]

    # If patient ID doesn't exist, return a 404 error
    raise HTTPException(
        status_code=404,
        detail=f"Patient with ID {patient_id} not found."
    )


# Sort patients based on height, weight, or BMI
# Example:
# /sort?sort_by=height&order=asc
@app.get('/sort')
def sort_patients(
    # Field on which the patients should be sorted
    sort_by: str = Query(
        ...,
        description="Sort on the basis of height, weight, or bmi"
    ),

    # Sorting order: asc (ascending) or desc (descending)
    # Default value is "asc"
    order: str = Query(
        'asc',
        description='sort in asc or desc order'
    )
):

    # List of fields that are allowed for sorting
    valid_fields = ['height', 'weight', 'bmi']

    # Check whether the requested sorting field is valid
    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort field. Must be one of {valid_fields}."
        )

    # Check whether the sorting order is valid
    if order not in ['asc', 'desc']:
        raise HTTPException(
            status_code=400,
            detail="Invalid order. Must be 'asc' or 'desc'."
        )

    # Load patient data
    data = load_data()

    # Determine sorting direction
    # reverse=True  -> Descending
    # reverse=False -> Ascending
    sort_order = True if order == 'desc' else False

    # Sort patient records based on the selected field
    # data.values() gives us all patient records
    # x.get(sort_by, 0) gets the value of height/weight/bmi
    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=sort_order
    )

    # Return the sorted patient records
    return sorted_data