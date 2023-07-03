# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?


matrix1 = [
    ["a","b","c","d","e"],
    ["f","g","h","i","l"],
    ["m","n","o","p","q"],
    ["r","s","t","u","v"],
    ["z","j","x","y","ab"]
]

cr = "\n"

print(f"Range di 1: {range(1)}")


def rotate_submatrix(matrix, subindex):
    #print(f"{cr}Submatrix Before rotate: {matrix} - subindex: {subindex}{cr}")
    n = len(matrix)
    sub_n = n-2*subindex
    #print(f"Submatrix sub_n = {sub_n} - subindex = {subindex}")
    temp_value = [val for val in matrix[subindex][subindex:len(matrix1)-subindex]]
    #print(f"Submatrix: Temp value: {temp_value}")
    for j in range(sub_n-1):
        #print(f"J = {j} - range = {range(sub_n-1)} - n = {n}")

        matrix[subindex][n-1-subindex-j] = matrix[j+subindex][subindex]
        #print(f"Matrice dopo submatrix step1 [{subindex}][{n-1-subindex-j}] <- [{j+subindex}][{subindex}] : {matrix}")
        
        matrix[j+subindex][subindex] = matrix[n-1-subindex][j+subindex]
        #print(f"Matrice dopo submatrix step2 [{j+subindex}][{subindex}] <- [{n-1-subindex}][{j+subindex}]: {matrix}")
        
        matrix[n-1-subindex][j+subindex] = matrix[n-1-j-subindex][n-1-subindex]
        #print(f"Matrice dopo submatrix step3 [{n-1-subindex}][{j+subindex}] <- [{n-1-j-subindex}][{n-1-subindex}]: {matrix}")
        
        #print(f"Submatrix: J = {j} - Inserting last value: {temp_value[n-1-j-2*subindex]} in position: [{n-1-j-subindex}][{n-1-subindex}]")
        matrix[n-1-j-subindex][n-1-subindex] = temp_value[n-1-j-2*subindex] 
        #print(f"Matrice dopo submatrix step4: {matrix}")
        
    #print(f"Matrice dopo submatrix con subindex: {subindex} : {matrix}")
    #return matrix
                         

def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        #print(f"{cr}{cr}New cycle with subindex={i}")
        rotate_submatrix(matrix, i)
        #print(f"Matrix after index i: {i}")
    return matrix

print(f"{rotate_matrix(matrix1)}")