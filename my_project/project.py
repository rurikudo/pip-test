import argparse

def main(message):
    print(f"message: {message}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="TODO")
    parser.add_argument("-m", "--message", help='')
    args = parser.parse_args()
    main(args.message)