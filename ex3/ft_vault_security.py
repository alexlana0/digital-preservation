

def secure_archive(file_name: str, mode: str = "r", content: str = ""
                   ) -> tuple[True | False, str]:
    if mode == "r":
        try:
            with open(file_name, mode) as file:
                return (True, file.read())
        except Exception as e:
            return (False, str(e))
    elif mode == "w":
        try:
            with open(file_name, mode) as file:
                file.write(content)
                return (True, "Content successfully written to file")
        except Exception as e:
            return (False, str(e))
    else:
        return (False, "Invalid mode - try 'r' or 'w'")


def main() -> None:
    print("== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("nonexistent_file.txt", "r"))

    print("\nUsing 'secure_archive' to read from a inaccessible file:")
    print(secure_archive("/etc/master.passwd", "r"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("/etc/master.passwd", "r"))
