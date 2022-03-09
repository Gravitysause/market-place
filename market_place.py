import discord
import os
import dotenv

import data_base as mc

dotenv.load_dotenv()

# Discord CLient Key
token = os.getenv("token")


# The Bot
class MarketPlace(discord.Client):
    async def on_message(self, message):        
        # Prevents bot from responding to its self
        if message.author == self.user:
            return

        # check if bot is on
        elif message.content.startswith("$running"):
            await message.channel.send("Yes")

        elif message.content.startswith("$help"):
            await message.channel.send("~Hello, I'm MarketPlace! \n hi")

        # creates account
        if message.content.startswith("$create"):
            mc.createAccount(message.author.id)

            await message.channel.send(f"Creating an account for {message.author}")

        # prints balance
        elif message.content.startswith("$view"):
            try:
                balance = mc.viewBalance(message.author.id)
                
                await message.channel.send(f"{message.author} has ${balance}")

            except:
                await message.channel.send(f"{message.author} has no account.\n To create an account, Type in $create")

        # update balance
        elif message.content.startswith("$update"):
            mc.updateBalance(message.author.id, 40)

            await message.channel.send(f"updating {message.author}'s balance")


if __name__ == "__main__":
    try:
        discordClient = MarketPlace()
        discordClient.run(token)

    except:
        print("Invalid Bot Token")
