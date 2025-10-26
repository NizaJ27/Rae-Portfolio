from pathlib import Path
import textwrap
from tools.mdx_loader import parse_artwork_mdx

def test_parse_artwork_mdx(tmp_path: Path):
    mdx = textwrap.dedent("""\
    ---
    title: "Title"
    slug: "slug"
    year: 2024
    medium: ["Ink"]
    dimensions: "10x10"
    featured: true
    order: 1
    images:
      - src: "/images/a.jpg"
        alt: "A"
    ---
    Body
    """)
    mdx_file = tmp_path / "work.mdx"
    mdx_file.write_text(mdx)
    art = parse_artwork_mdx(str(mdx_file))
    assert art.title == "Title"
    assert art.images[0].src.endswith("a.jpg")
