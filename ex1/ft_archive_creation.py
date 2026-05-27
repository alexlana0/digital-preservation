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

        file.close()
        print(f"File '{args[0]}' closed.")
        print()

        lines = file_content.splitlines()
        new_lines = []

        for line in lines:
            line += "#"
            new_lines.append(line)

        new_file_content = "\n".join(new_lines)

        print("Transform data:")
        print("---")
        print()

        print(new_file_content)

        print()
        print("---")

        new_file_name = input("Enter new file name (or empty): ")

        if new_file_name == "":
            print("Not saving data.")
            return
        else:
            new_file: typing.IO[str] = open(new_file_name, 'w')
            new_file.write(new_file_content)
            new_file.close()
            print(f"Saving data to '{new_file_name}'.")
            print(f"Data saved in file '{new_file_name}'.")

    except Exception as e:
        print(f"Error opening file '{args[0]}': {e}")
        return


if __name__ == "__main__":
    main()
