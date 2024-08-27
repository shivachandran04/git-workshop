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
    
    
    # More core functionalities like get_column, set_column, etc (potentially)
    
    
    def remove_duplicates(self):
        """
        Removes duplicate rows from the DataFrame.
        """
        # Use a set to track seen rows
        seen = set()
        unique_data = []
        for row in self.data:
            tuple_row = tuple(row)
            if tuple_row not in seen:
                seen.add(tuple_row)
                unique_data.append(row)
        self.data = unique_data

    def combine_columns(self, col1: str, col2: str, new_col: str, operation):
        """
        Combines two columns in the DataFrame based on a specified operation.
        
        :param col1: The name of the first column.
        :param col2: The name of the second column.
        :param new_col: The name of the new column to create.
        :param operation: A function that takes two arguments and returns a value (e.g., addition, multiplication).
        """
        if col1 not in self.columns or col2 not in self.columns:
            raise ValueError("Both columns must exist in the DataFrame")
        
        # Find the indices of the columns
        index1 = self.columns.index(col1)
        index2 = self.columns.index(col2)
        
        # Apply the operation and create the new column
        new_data = []
        for row in self.data:
            new_value = operation(row[index1], row[index2])
            new_data.append(row + [new_value])
        
        # Update the DataFrame
        self.data = new_data
        self.columns.append(new_col)
        
        
# Implement the following (these can be TODO's?... some may be difficult):
# 1. renaming columns
# 2. concatenating two tables (vertically, horizontally)
# 3. a mapping function (applying one transformation to each element of the 
#    entire dataframe, or to a particular column)
    
    