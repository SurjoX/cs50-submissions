def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check for valid length
    if not (2 <= len(s) <= 6):
        return False

    # Check that the plate starts with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Check for invalid characters
    if not s.isalnum():
        return False

    # Check the format for numbers
    found_digit = False
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0' and not found_digit:  # Check if the first digit is '0'
                return False
            found_digit = True
        elif found_digit:  # If a letter is found after digits have started
            return False

    return True

main()
