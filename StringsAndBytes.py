#In python 3 youll need one method that takes a str or bytes and always returns str like the following:

def to_str(bytes_or_str): #converts a byte or string to a string
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

def to_byte(bytes_or_str): #converts a byte or a string to bytes (UTF-8 encoding)
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value




myval = to_byte('test')

#with open ('somefile.txt', 'wb') as f:
#   f.write('test') #This does not work due to the fact the 'test' string must be converted to bytes before placed in the txt file

myval = to_byte('test')

with open('somefile.txt', 'wb') as f:
    f.write(myval)

print(myval)