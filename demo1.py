import string, random

capita = ''
words = ''.join((string.ascii_letters, string.digits))

for i in range(6):
    capita += random.choice(words)
print(capita)