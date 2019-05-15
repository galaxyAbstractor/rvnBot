class UserService:
    def __init__(self, dbpool):
        self.dbpool = dbpool

    async def fetch(self, discord_id):
        user = await self.dbpool.fetchval('''
            select * from users where discord_user_id = $1
        ''', discord_id)

        if not user:
            await self.dbpool.execute('''
                    insert into users (discord_user_id) values ($1)
                ''', discord_id)


class User:
    def __init__(self):
        self.id = ""
        self.discordId = ""
