import re

phoneNumberRegex = re.compile(r'''
    (\d{3}-|\(\d{3}\))#area code
    (\d{3}-\d{4})#rest of number
    ''', re.VERBOSE)#creates regular expression object in the xxx-xxx-xxxx format

matchedObject = phoneNumberRegex.findall('test phone number 703-420-6969 or 703-324-4343')#searches what is passed thru
print(matchedObject)
#areaCode, number = matchedObject.group()
#print(matchedObject.group())#returns phone numbers found