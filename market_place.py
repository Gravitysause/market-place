import discord
import os
import dotenv

import data_base as mc

dotenv.load_dotenv()

# Discord CLient Key
token = os.getenv("token")


# The Bot
class MarketPlace(discord.Client):
    def getPrice(self, message):
        newMessage = message.content.split()

        try:
            return int(newMessage[1])

        except:
            return 

    async def on_message(self, message):        

        ####################
        ## Debug Commands ##
        ####################

        # Prevents bot from responding to its self
        if message.author == self.user:
            return

        # check if bot is on
        elif message.content.startswith("$running"):
            await message.channel.send("Yes")

        elif message.content.startswith("$help"):
            await message.channel.send("$running is used to check if I'm running \n$create is used to create an account \n$view is used to view your account balance \n$update is used to update your balance")


        ##################
        ## Bot Commands ##
        ##################

        # creates account

        # TODO check if user has account 
        if message.content.startswith("$create"):
            mc.createAccount(message.author.id, str(message.author))

            await message.channel.send(f"Creating an account for {message.author}")

        try:
            # prints balance
            if message.content.startswith("$view"):
                    balance = mc.viewBalance(message.author.id)
                    
                    await message.channel.send(f"{message.author} has ${balance}")

            # update balance
            elif message.content.startswith("$update"):
                if type(self.getPrice(message)) == type(69):
                    mc.updateBalance(message.author.id, self.getPrice(message))
                    await message.channel.send(f"updating {message.author}'s balance")

            # donate cash to other user
            elif message.content.startswith("$donate"):
                pass

        except NameError:
            await message.channel.send(f"{message.author} has no account.\nTo create an account, Type in $create")

        except OverflowError:
            if self.getPrice(message) < 0:
                await message.channel.send(f"{self.getPrice(message)} is too low to update")

            elif self.getPrice(message) > 0:
                await message.channel.send(f"{self.getPrice(message)} is too high to update")


if __name__ == "__main__":
    try:
        discordClient = MarketPlace()
        discordClient.run(token)

    except:
        print("Invalid Bot Token")
