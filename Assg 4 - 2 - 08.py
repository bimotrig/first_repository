def myFunc(p1=2, p2=2, p3=2):
    ret = p1 + p2 + p3
    return ret

print("call without parameters ==>", myFunc())
print("call with 1 parameter ==>", myFunc(1))
print("call with 2 parameters ==>", myFunc(1, 2))
print("call with 3 parameters ==>", myFunc(1, 2, 3))
