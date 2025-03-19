import random

lchar1 = random.randint(97, 122)
lchar2 = random.randint(97, 122)
uchar3 = random.randint(65,90)
uchar4 = random.randint(65,90)
digit1 = random.randint(48,57)
digit2 = random.randint(48,57)
symbol1 = random.randint(33,47)
symbol2 = random.randint(33,47)

password =  list(f"{chr(lchar1)}{chr(lchar2)}{chr(uchar3)}{chr(uchar4)}{chr(digit1)}{chr(digit2)}{chr(symbol1)}{chr(symbol2)}")
random.shuffle(password)

final_shuffled_password = "".join(password)

print(final_shuffled_password)