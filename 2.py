try:
    a = float(input())
    c = 100 / a
    print(c)
except (ZeroDivisionError):
    print("Нельзя делить на ноль")
except (ValueError):
    print("Нельзя делить на строки")
