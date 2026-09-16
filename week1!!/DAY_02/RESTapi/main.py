from fastapi import FastAPI ,Path ,HTTPException
import json

app = FastAPI()

def load_data():
    with open("patient.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/")
async def root():
    return {"message": "Patient Management System API"}

@app.get('/about')
async def about():
    return {"message": "A fully functional API to manage patient records, appointments, and medical history."}

@app.get("/view")
def view():
    data = load_data()
    return data 

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="The ID of the patient in the database", example="P001")):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail=f"Patient with ID {patient_id} not found.")

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description=""))