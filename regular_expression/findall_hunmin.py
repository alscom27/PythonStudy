import re

with open("hunmin.txt", "r", encoding="UTF-8") as hunmin:
    hantext = hunmin.read()
    exp1 = r"[가-힝]{5}"
    print("exp1: ", re.findall(exp1, hantext))

    exp2 = r"\s사[가-힝]*\s"
    print("exp2:", re.findall(exp2, hantext))
