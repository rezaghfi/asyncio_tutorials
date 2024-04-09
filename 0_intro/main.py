# import asyncio for use asyncio
import requests
# یکی سری پردازش ها محدود به پردازنده هستند و یکسری از آن ها محدود به ورودی و خروجی هستند
# CPU - bound VS I/O bound

# یک برنامه می نویسیم که درخواست به سایت گیت هاب می فرسته و هدر بسته ها رو در فایلی ذخیره کنیم.

# I/O bound
response = requests.get('https://github.com/rezaghfi')

#dictionary
#CPU - bound
items = response.headers.items()

#list
# CPU - bound
res_headers = [f"{key} : {value}" for key, value in items]

# I/O - bound
for item in items:
    print(item)
# I/O - bound
print("---------------------------------------")
for item in res_headers:
    print(item)

#print(type(res_headers))
# CPU - bound
formatted_headers = str(res_headers)

# I/O bound
with open("headers.txt","w") as file:
    file.write(formatted_headers)

formatted_headers = "\n".join(res_headers)
with open("headers.txt","a") as file:
    file.write(formatted_headers)