import numpy as np

# 3x3 boyutunda rastgele bir matris oluştur
matrix = np.random.randint(1, 10, (3, 3))
print("Orijinal Matris:\n", matrix)

# Matrisin transpozunu al
transpose_matrix = matrix.T
print("\nTranspoze Matris:\n", transpose_matrix)

# Matrisin determinanını hesapla
det = np.linalg.det(matrix)
print("\nDeterminant:", det)

# Matrisin tersini hesapla (Eğer determinant 0 değilse)
if det != 0:
    inverse_matrix = np.linalg.inv(matrix)
    print("\nTers Matris:\n", inverse_matrix)
else:
    print("\nMatris tekil olduğu için ters alinamaz.")
