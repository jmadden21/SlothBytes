"""
Someone is typing on the sticky keyboard.
Occasionally a key gets stuck and more than intended number of characters
of a particular letter is being added into the string. The function input contains original and typed strings.

Determine if the typed string has been made from the original.
Return true if it is and false if the typed string cannot have been made from the original.

Example:
    #function: isLongPressed(original, typed)
isLongPressed("alex", "aaleex")
output = true

isLongPressed("saeed", "ssaaedd")
#original contains 2 E's, but the typed only has 1. Not a sticky key issue.
output = false

isLongPressed("leelee", "lleeelee")
output = true

isLongPressed("Tokyo", "TTokkyoh")
#An h was typed, not a sticky key problem, just skill issues.
output = false

isLongPressed("laiden", "laiden")
output = true
"""

def isLongPressed(original, typed):
    original_index = 0
    typed_index = 0
    original_length = len(original)
    typed_length = len(typed)
    while original_index < original_length and typed_index < typed_length:
        if original[original_index] == typed[typed_index]:
            original_index += 1
            typed_index += 1
        elif typed_index > 0 and typed[typed_index] == typed[typed_index - 1]:
            typed_index += 1
        else:
            return False
    while typed_index < typed_length:
        if typed[typed_index] != typed[typed_index - 1]:
            return False
        typed_index += 1
    return original_index == original_length


#main function, user inputs original and typed string,
# output true or false, true if sticky key issue, false if not

if __name__ == "__main__":
    while True:
        original = input("Enter the original string: ")
        typed = input("Enter the typed string: ")
        result = isLongPressed(original, typed)
        print(f"Is the typed string made from the original? {result}")
        run_again = input("Do you want to run the program again? (yes/no): ").strip().lower()
        if run_again != 'yes':
            break