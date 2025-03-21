def main():
    t = input("What time is it ? ")
    ti = convert(t)
    if 7.0<=ti<=8.0 :
        print("breakfast time")
    elif 12.0<=ti<=13.0 :
        print("lunch time")
    elif 18.0<=ti<=19.0 :
        print("dinner time")
    else :
        print("don't eat")
def convert(ti):
    h, m = ti.split(":")
    mins = float(m)/60
    ti = float(h) + mins
    return ti
if __name__ == "__main__":
    main()
