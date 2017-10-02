def just_letters(s):
    letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    new_str = ""
    for i in range(len(s)):
        if s[i] in letters:
            new_str += s[i]
    return new_str

print just_letters("!!!Let's hope ?!> << this works !? !?")