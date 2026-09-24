from typing import List,Dict

from pydantic import BaseModel, EmailStr, computed_field

class Patient(BaseModel):
    name: str
    email: EmailStr 
    age: int  
    weight: float
    height: float
    married: bool 
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field # computed_field is used to define a property that is computed based on other fields in the model. It is not stored in the database, but can be accessed like any other field.
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)  # BMI = weight(kg) / height(m)^2

        

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print('inserted into database')

def update_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(f'BMI: {patient.bmi}')
    print('updated in database')

patient_info = {'name': 'John Doe','email': 'john.doe@hdfc.com', 'age': 10,'married': False, 'allergies': ['peanuts', 'shellfish'], 'weight': 70.5, 'height': 1.75, 'contact_details': { 'phone': '123-456-7890'}}  # This is a dictionary with the patient information

patient = Patient(**patient_info)  # This will create a Patient object with the provided data

update_patient(patient)  # This will work correctly and print the patient information