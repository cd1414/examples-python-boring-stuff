import re

heroRegex = re.compile(r'Batman|Tina Fey')
mo = heroRegex.search('Batman and Tina Fey')
print(mo.group())

heroRegex = re.compile(r'Tina Fey|Batman')
mo = heroRegex.search('Tina Fey and Batman ')
print(mo.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))