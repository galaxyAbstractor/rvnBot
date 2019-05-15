from discord import TextChannel
from discord.ext import commands
from stats import StatService
from users import UserService


class StatCollector(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.stats = StatService(bot.pool)
        self.users = UserService(bot.pool)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if not isinstance(message.channel, TextChannel):
            return

        user = await self.users.fetch(message.author.id)


    @commands.Cog.listener()
    async def on_typing(self, channel, user, when):
        if user == self.bot.user:
            return

        if not isinstance(channel, TextChannel):
            return

    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload):
        message = payload.cached_message

        return

    @commands.Cog.listener()
    async def on_raw_bulk_message_delete(self, payload):
        messages = payload.cached_messages

        return

    @commands.Cog.listener()
    async def on_raw_message_edit(self, payload):
        messages = payload.cached_messages

        return

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        return

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        return

    @commands.Cog.listener()
    async def on_member_join(self, member):
        return

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        return

    @commands.Cog.listener()
    async def on_member_update(self, member):
        return

    @commands.Cog.listener()
    async def on_user_update(self, user):
        return

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        return

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        return


def setup(bot):
    bot.add_cog(StatCollector(bot))
