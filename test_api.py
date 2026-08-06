"""Unit tests for ComickAPI."""
import pytest
from manga_downloader.core.api import ComickAPI


@pytest.mark.asyncio
async def test_search_returns_results():
    async with ComickAPI() as api:
        results = await api.search("One Piece", limit=3)
        assert isinstance(results, list)
        if results:
            assert results[0].manga.title


@pytest.mark.asyncio
async def test_extract_slug_from_url():
    from manga_downloader.utils.helpers import extract_slug
    assert extract_slug("https://comick.io/comic/solo-leveling") == "solo-leveling"
    assert extract_slug("https://comick.fun/comic/one-piece") == "one-piece"
    assert extract_slug("invalid-url") is None
