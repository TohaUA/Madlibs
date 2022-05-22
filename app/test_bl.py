import asyncio

from app import bl
from app.constants import WordType


def test_get_words():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(bl.get_words())

    assert isinstance(result, dict)

    for word_type in (WordType.ADJECTIVE, WordType.VERB, WordType.NOUN):
        assert isinstance(result.get(word_type), str)


def test_get_words_mock(mocker):
    mocker.patch.object(bl, 'get_word', return_value='foo')
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(bl.get_words())

    assert isinstance(result, dict)

    for word_type in (WordType.ADJECTIVE, WordType.VERB, WordType.NOUN):
        assert isinstance(result.get(word_type), str)
