x = input("")
total_e =  x.count("e")
x = x.split("e")

x.insert(1, "e" * (total_e * 2))
print(*x, sep="")
