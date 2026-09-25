def deposit(money):
    balance = 1000

    print (f"ยอดเริ่มต้น: {balance} บาท")

    try:
        money = float(input("จำนวนเงินที่ต้องการฝาก: "))

        if money <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")

        balance += money

    except ValueError as error:
        print(f"เกิดข้อผิดพลาด: {error}")

    else:
        print("เงินฝากสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {balance:.2f} บาท")

    finally:
        print("สิ้นสุดรายการฝากเงิน")

deposit(0)