from typing import TypedDict, NotRequired, List


class ConfigOverride(TypedDict):
    excludedFiles: NotRequired[str | List[str] | None]
    files: str | List[str]
