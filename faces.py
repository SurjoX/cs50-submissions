def main():
    string=input()
    result=convert(string)
    print(result)

def convert(string):

    result1=string.replace(":)", "🙂").replace(":(","🙁")
    return result1
main()
