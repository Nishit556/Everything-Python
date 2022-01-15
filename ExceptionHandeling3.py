def linus_interaction():
    assert ('linux' in sys.platform), "This code runs on linux only"
    print('Doing something.')

try:
    linus_interaction()
except:
    print("linux function was not executed")

try:
    linus_interaction()
except AssertionError as error:
    print("error")
    print("linux_interaction function was not executed")