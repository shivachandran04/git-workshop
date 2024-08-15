from pydantic import BaseModel, Field

class Matrix(BaseModel):

    data: list[list[float]] = Field(..., description="Matrix data")

    def __init__(self, data):
        """
        Initialize the Matrix object with a 2D list.
        :param data: 2D list representing the matrix.
        """
        self.data = data

    def __str__(self):
        """
        String representation of the matrix.
        """
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

    # TODO: Person 2 - Implement matrix addition (__add__)

    # TODO: Person 3 - Implement matrix multiplication (__mul__)

    # TODO: Person 4 - Implement matrix transposition (transpose)

    # TODO: Person 1 & 3 - Implement determinant calculation (determinant)

    # TODO: Person 2 & 4 - Implement inverse calculation (inverse)

    # STRETCH CHALLENGE TODO: Implement matrix power (__pow__)

    # STRETCH CHALLENGE TODO: Implement matrix eigenvalues and eigenvectors (eigen)