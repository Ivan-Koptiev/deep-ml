import numpy as np

def rref(matrix):
    num_rows, num_cols = matrix.shape
    lead = 0
    matrix = matrix.astype(float)
    for r in range(num_rows):
        if lead >= num_cols:
            break

        i = r
        while i < num_rows and matrix[i, lead] == 0:
            i += 1

        if i == num_rows:
            lead += 1
            continue

        # Swap rows to bring a non-zero pivot to the current row
        matrix[[r, i]] = matrix[[i, r]]

        # Normalize the current row
        pivot_value = matrix[r, lead]
        matrix[r] /= pivot_value

        # Eliminate other rows
        for j in range(num_rows):
            if j != r:
                factor = matrix[j, lead]
                matrix[j] -= factor * matrix[r]

        lead += 1

    return matrix

def matrix_image(A):
	# Write your code here
	rref_form=rref(A)
	lead_cols=[]
	lead=0
	for i in range(len(rref_form[0])):
		found=False
		for j in range(len(rref_form)):
			if lead<len(rref_form) and np.abs(rref_