# 홀짝 구분

num = int(input("숫자를 입력하세요: "))
# if num % 2 == 0:
#    print("짝수")
#else :
#    print("홀수")

# 중첩 if문
 
num = int(input("숫자를 입력하세요: "))

if num < 1000:
    if num < 100:
        print("100보다 작음")
    else:
        print("100보다 크고 1000보다 작습니다")
else:
    print("1000보다 큼")

