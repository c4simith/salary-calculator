# GENERIC
PRECISION_DIGITS = 2

# PAYE
PAYE_RATEBAND = 40000
TAX_CREDIT = 3550
STANDARD_TAXRATE = 0.20
HIGHER_TAXRATE = 0.40

# USC
USC_RATEBAND = 13000
COMP1_AMOUNT = 12012
COMP2_AMOUNT = 22920 - 12012
COMP3_AMOUNT = 70044 - 22920
COMP1_RATE = 0.005
COMP2_RATE = 0.02
COMP3_RATE = 0.045
COMP4_RATE = 0.08
BAND1_CUTOFF = 22920.0
BAND2_CUTOFF = 70044.0

# PRSI
PRSI_RATEBAND = 4224
PRSI_RATE = 0.04


def calculate_paye(gross_salary):
    if gross_salary <= PAYE_RATEBAND:
        tax = gross_salary * STANDARD_TAXRATE
    else:
        standard_tax = PAYE_RATEBAND * STANDARD_TAXRATE
        higher_tax = (gross_salary - PAYE_RATEBAND) * HIGHER_TAXRATE
        tax = standard_tax + higher_tax
    paye = tax - TAX_CREDIT
    paye = round(paye, PRECISION_DIGITS)
    return paye


def calculate_usc(gross_salary):
    if gross_salary <= USC_RATEBAND:
        return 0.0

    component1 = 0
    component2 = 0
    component3 = 0
    component4 = 0
    if gross_salary <= BAND1_CUTOFF:
        component1 = COMP1_AMOUNT
        component2 = gross_salary - component1
    elif gross_salary <= BAND2_CUTOFF:
        component1 = COMP1_AMOUNT
        component2 = COMP2_AMOUNT
        component3 = gross_salary - component2 - component1
    else:
        component1 = COMP1_AMOUNT
        component2 = COMP2_AMOUNT
        component3 = COMP3_AMOUNT
        component4 = gross_salary - component3 - component2 - component1

    usc_component1 = component1 * COMP1_RATE
    usc_component2 = component2 * COMP2_RATE
    usc_component3 = component3 * COMP3_RATE
    usc_component4 = component4 * COMP4_RATE
    usc = usc_component1 + usc_component2 + usc_component3 + usc_component4
    usc = round(usc, PRECISION_DIGITS)
    return usc


def calculate_prsi(gross_salary):
    if gross_salary <= PRSI_RATEBAND:
        return 0.0

    prsi = gross_salary * PRSI_RATE
    prsi = round(prsi, PRECISION_DIGITS)
    return prsi
