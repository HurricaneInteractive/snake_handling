class MyException(Exception):
    pass # all content inherited from Exception

try:
    print("I run")
    raise MyException("Custom Exception Message")
    print("I don't run")
except MyException as ex:
    print(ex)

raise MyException("Uncaught Exception Message")
