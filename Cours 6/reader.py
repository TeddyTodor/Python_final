
def read():

    print ("READ - Started")

    with open("logs/test.log", "r") as file :
        test_log = print(file.read())

    with open("logs/error.log", "r") as file :
        error_log = print(file.read())
    return test_log, error_log