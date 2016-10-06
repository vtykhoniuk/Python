import split_word


def test_split_word():
    assert sorted(['the', 'man', 'ran']) == \
        sorted(split_word.split("themanran", "the ran man".split()))

    assert sorted(['the', 'man', 'ran']) == \
        sorted(split_word.split("themanran", "i the ran man".split()))

    assert sorted(['i', 'love', 'dogs', 'John']) == \
        sorted(split_word.split("ilovedogsJohn", "i am a dogs lover love John".split()))

    assert sorted(['the', 'man']) == \
        sorted(split_word.split("themanran", "the clown man".split()))
