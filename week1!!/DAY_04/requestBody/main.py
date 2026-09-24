from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated,Literal, Optional
import json

app = FastAPI()

class Patient(BaseModel):
    id:Annotated[str, Field(..., description="The ID of the patient in the database", example="P001")]
    name:Annotated[str, Field(..., description="The name of the patient", example="John Doe")]
    city:Annotated[str, Field(..., description="The city of the patient", example="New York")]
    age:Annotated[int, Field(..., gt=0,lt=120, description="The age of the patient", example=30)]
    gender:Annotated[Literal['male','female','other'], Field(..., description="The gender of the patient", example="female")]
    height:Annotated[float, Field(..., gt=0, description="The height of the patient in meters", example=1.75)]
    weight:Annotated[float, Field(..., gt=0, description="The weight of the patient in kilograms", example=70.5)]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)  
    
    @computed_field
    @property
    def verdict(self) -> str:
            if self.bmi < 18.5:
                return "Underweight"
            elif 18.5 <= self.bmi < 25:
                return "Normal"
            elif 25 <= self.bmi < 30:
                return "Overweight"
            else:
                return "Obese"

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None, description="The name of the patient", example="John Doe")]
    city: Annotated[Optional[str], Field(default=None, description="The city of the patient", example="New York")]
    age: Annotated[Optional[int], Field(default=None, gt=0,lt=120, description="The age of the patient", example=30)]
    gender: Annotated[Optional[Literal['male','female','other']], Field(default=None, description="The gender of the patient", example="female")]
    height: Annotated[Optional[float], Field(default=None, gt=0, description="The height of the patient in meters", example=1.75)]
    weight: Annotated[Optional[float], Field(default=None, gt=0, description="The weight of the patient in kilograms", example=70.5)]

def load_data():
    with open("patient.json", "r") as f:
        data = json.load(f)

    return data

def save_data(data):
    with open("patient.json", "w") as f:
        json.dump(data, f, indent=4)


@app.get("/")
async def root():
    return {"message": "Patient Management System API"}


@app.get("/about")
async def about():
    return {
        "message": "A fully functional API to manage patient records, appointments, and medical history."
    }


@app.get("/view")
def view():
    data = load_data()
    return data


@app.get("/patient/{patient_id}")
def view_patient(
    patient_id: str = Path(
        ...,
        description="The ID of the patient in the database",
        example="P001"
    )
):
    data = load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(
        status_code=404,
        detail=f"Patient with ID {patient_id} not found."
    )


@app.get("/sort")
def sort_patients(
    sort_by: str = Query(
        ...,
        description="Sort on the basis of height, weight, or bmi"
    ),
    order: str = Query(
        "asc",
        description="sort in asc or desc order"
    )
):
    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort field. Must be one of {valid_fields}."
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid order. Must be 'asc' or 'desc'."
        )

    data = load_data()

    sort_order = True if order == "desc" else False

    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=sort_order
    )

    return sorted_data

@app.post('/create')
def create_patient(patient: Patient):

     
    #load existing data
    data = load_data()

    #check if patient id already exists
    if patient.id in data:
        raise HTTPException(
            status_code=400,
            detail=f"Patient with ID {patient.id} already exists."
        )

    #new patient data to be added
    data[patient.id] = patient.model_dump(exclude=['id'])

    #save into the json file
    save_data(data)

    return JSONResponse(status_code=201, content={"message": f"Patient with ID {patient.id} created successfully."})

@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):
    #load existing data
    data = load_data()

    #check if patient id exists
    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail=f"Patient with ID {patient_id} not found."
        )

    #update the patient data
    existing_patient_info= data[patient_id]
    Updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key,value in Updated_patient_info.items():
        existing_patient_info[key] = value

    #existing_patient_info -> pydantic object -> updated bmi + verdict -> pydantic object -> dict 
    existing_patient_info['id'] = patient_id
    Patient_pydantic_object = Patient(**existing_patient_info)

    existing_patient_info= Patient_pydantic_object.model_dump(exclude={'id'})

    #add the updated patient info back to the data dictionary
    data[patient_id] = existing_patient_info
    #save into the json file
    save_data(data)

    return JSONResponse(status_code=200, content={"message": f"Patient with ID {patient_id} updated successfully."})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    #load existing data
    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail=f"Patient with ID {patient_id} not found."
        )

    #delete the patient data
    del data[patient_id]

    #save into the json file
    save_data(data)

    return JSONResponse(status_code=200, content={"message": f"Patient with ID {patient_id} deleted successfully."})