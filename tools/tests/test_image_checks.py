from pathlib import Path
from tools.image_checks import all_paths_exist

def test_all_paths_exist(tmp_path: Path):
    (tmp_path / "x.jpg").write_text("x")
    assert all_paths_exist(str(tmp_path), ["x.jpg"])
    assert not all_paths_exist(str(tmp_path), ["x.jpg", "y.jpg"])
