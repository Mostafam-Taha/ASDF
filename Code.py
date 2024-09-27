import random
import string
import json

# تعريف الحروف الممكنة
characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#"

# وظيفة لتوليد أرقام عشوائية مع تفضيل الأرقام البسيطة
def generate_weighted_random_number(max_value):
    # توليد رقم عشوائي مع تفضيل الأرقام الصغيرة
    return int(random.gauss(mu=0, sigma=max_value / 3)) % (max_value + 1)

# إنشاء 1000 كود عشوائي كل واحد مكون من 4 حروف
codes = [''.join(random.choices(characters, k=6)) for _ in range(10000)]

# تحويل الأكواد إلى تنسيق JSON مع أرقام عشوائية
codes_dict = {code: generate_weighted_random_number(90) for code in codes}

# كتابة الأكواد في ملف JSON
with open("random_codes.json", "w") as file:
    json.dump(codes_dict, file, indent=4)

print("تم إنشاء 1000 كود وحفظها في ملف random_codes.json")
