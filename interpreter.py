exp = input("Expression : ")
x, y, z = exp.split(" ")
nx = float(x)
ny = float(z)

if y=="+":
    s = nx + ny
    print(f"{s :.1f}")
if y=="-":
    s = nx - ny
    print(f"{s :.1f}")
if y=="*":
    s = nx * ny
    print(f"{s :.1f}")
if y=="/":
    s = nx / ny
    print(f"{s :.1f}")
