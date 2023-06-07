def valid_salary(gross_salary):
    if gross_salary <= 0:
        print(f"{gross_salary} : Invalid salary, a positive numbere expected")
        return False
    return True
