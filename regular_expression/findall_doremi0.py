import re

with open("doremisong.txt", "r") as file:
    mytext = file.read()
    exp1 = r"\s...\s"
    print("exp1:", re.findall(exp1, mytext))

    exp2 = r"([a-zA-z]+),"
    print("exp2", re.findall(exp2, mytext))
