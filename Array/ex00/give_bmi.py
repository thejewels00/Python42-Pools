def give_bmi(height: list[int | float], weight:
             list[int | float]) -> list[int | float]:
    '''this function calculates the BMI of a person using the formula: '''
    print(tuple(zip(height, weight)))
    return [w / h ** 2 for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''this function returns a list of boolean values where True means the BMI 
    is greater than the limit'''
    return [True if b > limit else False for b in bmi]
