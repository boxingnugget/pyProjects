#finds phone and email address from clipboard
#pastes findings in clipboard

import re, pyperclip

phone = re.compile(r'''
    (\d{3}|\(\d{3}\))? #area code
    (\s|-|\.)?#seperator
    (\d{3})#3 digits
    (\s|-|\.)#seperator
    (\d{4})#4 digits
    ''', re.VERBOSE)

email = re.compile(r'''(
    ([a-zA-Z0-9._%+-]+)#user
    (@)
    ([^.@]+)#domain name
    (\.[a-zA-Z]+)#top level domain
    )''',re.VERBOSE)

text = str(pyperclip.paste())#paste from clipboard into text

matches = []
for groups in phone.findall(text):
    matches.append('-'.join([groups[0], groups[2], groups[4]]))#standard format phone string

for groups in email.findall(text):
    matches.append(groups[0])

if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print("Matches copied to clipboard.")
else:
    print("No matches found.")