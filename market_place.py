import discord
import os
import dotenv

import data_base

dotenv.load_dotenv()

# Discord CLient Key
token = os.getenv("token")


# The Bot
class MarketPlace(discord.Client):
    async def on_message(self, message):
        # Prevents bot from responding to its self
        if message.author == self.user:
            return

        elif message.content.startswith("$running"):
            await message.channel.send("Yes")

        # creates account
        elif message.content.startswith("$create"):
            data_base.createAccount(message.author.id)

            await message.channel.send(f"Creating an account for {message.author}")

        # prints ballence
        elif message.content.startswith("$view"):
            balance = data_base.viewBalance(message.author.id)

            if balance == None:
                await message.channel.send(f"{message.author} doesn't have an account. \n to create an account, use $create")

            else: 
                await message.channel.send(f"{message.author} has ${balance}")


try:
    discordClient = MarketPlace()
    discordClient.run(token)

except:
    print("Invalid Bot Token")
