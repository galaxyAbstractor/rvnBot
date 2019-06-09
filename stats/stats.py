class StatService:
    def __init__(self, dbpool):
        self.dbpool = dbpool

    async def handle_message_stat(self, message):
        user_id = message.author.id
        channel_id = message.channel.id
        guild_id = message.channel.guild.id

        character_count = len(message.clean_content)
        word_count = len(message.clean_content.split())

        query = '''
            insert into message_stats (
                user_id,
                guild_id,
                channel_id,
                message_count,
                character_count,
                word_count
            )
            values (
                $1,
                $2,
                $3,
                1,
                $4,
                $5
            )
            on conflict (user_id, guild_id, channel_id) do update set 
                message_count = 
                    message_stats.message_count + 1,
                character_count =
                    message_stats.character_count + excluded.character_count,
                word_count = 
                    message_stats.word_count + excluded.word_count
                
        '''

        await self.dbpool.execute(query, user_id, guild_id, channel_id,
                                  character_count, word_count)
