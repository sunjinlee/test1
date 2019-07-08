num1 = 21
if num1 % 3 == 0:
    print ("num1은 3의 배수다")
elif num1 % 7 == 0:
    print ("num1은 7의 배수다")
elif num1 % 3== 0 and num1 % 7 == 0:
    print ("num1은 3과 7의 배수다")
else:
    print("다시 입력하세요")
