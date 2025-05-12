outfile = open("outTset.text","w",encoding="utf-8")

while True :
    outstr = input("내용 입력 : ")
    # 끝이라고 입력하면 종료
    if outstr == '끝':
        break
    outfile.writelines(outstr+"\n")


outfile.close()