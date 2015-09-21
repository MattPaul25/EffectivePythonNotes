from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=20&green=',
                         keep_blank_values = True)
print(str(my_values))

#method one (the short handed method) hard to read but succint
red = int(my_values.get('red', [''])[0] or 0)
blue = int(my_values.get('blue', [''])[0] or 0)
green = int(my_values.get('green', [''])[0] or 0)

print('Red:     %r' % red)
print('Blue:    %r' % blue)
print('Green:   %r' % green)

#method two (the if else method) -- slightly less succint easier to read
red1 = my_values.get('red', [''])
red1 = int(red1[0]) if red1[0] else 0

blue1 = my_values.get('blue', [''])
blue1 = int(blue1[0]) if blue1[0] else 0

green1 = my_values.get('green', [''])
green1 = int(green1[0]) if green1[0] else 0

print('Red:     %r' % red1)
print('Blue:    %r' % blue1)
print('Green:   %r' % green1)


#method three (using full if statement with  a helper function

def get_first_int(values, key, default = 0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

green2 = get_first_int(my_values, 'green')
print("green " + str(green2))