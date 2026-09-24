from typing import List,Dict

from pydantic import BaseModel, EmailStr, model_validator

class Patient(BaseModel):
    name: str
    email: EmailStr 
    age: int  
    weight: float
    married: bool 
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after') #model_validator is used to validate the entire model after all fields have been validated
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Emergency contact is required for patients over 60 years old')
        return model

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted into database')

def update_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('updated in database')

patient_info = {'name': 'John Doe','email': 'john.doe@hdfc.com', 'age': 67,'married': False, 'allergies': ['peanuts', 'shellfish'], 'weight': 70.5, 'contact_details': { 'phone': '123-456-7890', 'emergency': '41354354' }}  # This is a dictionary with the patient information

patient = Patient(**patient_info)  # This will create a Patient object with the provided data

update_patient(patient)  # This will work correctly and print the patient information