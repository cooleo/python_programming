print('{0}, {1}, {2}'format('a', 'b', 'c'))
print('{2}, {1}, {0}'.format(*'abc'))
print('hello world'.islower())
print('138383'.isnumeric())
print('1938383'.isdigit())
print('8383.8383883'.isdecimal())
print('hello world'.ispace())

'''
str.rstrip([chars])

Return a copy of the string with trailing characters removed. The chars argument is a string specifying the set of
characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars
argument is not a suffix; rather, all combinations of its values are stripped:

'''
print(' spacious '.rstrip())
print(' spacious '.lstrip())

print('1,2,3'.split(','))


print('ab c\n\nde fg\rkl\r\n'.splitlines()) # print('ab c\n\nde fg\rkl\r\n'.splitlines())


