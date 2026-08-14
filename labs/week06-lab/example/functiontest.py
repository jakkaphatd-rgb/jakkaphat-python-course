""" 
เขียน FUNCTION แปลงหน่วยสกุลเงิน ที่สามารถแปลงเงินจาก
THB <-> USD .. 1 USD = 32 THB 

โดยใช้ชื้อและการใช้งาน
function convert_currency(100, "USD")

แสดงผลออกทางหน้าจอ
100 THB = 3.3 USD

และทดสอบการใช้งาน function ที่ตัวเองเขียนด้วย

"""

def convert_currency(amount, currency):
    """Converts currency between THB and USD"""
    rate = 32

    if currency.upper() == "USD":
        converted = amount / rate
        return f"{amount} THB = {converted:.2} USD"

    elif currency.upper() == "THB":
        converted = amount * rate
        return f"{amount} USD = {converted:.2f} THB" 

    else:
        return "Invaid currency. Use 'THB' or 'USD' "

    print("Currency Converter:")
    print(convert_currency(100, "USD"))
    print(convert_currency(3.13, "THB"))
    print(convert_currency(500, "USD"))
    print(convert_currency(10, "THB"))
    print()
