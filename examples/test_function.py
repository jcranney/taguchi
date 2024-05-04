import os

a = float(os.environ["PARAM_A"])
b = float(os.environ["PARAM_B"])
c = float(os.environ["PARAM_C"])

print("annoying print message")

f = (a-3.5)**2 + (b-(-20))**2 + (c-1000)**2

print(f)