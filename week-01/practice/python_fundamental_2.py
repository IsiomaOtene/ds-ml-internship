state_records = [
    {"state": "Akwa Ibom", "registered": "1200", "votes_cast": 684},
    {"state": "Bauchi", "registered": "950", "votes_cast": 611},
    {"state": "Gombe", "registered": "1500", "votes_cast": 720},
    {"state": "Delta", "registered": "0", "votes_cast": 0},
    {"state": "Ebonyi", "registered": "800", "votes_cast": 536},
]
new_records = []
for record in state_records:
    state_data = {
        "state": record["state"],
        "registered": record["registered"],
        "votes_cast": record["votes_cast"],
        "turnout_percentage": 0
    }
    new_records.append(state_data)

highest_turnout = 0
highest_turnout_state = ""
for record in new_records:
    if int(record["registered"]) > 0:
        turnout = (int(record["votes_cast"])) / (int(record["registered"])) * 100
    else:
        turnout = 0
    record["turnout_percentage"] = turnout
    if turnout > highest_turnout:
        highest_turnout = turnout
        highest_turnout_state = record["state"]
print("States with turnout above 60%:")
for record in new_records:
    if record["turnout_percentage"] > 60:
        print(f"- {record['state']}: {record['turnout_percentage']}%")
valid_state_count = 0
    if valid_state_count > 0:
        average_turnout = total_turnout / valid_state_count
        print(f"Average turnout (excluding zero-registration states): {round(average_turnout, 2)}%")
        print (f"In {state_data['state']}, {state_data['votes_cast']} out of {state_data['registered']} registered voters voted, and the turnout is {state_data['turnout_percentage']}%")
#assertions
assert state_data["turnout_percentage"] <= 100, f"Error: {state_data['state']} has a turnout greater than 100%."
assert len(new_records) == len(state_records), "Error: The number of new records does not match the original data."
if state_data["state"] == "Ebonyi":
    assert state_data["turnout_percentage"] == 0, "Error: Ebonyi should have a turnout percentage of 0%."
print(f"All assertions passed.")