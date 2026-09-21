from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted into database')

patient_info = {'name': 'John Doe', 'age': 30}

patient = Patient(**patient_info)  # This will create a Patient object with the provided data

insert_patient(patient)  # This will work correctly and print the patient information