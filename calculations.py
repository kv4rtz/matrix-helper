import copy

class VectorMatrix:
	def __init__(self, entries: list[float]):
		self.entries = entries

class ThirdOrderMatrix:
	def __init__(self, entries: list[list[float]]):
		self.entries = entries
  
	def determinant(self) -> float:
		first_calculated = [
			self.entries[0][0] * self.entries[1][1] * self.entries[2][2],
			self.entries[0][1] * self.entries[1][2] * self.entries[2][0],
			self.entries[1][0] * self.entries[2][1] * self.entries[0][2]
		]
  
		second_calculated = [
			self.entries[0][2] * self.entries[1][1] * self.entries[2][0],
			self.entries[0][1] * self.entries[1][0] * self.entries[2][2],
			self.entries[0][0] * self.entries[1][2] * self.entries[2][1]
		]
  
		return sum(first_calculated) - sum(second_calculated)

	def gauss_method(self, vector: VectorMatrix):
		matrix = copy.deepcopy(self.entries)
		copy_vector = vector.entries.copy()

		for k in range(3):
			for i in range(k + 1, 3):
				if matrix[k][k] != 0:
					factor = matrix[i][k] / matrix[k][k]
				for j in range(k, 3):
					matrix[i][j] -= factor * matrix[k][j]
				copy_vector[i] -= factor * copy_vector[k]

		x = [0, 0, 0]
		for i in range(3 - 1, -1, -1):
			sum_ax = sum(matrix[i][j] * x[j] for j in range(i + 1, 3))
			if matrix[i][i] != 0:
				x[i] = (copy_vector[i] - sum_ax) / matrix[i][i]
				
   
		return {
			"x": round(x[0], 6),
			"y": round(x[1], 6),
			"z": round(x[2], 6),
		}
  
  
	def reverse_matrix_method(self, vector: VectorMatrix):
		det_A = self.determinant()

		A11 = self.entries[1][1] * self.entries[2][2] - self.entries[1][2] * self.entries[2][1]
		A12 = -(self.entries[1][0] * self.entries[2][2] - self.entries[1][2] * self.entries[2][0])
		A13 = self.entries[1][0] * self.entries[2][1] - self.entries[1][1] * self.entries[2][0]

		A21 = -(self.entries[0][1] * self.entries[2][2] - self.entries[0][2] * self.entries[2][1])
		A22 = self.entries[0][0] * self.entries[2][2] - self.entries[0][2] * self.entries[2][0]
		A23 = -(self.entries[0][0] * self.entries[2][1] - self.entries[0][1] * self.entries[2][0])

		A31 = self.entries[0][1] * self.entries[1][2] - self.entries[0][2] * self.entries[1][1]
		A32 = -(self.entries[0][0] * self.entries[1][2] - self.entries[0][2] * self.entries[1][0])
		A33 = self.entries[0][0] * self.entries[1][1] - self.entries[0][1] * self.entries[1][0]

		reversed_matrix = ThirdOrderMatrix([
			[A11, A21, A31],
			[A12, A22, A32],
			[A13, A23, A33]
		])

		result_matrix = []

		print(vector.entries)

		for i in range(3):
			result_matrix.append(reversed_matrix.entries[i][0] * vector.entries[0] + reversed_matrix.entries[i][1] * vector.entries[1] + reversed_matrix.entries[i][2] * vector.entries[2])

		print(result_matrix)

		return {
			"x": result_matrix[0] / det_A,
			"y": result_matrix[1] / det_A,
			"z": result_matrix[2] / det_A,
		}

	def cramer_method(self, vector: VectorMatrix):
		det_A = self.determinant()
	  
		results = {
			"x": None,
			"y": None,
			"z": None
		}
  
		for i in self.entries:
			matrix = copy.deepcopy(self.entries)
			if results.get('x') is None:
				matrix[0][0] = vector.entries[0]
				matrix[1][0] = vector.entries[1]
				matrix[2][0] = vector.entries[2]
				new_matrix = ThirdOrderMatrix(matrix)
				results["x"] = round(new_matrix.determinant() / det_A, 6)
			elif results.get('y') is None:
				matrix[0][1] = vector.entries[0]
				matrix[1][1] = vector.entries[1]
				matrix[2][1] = vector.entries[2]
				new_matrix = ThirdOrderMatrix(matrix)
				results["y"] = round(new_matrix.determinant() / det_A, 6)
			elif results.get('z') is None:
				matrix[0][2] = vector.entries[0]
				matrix[1][2] = vector.entries[1]
				matrix[2][2] = vector.entries[2]
				new_matrix = ThirdOrderMatrix(matrix)
				results["z"] = round(new_matrix.determinant() / det_A, 6)
    
		return results
