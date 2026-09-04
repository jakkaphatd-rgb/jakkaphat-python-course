# 1. รับค่า text จากผู้ใช้
# 2. รับค่าอักขระที่ต้องการค้นหาจากผู้ใช้
# 3. แสดงผลจำนวนของอักขระในข้อความ text
 
# ตัวอย่างหน้าจอ
# Insert your text: Boonchoo Jitupong
# Character to find: o
# 5 letters 'o' found in 'Boonchoo Jitupong
 
print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Insert your text: ")
char = input("Character to find: ")

# Your password is not strong
#
# Insert your password: Test@123
# Your password is strong
 
password = input("Innsert your password: ")
lenght = len(password)
words = password.split('@')
 
if len(words) > 1 and password . count('@')
    left = words[0].isalnum()
    right = words[1].isalnum()
else:
    left = False;
    right = False;
 
if lenght >= 8 and len(words) == 2 and left and right:
    print("Your password is strong!")
else:
    print("Your password is not strong!")