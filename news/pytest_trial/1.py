

def age_validator(age):
    if not age.isdigit():
        raise ValueError('Возраст должен указываться числом')
    return int(age)


print(age_validator('Двадцать'))
