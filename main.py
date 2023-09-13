import discord
from discord import app_commands
from discord import ui

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False 

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #Checar se os comandos foram sincronizados 
            self.synced = True
        print(f"Entramos como {self.user}.")

client = client()
tree = app_commands.CommandTree(client)

@tree.command( name = 'teste', description='Testando') #Comando para execucao 
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"to on!", ephemeral = True) 

try:
    client.run('DISCORD API KEY')
except discord.errors.HTTPException:
  print("\n\n\nBLOCK BY RATE LIMIT\n")