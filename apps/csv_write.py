import pandas as pd
import os
from resources.data_base_general import csv_test_cases_result_path

def write_to_csv_old(filename, data, row, col):
    try:
        # Read the existing CSV file
        df = pd.read_csv(filename, header=None)
    except FileNotFoundError:
        # If the file does not exist, create an empty DataFrame
        df = pd.DataFrame()

    # Ensure the DataFrame has enough rows
    while len(df) <= row:
        df = pd.concat([df, pd.DataFrame([[None] * len(df.columns)])], ignore_index=True)

    # Ensure the DataFrame has enough columns
    while len(df.columns) <= col:
        df[len(df.columns)] = None

    # Write the data to the specified row and column
    df.iat[row, col] = data

    # Write the DataFrame back to the CSV file
    df.to_csv(filename, index=False, header=False)

def clear_csv(filename):
    # Write an empty DataFrame to the CSV file
    df = pd.DataFrame()
    df.to_csv(filename, index=False, header=False)

def write_to_csv(file_path, string_to_write, row, col):
    """
    Writes a string to a specific row and column in a CSV file using pandas.

    Args:
        file_path (str): The path to the CSV file.
        string_to_write (str): The string to write.
        row (int): The row index (0-based).
        col (int): The column index (0-based).
    """

    try:
        # Check if the file exists. If not, create an empty DataFrame.
        if os.path.exists(file_path):
            try:
                df = pd.read_csv(file_path, header=None)
            except pd.errors.EmptyDataError:  # Handle the empty file case.
                df = pd.DataFrame()
        else:
            df = pd.DataFrame()

        # Ensure the DataFrame is large enough. If not, append rows/columns.
        while df.shape[0] <= row:
            df = pd.concat([df, pd.DataFrame([([None] * df.shape[1])])], ignore_index=True)

        while df.shape[1] <= col:
            df[df.shape[1]] = None

        # Write the string to the specified row and column.
        df.iloc[row, col] = string_to_write

        # Write the DataFrame back to the CSV file.
        df.to_csv(file_path, index=False, header=False)  # index=False, header=False to maintain original structure

        print(f"String '{string_to_write}' written to row {row}, column {col} in '{file_path}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

def csv_file_init() -> None:
    """
    This function bla bla
    """
    clear_csv(csv_test_cases_result_path)
    write_to_csv(csv_test_cases_result_path, 'Test Cases Service 22', 0, 0)
