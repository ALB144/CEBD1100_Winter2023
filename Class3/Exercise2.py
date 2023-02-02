# number = input("enter your number")
# evaluation = number/10
# if evaluation = int:
#     print("multiple OK")

num = input("enter number")

if num.isnumeric():
    print("num")
    if int(num) % 10 == 0 and int(num) < 100:
        print("YES")
    else:
        print("NO, THE NUMBER IS NOT LESS THAN 100 AND MULTIPLE OF 10")
else:
    print("not a nom")

