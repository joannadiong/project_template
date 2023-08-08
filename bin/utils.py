from dataclasses import dataclass
from pathlib import Path


@dataclass()
class Filepaths:
    project_path = Path('.')
    path_raw = project_path / '..' / 'data' / 'raw'
    path_proc = project_path / '..' / 'data' / 'proc'


@dataclass()
class Constants:
    results = 'results.md'