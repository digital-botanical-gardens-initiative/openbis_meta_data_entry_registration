import pandas as pd
import argparse

def transform_date_columns(input_csv, output_csv, date_columns):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(input_csv)

    # Convert specified columns to datetime
    for col in date_columns:
        if col in df.columns:
            try:
                df[col] = pd.to_datetime(df[col])
            except pd.errors.ParserError:
                print(f"Skipping column '{col}' as it contains non-datetime-like values.")

    # Iterate through each specified column name
    for col in date_columns:
        # Check if the column exists in the DataFrame and contains date-like values
        if col in df.columns and df[col].dtype == 'datetime64[ns, UTC]':
            # Convert datetime to the desired format (already in UTC)
            df[col] = df[col].dt.strftime('%Y-%m-%dT%H:%M:%S+00:00')
        else:
            # Handle non-standard datetime format and convert to UTC first
            df[col] = pd.to_datetime(df[col], errors='coerce', utc=True).dt.strftime('%Y-%m-%dT%H:%M:%S+00:00')

    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_csv, index=False)

def main():
    parser = argparse.ArgumentParser(description='Transform date-like columns in a CSV file.')
    parser.add_argument('input_file', help='Path to the input CSV file')
    parser.add_argument('output_file', help='Path to the output CSV file')
    parser.add_argument('date_columns', nargs='+', help='Names of columns to apply the transformation on')
    args = parser.parse_args()

    print(f"Input CSV: {args.input_file}")
    print(f"Output CSV: {args.output_file}")
    print(f"Date columns: {args.date_columns}")

    transform_date_columns(args.input_file, args.output_file, args.date_columns)
    print(f"Date-like columns transformed and saved to {args.output_file}")

if __name__ == '__main__':
    main()
