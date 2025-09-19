class Advanced:
    def ex51(self):
        money = float(input("Үндсэн мөнгөн дүнгээ оруулна уу (P): "))
        interestpercent = float(input("Жилийн хүүгийн хувийг оруулна уу (R): "))
        duration = int(input("Хугацааг жилээр оруулна уу (T):"))
        interest = (money*interestpercent*duration)/100
        print(f"Бодогдсон хүүгийн дүн: {interest} \n Нийт эцсийн дүн: {money+interest}")

    def ex52(self):
        distance = float(input("Зайг километрээр оруулна уу: "))
        print(f"{distance}км нь: \n {distance*1000} метр \n {distance*100000} сантиметр \n {distance*100000/2.54} инч-тэй тэнцүү.")

    def ex53(self):
        weight = float(input("Өөрийн жинг килограммаар оруулна уу: "))
        height = float(input("Өөрийн өндрийг сантиметрээр оруулна уу: "))
        print(f"Таны биеийн жингийн индекс (BMI): {weight/ (height**2)}")
    def ex54():
        aname = input("1-р барааны нэр: ")
        aprice = int(input(f"{aname}-ийн үнэ: "))
        bname = input("2-р барааны нэр: ")
        bprice = int(input(f"{bname}-ийн үнэ: "))
        cname = input("3-р барааны нэр: ")
        cprice = int(input(f"{cname}-ийн үнэ: "))
        overallprice = aprice+bprice+cprice
        print(f"--- ТАНЫ ТАЛОН --- \n {aname}: {aprice} \n {bname}: {bprice} \n {cname}: {cprice} \n -------------------- \n Нийт дүн: {overallprice} \n НӨАТ (10%): {overallprice*0.1} \n Эцсийн төлбөр: {overallprice+ (overallprice*0.1)}")
    def ex55():
        duration = int(input("Нийт хугацааг секундээр оруулна уу: "))
        print(f"{duration} секунд нь 1 цаг, 6 минут, 40 секундтэй тэнцүү.")