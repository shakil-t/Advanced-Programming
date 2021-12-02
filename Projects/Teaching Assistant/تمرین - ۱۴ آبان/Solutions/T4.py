
a = int(input())
t = input("C or F?")
if t == "C" or t == "c":
    ans = (a * 9/5) + 32
elif t == "F" or t == "f":
    ans = (a-32)*5/9

print (ans)
