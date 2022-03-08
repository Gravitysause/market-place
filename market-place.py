import discord
import os
import dotenv

import dataBase

dotenv.load_dotenv()

# Discord CLient Key
token = os.getenv("token")

class MarketPlace(discord.Client):
    async def on_message(self, message):

        # Prevents bot from responding to its self
        if message.author == self.user:
            return

        # creates account
        elif message.content.startswith("$create"):
            dataBase.createAccount(str(message.author), 100)

        # view account
        elif message.content.startswith("$view"):
            print("Viewing Account")

            await message.channel.send(f"{message.author} has a balence of {message.author}")


discordClient = MarketPlace()
discordClient.run(token)
