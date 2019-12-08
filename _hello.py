# import math
# import sys

# from os import rename

# third party package was sorted separately.
import requests

# # # print(sys.version)
# print(sys.executable)


# def greet(who_to_greet):
#     greeting = "Hello, {}".format(who_to_greet)
#     return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)

# example displays input using terminal.
# name = input("Your Name? ")
# print("Hello,", name)
