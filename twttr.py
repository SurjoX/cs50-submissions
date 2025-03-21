input = input("Input: ")
for char in input :
    if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
       input = input.replace(char,'')
print(f"Output: {input}")
