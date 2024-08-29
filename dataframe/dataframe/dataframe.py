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
        
        
    def __repr__(self) -> str:
        """Return a string representation of the DataFrame."""
        column_str = " | ".join(self.columns)
        rows_str = "\n".join(" | ".join(map(str, row)) for row in self.data)
        return f"{column_str}\n{rows_str}"
        
        
    def shape(self) -> tuple[int, int]:
        """
        Return the shape of the DataFrame (rows, columns).
        """
        return (len(self.data), len(self.columns))


    def head(self, n: int = 5) -> list[list[float]]:
        """
        Returns the first n rows of the DataFrame. Defaults to first 5.
        :param n: Number of rows to return.
        :return: A list of the first n rows.
        """
        # TODO: Person 1 - Implement this function


    def tail(self, n: int = 5) -> list[list[float]]:
        """
        Returns the last n rows of the DataFrame. Defaults to last 5.
        :param n: Number of rows to return.
        :return: A list of the last n rows.
        """
        # TODO: Person 2 - Implement this function
    
    
    def add_column(self, column_name: str, data: list[float]):
        """
        Add a new column to the DataFrame.
        
        :param column_name: Name of the new column.
        :param data: List of values for the new column.
        """
        # TODO: Person 1 - Implement this function
    
    
    def drop_column(self, column_name: str):
        """
        Drops a column from the DataFrame.
        :param col_name: The name of the column to drop.
        """
        # TODO: Person 2 - Implement this function


    def get_column(self, column_name: str) -> list[float]:
        """
        Returns the data for a specific column.
        :param column_name: The name of the column to retrieve.
        :return: A list of data for the specified column.
        """
        # TODO: Person 1 - Implement this function
    
    
    def set_column(self, column_name: str, values: list[float]):
        """
        Sets the data for a specific column.
        :param column_name: The name of the column to set.
        :param values: A list of data to set for the specified column.
        """
        # TODO: Person 2 - Implement this function
    
    
    def remove_duplicates(self):
        """
        Removes duplicate rows from the DataFrame.
        """
        # TODO: Person 1 & 2 - Implement this function
        # Either code together or have one person code and the other review
        # If coding together, use pair programming & co-author the commit (git commit -m "message" -m "Co-authored-by: name <email>")
        # If reviewing, leave comments on what you think can be improved


    def combine_columns(self, col1: str, col2: str, new_col: str, operation):
        """
        Combines two columns in the DataFrame based on a specified operation.
        
        :param col1: The name of the first column.
        :param col2: The name of the second column.
        :param new_col: The name of the new column to create.
        :param operation: A function that takes two arguments and returns a value (e.g., addition, multiplication).
        """
        # TODO: Person 3 & 4 - Implement this function
        # Either code together or have one person code and the other review
        # ...    


    def concatenate_vertically(self, other):
        """
        Concatenates another DataFrame to the current DataFrame vertically (adding rows).
        
        :param other: Another DataFrame object to concatenate vertically.
        """
        # TODO: Person 3 - Implement this function


    def concatenate_horizontally(self, other):
        """
        Concatenates another DataFrame to the current DataFrame horizontally (adding columns).
        
        :param other: Another DataFrame object to concatenate horizontally.
        """
        # TODO: Person 4 - Implement this function
    
    
    def apply(self, func, axis, column):
        """
        Applies a function to each element of the entire DataFrame or to a specific column.
        
        :param func: A mapping function to apply to each element.
        :param axis: If None, applies to all elements; if 0, applies to each column.
        :param column: Name of the column to apply the function to (if axis is None).
        """
        # TODO: Person 3 & 4 - Implement this function
        # Either code together or have one person code and the other review
        # ...