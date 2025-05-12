# test.txt 파일을 읽어와서
# outTest 파일에 쓴다.

infile = open("C:/Users/user/Desktop/python/9week/test.txt", "r", encoding="utf-8")
outfile = open("outTest.text", "w", encoding="utf-8")

#파일 읽어서 쓰기
while True:
    strfile = infile.readline()
    if(strfile == ""): 
        break
    outfile.writelines(strfile)

infile.close()
outfile.close()