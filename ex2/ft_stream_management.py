import sys
import typing


def main() -> None:
    args = sys.argv[1:]

    if len(args) == 0:
        print("Usage: ft_stream_management.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
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

    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{args[0]}': {e}\n")
        return

    lines = file_content.splitlines()
    new_lines = []

    for line in lines:
        new_lines.append(line + "#")

    new_file_content = "\n".join(new_lines)

    print("Transform data:")
    print("---")
    print()

    print(new_file_content)

    print()
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()

    new_file_name = sys.stdin.readline().strip()

    if new_file_name:
        sys.stdout.write(f"Saving data to '{new_file_name}'.\n")
        sys.stdout.flush()
        try:
            new_file: typing.IO[str] = open(new_file_name, 'w')
            new_file.write(new_file_content)
            new_file.close()
            print(f"Data saved in file '{new_file_name}'.")
        except Exception as e:
            sys.stderr.write(f"[STDERR] Error opening file '{new_file_name}':"
                             f"{e}\n")
            sys.stderr.flush()
            print("Data not saved.")


if __name__ == "__main__":
    main()
