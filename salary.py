from validation import valid_salary
from tax import calculate_paye, calculate_usc, calculate_prsi
from validationerror import ValidationError

PRECISION_DIGITS = 2

try:
    user_input = input("Enter yearly gross salary :")
    gross_salary = float(user_input)
    if not valid_salary(gross_salary):
        raise ValidationError

    paye = calculate_paye(gross_salary)
    usc = calculate_usc(gross_salary)
    prsi = calculate_prsi(gross_salary)
    total_deductions = paye + usc + prsi
    net_salary = gross_salary - total_deductions

    monthly_gross_salary = round(gross_salary/12, PRECISION_DIGITS)
    monthly_paye = round(paye/12, PRECISION_DIGITS)
    monthly_usc = round(usc/12, PRECISION_DIGITS)
    monthly_prsi = round(prsi/12, PRECISION_DIGITS)
    monthly_total_deductions = round(total_deductions/12, PRECISION_DIGITS)
    monthly_net_salary = round(net_salary/12, PRECISION_DIGITS)

    tax_table = [
        ["", "YEARLY", "MONTHLY"],
        ["Gross Income", gross_salary, monthly_gross_salary],
        ["PAYE", paye, monthly_paye],
        ["USC", usc, monthly_usc],
        ["PRSI", prsi, monthly_prsi],
        ["Total Deductions", total_deductions, monthly_total_deductions],
        ["Net Salary", net_salary, monthly_net_salary]
    ]
    for row in tax_table:
        print(f"{row[0]:<20}{row[1]:<15}{row[2]:<15}")

except ValueError:
    print("Invalid input, a valid number expected.")
except ValidationError:
    print("Validation error occcured. Exiting.")
