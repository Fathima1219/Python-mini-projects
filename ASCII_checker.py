# ASCII Value Checker
char = input("Enter a character: ")

print("ASCII value:", ord(char))
print("Next character:", chr(ord(char) + 1))
print("Previous character:", chr(ord(char) - 1))