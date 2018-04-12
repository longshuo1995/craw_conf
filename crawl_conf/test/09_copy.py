import os

l = os.listdir(".")

for i in l:
    print(i)
    print("*" * 11)
    with open(i, 'rb') as f:
        temp = f.read()
    with open("/Volumes/longshuo/git_test/copy/%s" % i, "wb") as f:
        f.write(temp)
