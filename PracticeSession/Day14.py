# Expected List: expected = ["iPhone 15", "iPhone 15 Pro", "iPhone 15 Pro Max"]
# Actual List (Scraped): actual = ["iPhone 15", "iPhone 14", "iPhone 15 Pro Max"]
# The Task: Write a loop that compares these two lists. If a name in actual does
# not match the name in expected, print: "Validation Failed: Expected [item] but found [item] at index [i]".


actual = ["iPhone 15", "iPhone 14", "iPhone 15 Pro Max"]
expected = ["iPhone 15 proo", "iPhone 15", "iPhone 15 Pro Max"]

for i in range(len(actual)):

    # Check if the current actual item exists ANYWHERE in the expected list
    if actual[i] in expected:
        # Match found: actual[i] is present in 'expected'
        print(f"Match Found: {actual[i]} is in the expected list.",{i})
    else:
        # No match found after checking all items in 'expected'
        print(f"Validation Failed: {actual[i]} at index {i} was not found in the expected list.")

print("-------------------------------------------")

actual = ["iPhone 15", "iPhone 14", "iPhone 15 Pro Max"]
expected = ["iPhone 15 proo", "iPhone 15", "iPhone 15 Pro Max"]

for i in range(len(actual)):
    # Check if the current item from 'actual' exists anywhere in 'expected'
    if actual[i] in expected:
        # Get the specific index where it was found in the 'expected' list
        match_index = expected.index(actual[i])
        print(f"Match Found: '{actual[i]}' at actual index {i} matches expected index {match_index}.")
    else:
        # If it is not found at all, print the failure message
        print(f"Validation Failed: Expected an item but found '{actual[i]}' at index {i} which is not in the expected list.")

print("-------------------------------------")