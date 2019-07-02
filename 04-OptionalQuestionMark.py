import re

# batRegex = re.compile(r'Bat(wo)?man')

# mo = batRegex.search('The Adventures of Batman')
# mo1 = batRegex.search('The Adventures of Batwoman')

# print( mo.group())
# print( mo1.group())

# phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo = phoneRegex.search('My number is 415-555-4242')
# mo1 = phoneRegex.search('My number is 555-4242')
# print( mo.group())
# print( mo1.group())

# phoneRegex = re.compile(r'\((\d\d\d\))?\d\d\d-\d\d\d\d')
# mo = phoneRegex.search('My number is (415)555-4242')
# mo1 = phoneRegex.search('My number is 555-4242')
# print( mo.group())
# print( mo1.group())

def search(match,text):
    Regex = re.compile(match)
    mo = Regex.search(text)

    print('Match:' + match )
    print('Text:' + text )

    if mo is None:
        print('No results')
        return

    print('Results:')
    print( mo.group())
    print('-------------------------')


# Match zero or one result

match = r'Bat(wo)?man'
search(match,'The Adventures of Batman')
search(match,'The Adventures of Batwoman')

match = r'(\d\d\d-)?\d\d\d-\d\d\d\d'
search(match,'My number is 415-555-4242')
search(match,'My number is 555-4242')

match = r'\((\d\d\d\))?\d\d\d-\d\d\d\d'
search(match,'My number is (415)555-4242')
search(match,'My number is 555-4242')


# Match zero or more results
match = 