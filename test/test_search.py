from unsplash_get.unsplash_get import search, get_image

def test_search_type() -> None:
    """test search function"""
    urls = search('cherry')
    assert isinstance(urls, list), "urls should be list"
    assert len(urls) == 20, "urls should be len of 20"

def test_search_urls() -> None:
    """test search function"""
    urls = search('cherry')
    pattern = 'https://unsplash.com/photos/'
    for url in urls:
        assert url.startswith(pattern), "wrong url pattern"

def test_search_content() -> None:
    """test search function"""
    urls = search('cherry')
    results = []
    for url in urls:
        img = get_image(url)
        results.append((url, bool(img)))
    fail_counts = len([status for (url, status) in results if not status])
    correct_counts = len([status for (url, status) in results if status])
    assert fail_counts == 5, "5 urls should be failed"
    assert correct_counts == 15, "15 urls should be correct"
