divisor = int(input("Please, insert a divisor: "))
try:
    dividend = int(input("Please, insert an integer dividend (different of 0, of course): "))
    result = divisor / dividend
except ValueError:
    print("The dividend must be an integer, bro...")
except ZeroDivisionError:
    print("I told you that the dividend MUST NOT be 0 (zero)!")
except ArithmeticError as ae:
    print("Ok, that's new. You managed to throw the following arithmetic error: ".format(ae))
except Exception as e:
    print("Wow, you are special. What the heck is ".format(e) + "? Please contact me <3")
else:
    print("The result of {} / {} is {}".format(divisor, dividend, result))
finally:
    print("That's it, thanks!")
