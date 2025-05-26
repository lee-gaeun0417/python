def sumFunc(user):
    print(user+"형님. 두 숫자를 입력해주십쇼.")
    num1 = int(input("정수1 ==> "))
    num2 = int(input("정수2 ==> "))
    num3 = int(input("정수3 ==> "))
    hap = num1 + num2 + num3
    return hap

def calc(v1,v2,op):
    result = 0
    if op == '+':
        result = v1 + v2
    elif op == '-' :
        result = v1 - v2
    elif op == '*' :
        result = v1 * v2
    elif op == '/' :
        result = v1 / v2
    return result

op = input("계산 입력 (+, -, *, /)")
v1 = int(input("첫 번째 숫자 입력: "))
v2 = int(input("두 번째 숫자 입력: "))
value = calc(v1,v2,op)
print("## 계산기 :", v1, op, v2, "=", value)