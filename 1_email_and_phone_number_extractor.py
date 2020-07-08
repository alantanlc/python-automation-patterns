import pyperclip
import re


# Regular expression for phone numbers
PHONE_REGEX = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Non greedy approach for area code
    (\s|-|\.)?          # Hyper or a dot (Phone number format)
    (\d{3})             # First 3 digit
    (\s|-|\.)?          # Separator
    (\d{4})             # Last 4 digits
    )''', re.VERBOSE)

EMAIL_REGEX = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # Username
    @                   # Symbol
    [a-zA-Z0-9.-]+      # Domain name
    (\.[a-z{2,4}])      # Dot-something
    )''', re.VERBOSE)


def main():
    # Text containing email and phone number to be pasted from clipboard
    text = str(pyperclip.paste())

    # List for storing all the matched found
    match = []

    for groups in PHONE_REGEX.findall(text):
        phone_number = '-'.join([groups[1], groups[3], groups[5]])
        match.append(phone_number)

    for groups in EMAIL_REGEX.findall(text):
        match.append(groups[0])

    # Copy results to clipboard
    if len(match) > 0:
        pyperclip.copy('\n'.join(match))
        print('Copied to clipboard')
        print('\n'.join(match))
    else:
        print('Nothing found')


if __name__ == '__main__':
    main()
