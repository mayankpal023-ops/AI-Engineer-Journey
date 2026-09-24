from typing import Optional,List,Dict, Annotated

from pydantic import BaseModel, EmailStr, AnyUrl, Field

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='The name of the patient in less than 50 characters', example=['John Doe','amit'])] # name must be a string with a maximum length of 50 characters
    email: EmailStr #it will validate the email address format
    age: int = Field(gt = 0, lt=120) # age must be greater than 0
    linkedin_url: AnyUrl #it will validate the URL format
    weight: Annotated[float, Field(gt = 0, strict=True)]  # weight must be greater than 0 # strict=True means that the value must be a float, not an int
    married: Annotated[bool, Field(default=False, description='Indicates if the patient is married')] = False #default value for married is False
    allergies: Annotated[Optional[List[str]], Field(max_length = 5)] = None # optional field for allergies, can be None or a list of strings
    contact_details: Dict[str, str]

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted into database')

def update_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('updated in database')

patient_info = {'name': 'John Doe','email': 'john.doe@example.com', 'age': 10,'linkedin_url': 'https://www.linkedin.com/in/johndoe', 'weight': 70.5, 'contact_details': { 'phone': '123-456-7890'}}  # This is a dictionary with the patient information

patient = Patient(**patient_info)  # This will create a Patient object with the provided data

update_patient(patient)  # This will work correctly and print the patient information