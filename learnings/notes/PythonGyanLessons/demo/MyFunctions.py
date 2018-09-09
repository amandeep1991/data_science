class Animal:
    def h(self):
        pass

a1 = Animal()
a2 = Animal()
id(a1)
id(a2)

hrs = 9
def overtime():
    return 90 * hrs


def regular():
    return 90 * hrs


def calculate_pay(strategy, days):
    return strategy() * days


print(calculate_pay(overtime, 30))