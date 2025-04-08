# c:/doit/mymod.py mysum(3,4)
import sys

sys.path.append("c:/doit")
import mymod

print(f"mymod.mysum(3,4) : {mymod.mysum(3,4)}")
