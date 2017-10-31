def make_change(charged, paid):
    difference = paid - charged
    if difference < 0.00:
        print('Please provide enough money')
    elif difference == 0.00:
        print('No change')
    else:
        change = {}
        while (difference >= 50.00):
            if "fifties" in change:
                change["fifties"] += 1
            else:
                change["fifties"] = 1
            difference -= 50.00
        while (difference >= 20.00):
            if "twenties" in change:
                change["twenties"] += 1
            else:
                change["twenties"] = 1
            difference -= 20.00
        while (difference >= 10.00):
            if "tens" in change:
                change["tens"] += 1
            else:
                change["tens"] = 1
            difference -= 10.00
        while (difference >= 5.00):
            if "fives" in change:
                change["fives"] += 1
            else:
                change["fives"] = 1
            difference -= 5.00
        while (difference >= 1.00):
            if "ones" in change:
                change["ones"] += 1
            else:
                change["ones"] = 1
            difference -= 1.00
        while (difference >= 0.25):
            if "quarters" in change:
                change["quarters"] += 1
            else:
                change["quarters"] = 1
            difference -= 0.25
        while (difference >= 0.10):
            if "dimes" in change:
                change["dimes"] += 1
            else:
                change["dimes"] = 1
            difference -= 0.10
        while (difference >= 0.05):
            if "nickles" in change:
                change["nickles"] += 1
            else:
                change["nickles"] = 1
            difference -= 0.05
        while (difference >= 0.01):
            if "pennies" in change:
                change["pennies"] += 1
            else:
                change["pennies"] = 1
            difference -= 0.01
        print(change)
        return change


make_change(27.00, 100.00)
make_change(43.31, 100.00)