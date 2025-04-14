# 반복문
# for i in range(5,10,2):
#    print(i, " 파이썬은 재밌습니다. ^^")

# 차례대로 숫자 출력
# for o in range(51, 101 , 3):
#     print(o, end=" ")

#실습 1 팩토리얼 계산기 ( 1부터 N까지 곱)
# N= 5
# res = 1
# for q in range(1, N + 1, 1):
#     res= res * q
# print(res)  #120

# 연습 1
# 1000 - 2000 사이에서 홀수의 합을 구하는 프로그램
#hap = 0
#res = 0
#for i in range(1001, 2001, 2):
#    hap += i
#print("1000에서 200 사이의 홀수의 합", hap)

# 중첩 for문
#for i in range(0,3,1):
#    for k in range(0,2,1):
        #print("i: ",i," k:",k)


#실습 2 (2-9단 구구단 계산기)
# for num1 in range(2,10,1):   #단
#     print("------ 구구단", num1, "단 ------" )
#     for num2 in range(1,10,1): #곱해지는 수
#         print(num1, "X", num2, "=\t", num1*num2)


#while문
#while( True ):
#    num1 = int(input(" 숫자 1 ==>"))
#    num2 = int(input(" 숫자 2 ==>"))
#    res = num1 + num2
#    print(num1, "+", num2, "=", num1 + num2)

#hap = 0
#res = 0
#while( True ):
    #num1 = int(input(" 숫자 1 ==>"))
    # num1이 0이면 반복문 종료
    #if num1 == 0:
        #break
    #num2 = int(input(" 숫자 2 ==>"))
    #print(num1, "+", num2, "=", num1 + num2)

#연습 2
# 1부터 100까지 더하되 3, 4의 배수는 더하지 않음
res = 0
for i in range(1, 101, 1):
    if i % 4 == 0: 
        continue
    elif i % 3 == 0:
        continue
    res = res +i
print(res)