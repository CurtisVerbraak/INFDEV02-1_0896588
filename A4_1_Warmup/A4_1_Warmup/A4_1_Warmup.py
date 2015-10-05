## warmup

## Fahrenheit > Celsius
fahrenheit = int(raw_input('Enter Fahrenheit: \n'))

celsius = (float(fahrenheit - 32) * 5/9)
celsius = round(celsius, 2)

print celsius, "celsius \n"

## Celsius > Kelvin
celsius = int(raw_input('Enter celcius: \n'))
kelvin = (float(celsius + 273.15))
if kelvin < 0:
    print "Kelvin: 0 is absolute zero"
else:
    print kelvin, "Kelvin \n"

## absolute value
number = raw_input('Enter a number: ')
number = float(number)
print('The absolute value is ' + str(abs(number)))
