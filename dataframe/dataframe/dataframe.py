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
        return self.data[:n]


    def tail(self, n: int = 5) -> list[list[float]]:
        """
        Returns the last n rows of the DataFrame. Defaults to last 5.
        :param n: Number of rows to return.
        :return: A list of the last n rows.
        """
        return self.data[-n:]
    
    
    def add_column(self, column_name: str, data: list[float]):
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
    
    
    def drop_column(self, column_name: str):
        """
        Drops a column from the DataFrame.
        :param col_name: The name of the column to drop.
        """
        if column_name not in self.columns:
            raise ValueError(f"Column '{column_name}' does not exist in the DataFrame")
        
        col_index = self.columns.index(column_name)
        self.columns.pop(col_index)
        for row in self.data:
            row.pop(col_index)


    def get_column(self, column_name: str) -> list[float]:
        """
        Returns the data for a specific column.
        :param column_name: The name of the column to retrieve.
        :return: A list of data for the specified column.
        """
        if column_name not in self.columns:
            raise ValueError(f"Column '{column_name}' does not exist in the DataFrame")
        
        col_index = self.columns.index(column_name)
        return [row[col_index] for row in self.data]
    
    
    def set_column(self, column_name: str, values: list[float]):
        """
        Sets the data for a specific column.
        :param column_name: The name of the column to set.
        :param values: A list of data to set for the specified column.
        """
        if column_name not in self.columns:
            raise ValueError(f"Column '{column_name}' does not exist in the DataFrame")
        
        if len(values) != len(self.data):
            raise ValueError("Length of values does not match number of rows in the DataFrame")
        
        col_index = self.columns.index(column_name)
        for i, value in enumerate(values):
            self.data[i][col_index] = value
    
    
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


    def concatenate_vertically(self, other):
        """
        Concatenates another DataFrame to the current DataFrame vertically (adding rows).
        
        :param other: Another DataFrame object to concatenate vertically.
        """
        if self.columns != other.columns:
            raise ValueError("DataFrames must have the same columns to concatenate vertically.")
        
        # Extend the data by adding rows from the other DataFrame
        self.data.extend(other.data)


    def concatenate_horizontally(self, other):
        """
        Concatenates another DataFrame to the current DataFrame horizontally (adding columns).
        
        :param other: Another DataFrame object to concatenate horizontally.
        """
        if len(self.data) != len(other.data):
            raise ValueError("DataFrames must have the same number of rows to concatenate horizontally.")
        
        # Extend the columns
        self.columns.extend(other.columns)
        
        # Extend each row with the corresponding row from the other DataFrame
        for i in range(len(self.data)):
            self.data[i].extend(other.data[i])
    
    
    def apply(self, func, axis, column):
        """
        Applies a function to each element of the entire DataFrame or to a specific column.
        
        :param func: A function to apply to each element.
        :param axis: If None, applies to all elements; if 0, applies to each column.
        :param column: Name of the column to apply the function to (if axis is None).
        """
        if axis is None and column is None:
            # Apply function to the entire DataFrame
            self.data = [[func(cell) for cell in row] for row in self.data]
        elif axis == 0:
            # Apply function to each column
            for col_index in range(len(self.columns)):
                for row_index in range(len(self.data)):
                    self.data[row_index][col_index] = func(self.data[row_index][col_index])
        elif column is not None:
            # Apply function to a specific column
            if column not in self.columns:
                raise ValueError(f"Column '{column}' does not exist in the DataFrame")
            col_index = self.columns.index(column)
            for row_index in range(len(self.data)):
                self.data[row_index][col_index] = func(self.data[row_index][col_index])
        else:
            raise ValueError("Invalid combination of axis and column")