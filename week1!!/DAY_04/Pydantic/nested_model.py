from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pincode: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address  # Nested model

address_info = {'city': 'New York', 'state': 'NY', 'pincode': '10001'}    
address = Address(**address_info)

patient_info = {'name': 'John Doe', 'gender': 'Male', 'age': 30, 'address': address_info}  # Nested model data
patient = Patient(**patient_info)  # This will create a Patient object with the provided data

print(patient)
print(patient.address.city)  # Accessing nested model attribute
print(patient.address.state)  # Accessing nested model attribute
print(patient.address.pincode)  # Accessing nested model attribute


#benifits of nested model are:
# 1. Reusability: Nested models allow you to define a model once and reuse it in multiple places, reducing code duplication and improving maintainability.
# 2. readability: Nested models can make your code more readable by clearly indicating the structure of your data and the relationships between different parts of your model.
# 3. Validation: Nested models can be validated independently, allowing you to catch errors early and ensure that your data is consistent and accurate.
# 4. better organization: Nested models can help you organize your code and data more effectively, making it easier to understand and work with complex data structures.