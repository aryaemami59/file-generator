import sys


def create_leet_code_template(file_name: str) -> None:
    f = open(f"{file_name}.js", "w")
    f.write(
        "// Description:\n\n\n// Challenge:\n\n\n// Alternate method:\n\n\n// testing:\n\n\n")


if __name__ == "__main__":
    create_leet_code_template(sys.argv[1])
