from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ImageRef:
    src: str
    alt: str
    caption: Optional[str] = None

@dataclass
class Artwork:  # pylint: disable=too-many-instance-attributes
    title: str
    slug: str
    year: int
    medium: List[str]
    dimensions: str
    series: Optional[str]
    featured: bool
    order: int
    category: Optional[str] = None
    images: List[ImageRef] = field(default_factory=list)
    process: List[ImageRef] = field(default_factory=list)
    description_short: Optional[str] = None  # pylint: disable=invalid-name

def validate_artwork(artwork: Artwork) -> None:
    if not artwork.title or not artwork.slug:
        raise ValueError("title and slug are required")
    if artwork.year < 1900 or artwork.year > 2100:
        raise ValueError("year is out of range")
    if not artwork.images:
        raise ValueError("at least one image is required")
    for img in artwork.images + artwork.process:
        if not img.src or not img.alt:
            raise ValueError("image src and alt are required")
