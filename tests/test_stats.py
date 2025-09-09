from ship0.stats import mean_length

def test_mean_length_basic():
    items = ["abc", "abcd", "a"]
    m = mean_length(items)
    assert 2.6 < m < 2.7  # 8/3
