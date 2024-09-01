class Matrix:
    """
    A class to represent a matrix.
    """

    data: list[list[float]]

    def __init__(self, data: list[list[float]]):
        """
        Constructs all the necessary attributes for the matrix object.
        """
        self.data = data

    def __str__(self):
        """
        String representation of the matrix.
        """
        return "\n".join(["\t".join(map(str, row)) for row in self.data])


    def __add__(self, other):
        """
        Add two matrices together.
        """
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same dimensions to be added.")

        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))])


    def __mul__(self, other):
        """
        Multiply a matrix by a scalar.
        """
        return Matrix([[self.data[i][j] * other for j in range(len(self.data[0]))] for i in range(len(self.data))])


    # TODO: Person 1 - Implement matrix outer product (__matmul__)

    # TODO: Person 2 - Implement matrix transposition (transpose)

    # TODO: Person 1 & 2 - Implement determinant calculation (determinant)
    # Either code together or have one person code and the other review
    # If coding together, use pair programming & co-author the commit (git commit -m "message" -m "Co-authored-by: name <email>")
    # If reviewing, leave comments on what you think can be improved

    # TODO: Person 1 & 2 - Implement inverse calculation (inverse)
    # Either code together or have one person code and the other review
    # ...

    # TODO: Person 3 - Implement a function that concatenates two matrices horizontally (hconcat)
    def hconcat(self, mat2):
        assert len(self.data) == len(mat2) #number of rows is the same
        for row_idx in range(len(self.data)):
            self.data[row_idx] = self.data[row_idx].extend(mat2[row_idx])
        return self.data

    # TODO: Person 3 - Implement a function that concatenates two matrices vertically (vconcat)
    def vconcat(self, mat2):
        assert len(self.data[0]) == len(mat2[0]) #number of columns is the same
        for row in mat2:
            self.data.append(row)
        return self.data

    # TODO: Person 3 & 4 - Implement matrix eigenvalues and eigenvectors (eigen)