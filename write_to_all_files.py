def write_to_file(file_name: str, content: str) -> None:
    file = open(file_name, "w")
    file.write(content)
    file.close()


def write_to_all_files(files: list[tuple[str, str]]) -> None:
    for file in files:
        write_to_file(file[0], file[1])
