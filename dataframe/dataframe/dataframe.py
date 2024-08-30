from .series import Series

class DataFrame:
    """
    A class to represent a DataFrame, which is a collection of Series.
    """

    def __init__(self, data: list[Series]):
        """
        Initialize the DataFrame with a list of Series.

        :param data: A list of Series objects.
        """
        self.data = data
        self.columns = [series.name for series in data]
        self._validate()


    def _validate(self):
        """
        Validate that the series names are unique and all series have the same length.
        """
        # Check if all series have the same length
        if len(set(len(series.data) for series in self.data)) != 1:
            raise ValueError("All Series in the DataFrame must have the same length.")
        # Check if column names are unique
        if len(self.columns) != len(set(self.columns)):
            raise ValueError("Column names must be unique.")


    def __repr__(self) -> str:
        """Return a string representation of the DataFrame."""
        column_str = " | ".join(self.columns)
        rows_str = "\n".join(" | ".join(map(str, row)) for row in zip(*[series.data for series in self.data]))
        return f"{column_str}\n{rows_str}"


    def shape(self) -> tuple[int, int]:
        """
        Return the shape of the DataFrame (rows, columns).
        """
        return (len(self.data[0].data), len(self.columns))


    def head(self, n: int = 5) -> 'DataFrame':
        """
        Returns a new DataFrame with the first n rows.
        
        :param n: Number of rows to return.
        :return: A new DataFrame with the first n rows.
        """
        # TODO: Person 1 - Implement this function


    def tail(self, n: int = 5) -> 'DataFrame':
        """
        Returns a new DataFrame with the last n rows.

        :param n: Number of rows to return.
        :return: A new DataFrame with the last n rows.
        """
        # TODO: Person 2 - Implement this function


    def add_column(self, series: Series):
        """
        Add a new Series (column) to the DataFrame.
        
        :param series: The Series object to add as a new column.
        """
        # TODO: Person 1 - Implement this function


    def drop_column(self, column_name: str):
        """
        Drop a column from the DataFrame.

        :param column_name: The name of the column to drop.
        """
        # TODO: Person 2 - Implement this function


    def get_column(self, column_name: str) -> Series:
        """
        Returns the Series for a specific column.
        
        :param column_name: The name of the column to retrieve.
        :return: The Series object for the specified column.
        """
        # TODO: Person 1 - Implement this function


    def set_column(self, column_name: str, values: list[float]):
        """
        Set the data for a specific column.
        
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
        # TODO: Person 1 & 2 - Implement this function
        # Either code together or have one person code and the other review
        # ...   


    def concatenate_vertically(self, other: 'DataFrame'):
        """
        Concatenates another DataFrame to the current DataFrame vertically (adding rows).

        :param other: Another DataFrame object to concatenate vertically.
        """
        # TODO: Person 1 - Implement this function


    def concatenate_horizontally(self, other: 'DataFrame'):
        """
        Concatenates another DataFrame to the current DataFrame horizontally (adding columns).

        :param other: Another DataFrame object to concatenate horizontally.
        """
        # TODO: Person 2 - Implement this function


    def apply(self, func, column: str = None):
        """
        Applies a function to a specific column or all elements in the DataFrame.

        :param func: A function to apply to each element.
        :param column: Name of the column to apply the function to (optional).
        """
        # TODO: Person 1 & 2 - Implement this function
        # Either code together or have one person code and the other review
        # ...   
                
                