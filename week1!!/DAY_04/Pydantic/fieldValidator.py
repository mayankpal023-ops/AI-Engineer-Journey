from typing import List,Dict

from pydantic import BaseModel, EmailStr, field_validator

class Patient(BaseModel):
    name: str
    email: EmailStr 
    age: int  
    weight: float
    married: bool 
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        #abc@gmail.com
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f'Email domain must be one of {valid_domains}')
        return value

    
    @field_validator('name')
    @classmethod
    def transfor_name(cls, value):
        return value.upper()  # This will transform the name to uppercase before validation

    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 120:
            return value
        else:
            raise ValueError('Age must be between 0 and 120')
        

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted into database')

def update_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('updated in database')

patient_info = {'name': 'John Doe','email': 'john.doe@hdfc.com', 'age': '10','married': False, 'allergies': ['peanuts', 'shellfish'], 'weight': 70.5, 'contact_details': { 'phone': '123-456-7890'}}  # This is a dictionary with the patient information

patient = Patient(**patient_info)  # This will create a Patient object with the provided data

update_patient(patient)  # This will work correctly and print the patient information