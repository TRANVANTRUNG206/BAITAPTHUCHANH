print("TRAN VAN TRUNG")
print("MSV: 24575202160133")
import re

text = input("Nhập văn bản: ")
words = re.findall(r'\w+', text)
if words:
    max_len = max(map(len, words))
    longest = list(dict.fromkeys(w for w in words if len(w) == max_len))
    print(f"Từ dài nhất ({max_len} ký tự): {', '.join(longest)}")
else:
    print("Không có từ nào.")
