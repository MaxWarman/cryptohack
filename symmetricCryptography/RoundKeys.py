state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    output_matrix = []
    for i in range(len(s)):
        new_row = []
        for j in range(len(s[0])):
            new_row.append(s[i][j] ^ k[i][j])
        output_matrix.append(new_row)

    return output_matrix

def matrix2bytes(matrix):
    txt = ""
    for row in matrix:
        for num in row:
            txt += chr(num)
    return txt

print(matrix2bytes(add_round_key(state, round_key)))

###
### FLAG: crypto{r0undk3y}
###
