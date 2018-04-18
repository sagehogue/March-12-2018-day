# Write a python script that figures out how to divvy up an amount of change
# into the fewest quarters, dimes, nickels, and pennies.

def change_in_cents():
    return input('What is the total change less than 100 cents.: ')

# def quarters(t):
#     return (int(t) // 25, int(t) % 25)
#
# def dimes(t):
#     return (int(t) // 10, int(t) % 10)
#
# def nickels(t):
#     return (int(t) // 5, int(t) % 5)

def foo(t, denom):
    return (int(t) // denom, int(t) % denom)


def find_change():
    total_change = change_in_cents()
    q, remainder = foo(total_change, 25)
    d, remainder = foo(remainder, 10)
    n, p = foo(remainder, 5)
    return 'You have {} quarters, {} dimes, {} nickels, {} pennies'.format(q, d, n, p)

print(find_change())
