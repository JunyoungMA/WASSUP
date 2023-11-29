# coffee.py
coffee = 10
while True:
    money = int(input("돈을 넣으시오:"))
    if money == 300:
        print("커피 나옵니다")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피 나옵니다" % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피 안줌")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee ==0:
        print("커피가 품절되었습니다. 판매를 중지합니다.")
        break