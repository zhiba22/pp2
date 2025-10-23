import re
pattern = r'^g.+[ing]$'
print(bool(re.fullmatch(pattern, 'gamebling')))