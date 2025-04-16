import re

input_path = r"C:\Users\김민석\Desktop\result.txt"
output_path = r"C:\Users\김민석\Desktop\result_updated.txt"

pattern = re.compile(r"result/result_ratio(\d+)\.png")

with open(input_path, "r", encoding="utf-8") as f:
    content = f.read()

def replacer(match):
    num = int(match.group(1))
    if 1 <= num <= 600:
        return f"result/augmented6_check{num}.jpg"
    return match.group(0)

new_content = pattern.sub(replacer, content)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("✅ result/result_ratio501~600.png 경로를 C:/result/augmented6_checkxxx.jpg로 치환 완료.")
