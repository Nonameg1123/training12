a = input()
uv, uc, lv, lc, d, s = 0, 0, 0, 0, 0, 0

for i in a:
    if i.isalpha():  # Check if the character is an alphabetic letter
        if i.isupper():  # Check if the character is an uppercase letter
            if i in "AEIOU":  # Check if the character is an uppercase vowel
                uv += 1
            else:  # It must be an uppercase consonant
                uc += 1
        elif i.islower():  # Check if the character is a lowercase letter
            if i in "aeiou":  # Check if the character is a lowercase vowel
                lv += 1
            else:  # It must be a lowercase consonant
                lc += 1
    elif i.isdigit():  # Check if the character is a digit
        d += 1
    elif not i.isalnum():  # Check if the character is a special character
        s += 1

print(" uv - ", uv, "\n", "uc - ", uc, "\n", "lv - ", lv, "\n", "lc - ", lc, "\n", "d  - ", d, "\n", "s  - ", s)
