from disturbia import distribute


def test_tally():
    generator = distribute([("five", 5), ("six", 6)])

    distribution = list(generator)

    assert len(distribution) == 11, "Length should be sum of all distributions"
    assert len([x for x in distribution if x == "five"]) == 5, "It should occur five times"
    assert len([x for x in distribution if x == "six"]) == 6, "It should occur six times"


def test_tally_for_single_distribution():
    distribution = distribute([("yes", 3)])

    assert list(distribution) == ["yes", "yes", "yes"], "Should have all (3) yeses"


def test_tally_for_no_distributions():
    distribution = distribute([])

    assert list(distribution) == [], "Should be an empty array"
