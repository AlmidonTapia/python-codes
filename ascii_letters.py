# for paswords  of 4 digites type  string 52 x 52 x 52 x 52
# 78.000.000 de posibilidades.

from string import ascii_letters, digits, punctuation

for i in ascii_letters + digits + punctuation:
    for j in ascii_letters + digits + punctuation:
        for k in ascii_letters + digits + punctuation:
            for l in ascii_letters + digits + punctuation:
                print(i, j, k, l)