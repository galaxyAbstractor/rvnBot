import asyncio
import datetime
import json
import sys
import traceback

import aiohttp
import asyncpg
import discord
from discord.ext import commands

with open('config.json', 'r') as f:
    config = json.load(f)

DB_URI = config["DB_URI"]
TOKEN = config["TOKEN"]
ADMINS = config["ADMINS"]
DEFAULT_PREFIX = config["DEFAULT_PREFIX"]
STARTUP_EXTENSIONS = config["STARTUP_EXTENSIONS"]

bot = commands.AutoShardedBot(
    command_prefix=commands.when_mentioned_or(DEFAULT_PREFIX),
    description="Hmmm")
bot.admins = ADMINS


@bot.event
async def on_ready():
    print('Logged in as', bot.user)
    print('id', bot.user.id)
    print('Running', discord.__version__)


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await bot.process_commands(message)


async def create_pool(uri, **kwargs):
    """
        Experimenting with setting up pool with init.
    """

    def converter(data):
        if isinstance(data, datetime.datetime):
            return data.__str__()

    def _encode_jsonb(data):
        return json.dumps(data, default=converter)

    def _decode_jsonb(data):
        return json.loads(data)

    extra_init = kwargs.pop('init', None)

    async def init(conn):
        await conn.set_type_codec('jsonb', schema='pg_catalog',
                                  encoder=_encode_jsonb, decoder=_decode_jsonb,
                                  format='text')
        if extra_init is not None:
            await extra_init(conn)

    return await asyncpg.create_pool(uri, init=init, **kwargs)


async def run():
    try:
        pool = await create_pool(DB_URI)
        print('Connected to postgresql server')
    except Exception as e:
        print('Could not set up postgresql')
        traceback.print_exc()
        return
    bot.session = aiohttp.ClientSession()
    bot.pool = pool
    bot.start_time = datetime.datetime.utcnow()
    try:
        await bot.start(TOKEN)
    except KeyboardInterrupt:
        await bot.logout()
    finally:
        loop.close()


if __name__ == "__main__":
    for extension in STARTUP_EXTENSIONS:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
