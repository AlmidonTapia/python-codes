# for paswords  of 4 digites 10 x 10 x 10 x 10
#10.000 contraseñas posibles.
from string import digits

for i in digits:
    for j in digits:
        for k in digits:
            for l in digits:
                print(i, j, k, l)