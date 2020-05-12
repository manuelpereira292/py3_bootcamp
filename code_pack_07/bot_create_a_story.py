from sys import stdin

print('Enter first name:')
name_a = stdin.readline().rstrip()

print('Enter 2nd name:')
name_b = stdin.readline().rstrip()

print('Enter a location:')
location = stdin.readline().rstrip()

print('Enter a adverb:')
adverb = stdin.readline().rstrip()

print('Enter a adjective:')
adjective = stdin.readline().rstrip()

print('\n--- The Story of ' + name_a + ' and ' + name_b + '---\n')
print(name_a + ' and ' + name_b + ' were best friends who both lived in')
print('the peaceful land of ' + location + '. One day, they saw a ' + adjective)
print('grizzly bear wreaking havok in the streets. They ' + adverb + ' got their')
print('swords out and slew the beast.')
print('... The End.\n')