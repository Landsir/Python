# напечатать строку в одну линию -  C:\WINDOWS\System32\drivers\etc\nst

file1 = open("les7.txt", "r")

# while True:
#     line = file1.readline()
#     if not line:
#         break
#     print(line.strip())
# file1.close

text = file1.readline().split()
print(" ".join(text))
file1.close()