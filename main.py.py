import string as s
import random as r
splchar="!@#$%^&*()_"
pswd = r.sample(s.ascii_letters+s.digits+splchar,8)
pswd = "".join(pswd)
# pswd = r.shuffle(pswd)
print(pswd)
print("\n")
input("Press any key to exit.")