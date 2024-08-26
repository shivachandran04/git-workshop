class DataFrame:
    """
    A class to represent a DataFrame.
    """

    data: list[list[float]]
    columns: list[str]

    def __init__(self, data: list[list[float]], columns: list[str]):
        """
        Initialize the DataFrame with data and column names.
        
        :param data: A list of lists (2D array) representing the data.
        :param columns: A list of strings representing column names.
        """
        self.data = data
        self.columns = columns
        self._validate(data)


    def _validate(self):
        """
        Validate that the data is a rectangular 2D list and column names are unique.
        """
        # Check if all rows have the same length
        if not all(len(row) == len(self.data[0]) for row in self.data):
            raise ValueError("All rows in the data must have the same length.")
        # Check if column names are unique
        if len(self.columns) != len(set(self.columns)):
            raise ValueError("Column names must be unique.")
        
        
    def shape(self):
        """
        Return the shape of the DataFrame (rows, columns).
        """
        return len(self.data), len(self.columns)


    def add_column(self, column_name, data):
        """
        Add a new column to the DataFrame.
        
        :param column_name: Name of the new column.
        :param data: List of values for the new column.
        """
        if len(data) != len(self.data):
            raise ValueError("Length of new column data must match number of rows in DataFrame.")
        self.columns.append(column_name)
        for i, row in enumerate(self.data):
            row.append(data[i])
            
    
    def __repr__(self):
        """Return a string representation of the DataFrame."""
        column_str = " | ".join(self.columns)
        rows_str = "\n".join(" | ".join(map(str, row)) for row in self.data)
        return f"{column_str}\n{rows_str}"


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

    # TODO: Person 3 - Implement a function that concatenates two matrices vertically (vconcat)

    # TODO: Person 3 & 4 - Implement matrix eigenvalues and eigenvectors (eigen)