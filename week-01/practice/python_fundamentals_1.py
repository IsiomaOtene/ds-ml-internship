def calculate_turnout(registered, votes_cast):
    if registered == 0:
        return 0.0
    # to calculate percentage
    percentage = (votes_cast / registered) * 100
    return percentage
def turnout_band(percentage):
    if percentage < 40:
        return "low "
    elif percentage <= 60:
        return "moderate"
    else:
        return "high"
print ("Test inputs")
assert calculate_turnout(100, 55) == "moderate"
assert calculate_turnout(100, 30) == "low"
assert calculate_turnout(100, 72) == "high"
assert calculate_turnout(0, 0) == "low"
assert calculate_turnout(100, 45) == "moderate"
print ("Test assertions inputs passed successfully")
assert calculate_turnout(100, 50) == "moderate"
assert calculate_turnout(100, 30) == 30.0
print("Assertions passed successfully")