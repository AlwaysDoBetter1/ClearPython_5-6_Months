"""
Quick check for the presence of an element in the dictionary, it happens quickly thanks to hashability
"""

voted = {}

def check_voted(name):
    if voted.get(name):
        print("kick them out")
    else:
        voted[name] = True
        print("let them vote!")

