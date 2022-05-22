import aiohttp
import asyncio

from app.constants import WordType

URL = 'https://reminiscent-steady-albertosaurus.glitch.me/'


async def get_word(session: aiohttp.ClientSession, word_type: WordType) -> str:
    async with session.get(f'{URL}{word_type.value}') as resp:
        if resp.status == 200:
            resp = await resp.text()
            return resp.strip('"')
        else:
            # TODO something
            raise Exception('Unknown error')


async def get_words() -> dict[WordType:str]:
    async with aiohttp.ClientSession() as session:
        tasks = []
        for word_type in (WordType.ADJECTIVE, WordType.VERB, WordType.NOUN):
            tasks.append(asyncio.ensure_future(get_word(session, word_type)))

        words = await asyncio.gather(*tasks, return_exceptions=True)

        result = {}
        for idx, word_type in enumerate((WordType.ADJECTIVE, WordType.VERB, WordType.NOUN)):
            if isinstance(w := words[idx], str):
                result[word_type] = w
            else:
                # TODO something
                ...

        return result
