# mi, km, ft, m
def to_mi(measurement, amount):
    if measurement == 'km':
        return amount * 1.60934
    elif measurement == 'ft':
        return amount / 5280
    elif measurement == 'm':
        return amount / 1609.34


def to_km(measurement, amount):
    if measurement == 'mi':
        return amount * 1.60934
    elif measurement == 'ft':
        return amount * 0.0003048
    elif measurement == 'm':
        return amount * 0.001


def to_ft(measurement, amount):
    if measurement == 'mi':
        return amount * 5280
    elif measurement == 'km':
        return amount * 3280.84
    elif measurement == 'm6':
        return amount * 3.28084


def to_m(measurement, amount):
    if measurement == 'mi':
        return amount * 1609.34
    elif measurement == 'km':
        return amount * 1000
    elif measurement == 'ft':
        return amount * 0.3048


def gather_information():
    from_meas = input('What measurement do you want to convert from?: ')
    amount = float(input('What is the amout you want to convert?: '))
    to_meas = input('What measurement do you wan to convert to?: ')
    return from_meas, to_meas, amount

print('Welcome to the super cool distance converter.')
while True:
    frm, to, amount = gather_information()
    if to == 'km':
        result = to_km(frm, amount)
    elif to == 'mi':
        result = to_mi(frm, amount)
    elif to == 'ft':
        result = to_ft(frm, amount)
    elif to == 'm':
        result = to_m(frm, amount)
    else:
        print("I don't understand that!")
        continue

    print("{} {} is {} {}".format(amount, frm, result, to))
    q = input('Whould you like to convert another measurement?: ')

    if q == 'n':
        print('Goodbye!')
        exit()
