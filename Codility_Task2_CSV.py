'''
Given Strings s and c String s represent a table in csv format where rows are separated by new line characters and
each row consists of one or more fields separated by comma's first row contains name of columns.
For example table below is represented by following string s = "id,name,age,act.,room,dep.\n1,jack,68,T,13,8,\n17,Betty,28,F,15,7".
String c is the name of column in the table described by s that contains only integers. Task is to find the maximum value in that column.In the example above ,for c = "age", the maximum value is 68
'''
'''
To solve this problem, we need to parse the CSV-formatted string s to extract the table data, identify the column specified by the string c, and find the maximum integer value in that column. Here is a step-by-step Python implementation to achieve this:

Parse the CSV String: Split the string by newline characters to separate the rows.
Extract Column Names: The first row contains the column names.
Identify the Target Column: Find the index of the target column specified by c.
Extract and Convert Values: For each row, extract the value in the target column, convert it to an integer, and keep track of the maximum value.
'''
def find_max_value_in_column(s, c):
    # Split the string into rows
    rows = s.split('\n')

    # Extract column names from the first row
    columns = rows[0].split(',')

    # Identify the index of the target column
    try:
        target_index = columns.index(c)
    except ValueError:
        return None  # Return None if the column does not exist

    # Initialize max_value
    max_value = float('-inf')

    # Iterate over each row starting from the second row
    for row in rows[1:]:
        if row.strip():  # Skip empty rows
            fields = row.split(',')
            try:
                # Convert the value to integer and update max_value if applicable
                value = int(fields[target_index])
                if value > max_value:
                    max_value = value
            except (ValueError, IndexError):
                continue  # Skip rows where the conversion fails or index is out of range

    # Return max_value if it was updated, else return None
    return max_value if max_value != float('-inf') else None


# Example usage:
s = "id,name,age,act.,room,dep.\n1,jack,68,T,13,8,\n17,Betty,28,F,15,7"
c = "age"
print(find_max_value_in_column(s, c))  # Output: 68

'''
Explanation:
Splitting Rows: The string s is split into rows using the newline character (\n).
Column Names: The first row (rows[0]) is split by commas to get the column names.
Finding Column Index: The index method finds the index of the target column name (c). If the column does not exist, the function returns None.
Iterating Through Rows: For each subsequent row:
The row is split by commas to get the fields.
The value in the target column is converted to an integer.
The maximum value is updated if the current value is greater than the current maximum.
Handling Errors: Rows with non-integer values or missing fields are skipped using a try-except block.
Return Result: The function returns the maximum value found, or None if no valid integers were found.
This implementation ensures robust handling of potential issues such as missing columns, non-integer values, and empty rows, providing a reliable solution to the problem.
'''