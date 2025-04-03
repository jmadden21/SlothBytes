# You have received an encrypted message from space. Your task is to decrypt the message with the following simple rules:
# Message string will consist of capital letters, numbers, and brackets only.
# When there's a block of code inside the brackets, such as [10AB], it means you need to repeat the letters AB for 10 times.
# Message can be embedded in multiple layers of blocks.
# Final decrypted message will only consist of capital letters.
# Create a function that takes encrypted message str and returns the decrypted message.

# spaceMessage("ABCD")
# output = "ABCD"

# spaceMessage("AB[3CD]")
# output = "ABCDCDCD"
# # "AB" = "AB"
# # "[3CD]" = "CDCDCD"
# # Combine both = "ABCDCDCD"
# spaceMessage("IF[2E]LG[5O]D")
# output = "IFEELGOOOOOD"

def spaceMessage(message):
    stack = []
    current_string = ""
    current_num = 0

    for char in message:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif char == ']':
            prev_string, repeat_count = stack.pop()
            current_string = prev_string + current_string * repeat_count
        else:
            current_string += char

    return current_string


message = "IF[2E]LG[5O]D"
result = spaceMessage(message)
print(result)
