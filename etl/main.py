import argparse
import os
import sys

sys.path.append(os.path.dirname(__file__))

from extract import extract
from transform import transform
from load import load_to_db
from validate import validate_raw_data, validate_transformed_data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--limit", type=int, default=100)
    args = parser.parse_args()

    raw_df = extract(args.url)
    validate_raw_data(raw_df)

    transformed_df = transform(raw_df)
    validate_transformed_data(transformed_df)

    load_to_db(transformed_df, args.limit)


if __name__ == "__main__":
    main()