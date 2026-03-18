ch = "likh22"

is_alpha = True

for c in ch:
    if not (('a' <= c <= 'z') or ('A' <= c <= 'Z')):
        is_alpha = False
        break

if is_alpha:
    print("Alphabet")
else:
    print("Not an alphabet")