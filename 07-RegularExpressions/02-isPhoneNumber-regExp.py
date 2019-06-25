import re

# search phone number with specific format
def isPhoneNumber(format, number):
    phoneNumRegex = re.compile(format)
    mo = phoneNumRegex.search(number)

    if mo is None:
        print('Is not a phone number')
        return

    print('Phone number found: ' + mo.group())

isPhoneNumber(r'\d\d\d-\d\d\d-\d\d\d\d', '415-555-4242')
isPhoneNumber(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)', '(415) 555-4242')

# search phone number grouped
def isPhoneNumberGrouped(format, number):
    phoneNumRegex = re.compile(format)
    mo = phoneNumRegex.search(number)

    if mo is None:
        print('Is not a phone number')
        return

    print('Phone number groups: ')
    print(mo.groups())

isPhoneNumberGrouped(r'(\d\d\d)-(\d\d\d-\d\d\d\d)', '415-555-4242')