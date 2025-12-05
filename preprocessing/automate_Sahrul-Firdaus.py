import argparse
import pandas as pd
from pathlib import Path


def preprocess(input_csv: str, output_csv: str):
    df = pd.read_csv(input_csv)
    # Example preprocessing: drop non-numeric, fill na, standardize column names
    numeric = df.select_dtypes(include=['number']).copy()
    numeric = numeric.fillna(numeric.mean())
    # Save
    Path(output_csv).parent.mkdir(parents=True, exist_ok=True)
    numeric.to_csv(output_csv, index=False)
    print(f"Saved preprocessed dataset to {output_csv}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    preprocess(args.input, args.output)
