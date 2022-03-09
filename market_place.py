import discord
import os
import dotenv

from data_base import MongoClient as mc

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

        # creates account
        if message.content.startswith("$create"):
            mc.createAccount(message.author.id)

            await message.channel.send(f"Creating an account for {message.author}")

        # prints balance
        elif message.content.startswith("$view"):
            balance = mc.viewBalance(message.author.id)
            
            await message.channel.send(f"{message.author} has ${balance}")

        # update balance
        elif message.content.startswith("$update"):
            balance = mc.viewBalance(message.author.id)

            mc.updateBalance(message.author.id, 40)
            await message.channel.send(f"{message.author} has ${balance}")


if __name__ == "__main__":
    try:
        discordClient = MarketPlace()
        discordClient.run(token)

    except:
        print("Invalid Bot Token")
