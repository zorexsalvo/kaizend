
def gather_info():
    weight = float(input('What is your weight? in kilograms or in pounds'))
    height = float(input('What is your height? in meters on in inches'))
    system = input('Are your measurements in metric or imperial units?').lower().strip()
    return (height, weight, system)


def calculate_bmi(height, weight, system='metric', **kwargs):
    """
    Return the the Body Mass Index (BMI) for the given
    weight, height, and measurement system.
    """
    if system == 'metric':
        bmi = weight / height ** 2
    elif system == 'imperial':
        bmi = 703 * (weight / height ** 2)
    return bmi


def main():
    while True:
        height, weight, system = gather_info()
        if system.startswith('i'):
            bmi = calculate_bmi(height, weight, system='imperial')
            print(f"Your BMI is {bmi}")
            break
        elif system.startswith('m'):
            bmi = calculate_bmi(weight, height)
            print(f"Your BMI is {bmi}")
            break
        else:
            print("Error: Unknown measurement system. Please use imperial or metric.")

if __name__ == '__main__':
    main()