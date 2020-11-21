import re

phoneNumberRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')#creates regular expression object in the xxx-xxx-xxxx format
matchedObject = phoneNumberRegex.search('test phone number 703-420-6969')#searches what is passed thru
print(matchedObject.group())#returns phone numbers found