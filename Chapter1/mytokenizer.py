englishwords={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
s="Hello World!"

for char in s:
        lower_char_string=char.lower()
        if  lower_char_string  in englishwords:
         print(f"{lower_char_string}:{englishwords[lower_char_string]}")
        else:
             print(f"{lower_char_string} does not exist in dictionary")
            
    