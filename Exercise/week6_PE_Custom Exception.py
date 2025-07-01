class ValueTooHighError(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "value cannot exceed 100"

def enter_number_below_100(num):
    if num > 100:
        raise ValueTooHighError

try:
    enter_number_below_100(int(input("enter number below 100: ")))
except ValueTooHighError as e:
    print(e)