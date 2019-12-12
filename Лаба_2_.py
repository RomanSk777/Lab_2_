m = int(input("  MENU:          \''Лаба №2\''  \n1) Кількість букв у тексті      \n2) Coртування слів  \n\n  \"Виберіть правильне меню!\""))

if m == 1:
    input_something = input("Enter your text:")
    d = {}
    for i in input_something:
        if i.isalpha():
            d[i] = d.get(i, 0) + 1
            
    for i in d:
        print (i, "=",d[i])
elif m == 2:
    message = input("Enter something: ")
    symbols = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    s_message = ""
    for letter in message:
        if letter not in symbols:
            s_message = s_message + letter
    s_message = s_message.split()
    s_message.sort()
    print("Sorted:" )
    for word in s_message:
        print(word)
else:
    print("??*??")
