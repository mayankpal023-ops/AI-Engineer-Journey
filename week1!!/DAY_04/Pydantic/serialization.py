from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pincode: str

class Patient(BaseModel):
    name: str
    gender: str = 'male'
    age: int
    address: Address  # Nested model

address_info = {'city': 'New York', 'state': 'NY', 'pincode': '10001'}    
address = Address(**address_info)

patient_info = {'name': 'John Doe','age': 30, 'address': address_info} 
patient = Patient(**patient_info)  

print(patient)
print(patient.address.city) 
print(patient.address.state)  
print(patient.address.pincode)  


temp = patient.model_dump(include={'name', 'age'})
print(temp)
print(type(temp))

pemp = patient.model_dump_json(exclude={'address': {'state'}})
print(pemp)
print(type(pemp))

simp = patient.model_dump(exclude_unset=True) # gender will be excluded as it is not set in the patient_info dictionary
print(simp)