try:
    i = 0
    number = 10 / i
except ZeroDivisionError as error:
    print(error)
    number = 56
except (ZeroDivisionError, TypeError):
    number = 44
except ValueError:
    number = 67
else:
    print('no error -- else block')
finally:
    print('finally')
print(number)

# --output--
# division by zero
# finally
# 56
