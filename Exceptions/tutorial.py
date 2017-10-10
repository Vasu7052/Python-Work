
try :
    num = int(input("What is your fav number? "))
    c = 4/num
    print("ALL WELL")
except ZeroDivisionError :
    print("ZeroDivisionError")
except:
    print("ERROR")
finally:
    print("Exit")

