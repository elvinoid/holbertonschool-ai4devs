def incremental_rehash(items, bucket_count):
    """Small model of moving items into a resized hash table."""
    new_count = bucket_count * 2

    return {
        item: hash(item) % new_count
        for item in items
    }


def test_rehash_preserves_items():
    items = [
        "alpha",
        "beta",
        "gamma",
        "delta"
    ]

    result = incremental_rehash(items, 4)

    assert set(result) == set(items)


def test_rehash_uses_new_bucket_count():
    items = [
        "alpha",
        "beta",
        "gamma"
    ]

    result = incremental_rehash(items, 4)

    assert all(
        0 <= bucket < 8
        for bucket in result.values()
    )


def test_rehash_empty_collection():
    assert incremental_rehash([], 4) == {}