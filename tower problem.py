
def tower(n,s,temp,d):
    if n == 1:
        print(f"move the 1 disk from {s} to {d}")
        return
    tower(n-1,s,d,temp)
    print(f"move the {n} disk from {s} to {d}")
    tower(n-1,temp,s,d)
print(tower(n=3,s="A",temp="B",d="C"))
