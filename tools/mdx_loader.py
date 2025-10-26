import frontmatter
from .content_schema import Artwork, ImageRef

def parse_artwork_mdx(path: str) -> Artwork:
    post = frontmatter.load(path)
    fm = post.metadata
    images = [ImageRef(**x) for x in fm.get("images", [])]
    process = [ImageRef(**x) for x in fm.get("process", [])]
    return Artwork(
        title=fm["title"],
        slug=fm["slug"],
        year=int(fm["year"]),
        medium=list(fm.get("medium", [])),
        dimensions=fm.get("dimensions", ""),
        series=fm.get("series"),
        featured=bool(fm.get("featured", False)),
        order=int(fm.get("order", 0)),
        category=fm.get("category"),
        images=images,
        process=process,
        description_short=fm.get("descriptionShort"),
    )
