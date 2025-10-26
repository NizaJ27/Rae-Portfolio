import pytest
from tools.content_schema import Artwork, ImageRef, validate_artwork

def _valid_artwork():
    return Artwork(
        title="T", slug="t", year=2024, medium=["Ink"], dimensions="10x10",
        series=None, featured=True, order=1,
        images=[ImageRef(src="/images/t.jpg", alt="t")]
    )

def test_validate_artwork_ok():
    validate_artwork(_valid_artwork())

@pytest.mark.parametrize("title,slug", [("", "t"), ("T", ""), ("", "")])
def test_validate_artwork_requires_title_and_slug(title, slug):
    artwork = _valid_artwork()
    artwork.title = title
    artwork.slug = slug
    with pytest.raises(ValueError):
        validate_artwork(artwork)

def test_validate_artwork_requires_images():
    artwork = _valid_artwork()
    artwork.images = []
    with pytest.raises(ValueError):
        validate_artwork(artwork)

def test_validate_artwork_year_bounds():
    artwork = _valid_artwork()
    artwork.year = 1800
    with pytest.raises(ValueError):
        validate_artwork(artwork)
    artwork.year = 2200
    with pytest.raises(ValueError):
        validate_artwork(artwork)

def test_validate_artwork_image_fields():
    artwork = _valid_artwork()
    artwork.images = [ImageRef(src="", alt="test")]
    with pytest.raises(ValueError):
        validate_artwork(artwork)

    artwork.images = [ImageRef(src="/test.jpg", alt="")]
    with pytest.raises(ValueError):
        validate_artwork(artwork)

    # Test process images too
    artwork.images = [ImageRef(src="/test.jpg", alt="test")]
    artwork.process = [ImageRef(src="", alt="process")]
    with pytest.raises(ValueError):
        validate_artwork(artwork)
