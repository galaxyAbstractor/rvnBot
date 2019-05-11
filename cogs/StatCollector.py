from discord import TextChannel
from discord.ext import commands


class StatCollector(commands.cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_result = None

    async def on_message(self, message):
        if message.author == self.user:
            return

        if not isinstance(message.channel, TextChannel):
            return

    async def on_typing(self, channel, user, when):
        if user == self.user:
            return

        if not isinstance(channel, TextChannel):
            return

    async def on_raw_message_delete(self, payload):
        message = payload.cached_message

        return

    async def on_raw_bulk_message_delete(self, payload):
        messages = payload.cached_messages

        return

    async def on_raw_message_edit(self, payload):
        messages = payload.cached_messages

        return

    async def on_reaction_add(self, reaction, user):
        return

    async def on_reaction_remove(self, reaction, user):
        return

    async def on_member_join(self, member):
        return

    async def on_member_remove(self, member):
        return

    async def on_member_update(self, member):
        return

    async def on_user_update(self, user):
        return

    async def on_member_ban(self, guild, user):
        return

    async def on_member_unban(self, guild, user):
        return
