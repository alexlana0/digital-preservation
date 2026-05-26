import sys
import typing


def main() -> None:
    args = sys.argv[1:]

    if len(args) == 0:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{args[0]}'")

    try:
        file: typing.IO[str] = open(args[0], 'r')
        file_content = file.read()

        print("---")
        print()

        print(file_content)

        print()
        print("---")

    except Exception as e:
        print(f"Error opening file '{args[0]}': {e}")
        return
    finally:
        file.close()
        print(f"File '{args[0]}' closed.")


if __name__ == "__main__":
    main()
