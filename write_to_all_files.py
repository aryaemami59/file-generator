def write_to_file(file: str, content: str) -> None:
    f = open(file, "w")
    f.write(content)
    f.close()


def write_to_all_files(files: list[tuple[str, str]]) -> None:
    for f in files:
        write_to_file(f[0], f[1])
