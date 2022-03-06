import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'insurance.csv')

def read_file():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        data = f.read().splitlines()
    return data


def main():
    data = read_file()
    print(data)
    

if __name__ == "__main__":
    raise SystemExit(main())