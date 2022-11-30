from write_to_all_files import write_to_all_files


def create_custom_hooks(hooks: list[dict[str, str]]) -> None:
    for hook in hooks:
        for key, value in hook.items():
            write_to_all_files([(f"src/hooks/{key}.ts", value)])
