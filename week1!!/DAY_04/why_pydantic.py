#pydantic is used for data validation and settings management using python type annotations. It enforces type hints at runtime, and provides user friendly errors when data is invalid.
#pydantic resoles typevalidation errors and datavalidation errors. It is used to validate the data that is sent to the API and also to validate the data that is returned from the API.

# def insert_patient(name, age):
#     print(name)
#     print(age)
#     print('inserted into database')
# insert_patient('John Doe', 'thirty') # This will not raise an error, but it should be an integer 

def insert_patient(name: str, age: int):
    if type(name) == str and type(age) == int: # by adding type hints, we can enforce that name should be a string and age should be an integer. If the types do not match, it will raise a TypeError.
        if age <0 :
            raise ValueError('Age cannot be negative.')
        else:
            print(name)
            print(age)
            print('inserted into database')
    else:
        raise TypeError('Invalid data type for name or age. Name should be a string and age should be an integer.')    

insert_patient('John Doe','30') # still this will not raise an error, but it should be an integer


def update_patient(name: str, age: int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('updated')
    else:
        raise TypeError('Invalid data type for name or age. Name should be a string and age should be an integer.')    

update_patient('John Doe','30')



 