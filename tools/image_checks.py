from typing import Iterable
from pathlib import Path

def all_paths_exist(root: str, rel_paths: Iterable[str]) -> bool:
    base = Path(root)
    return all((base / p).exists() for p in rel_paths)
