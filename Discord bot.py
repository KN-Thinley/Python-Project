import discord

'''client = discord.Client()
n 
@client.event
async def on_ready() :
    print('Mini KN Thinley is now on')''' 

     
class thebot(discord.Client) :
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 997697548473094185
        
    async def on_ready(self) :
        print('ready')
    
    async def on_raw_reaction_add(self, payload) :
        """
        Give a role based on a reaction emoji
        """
        if payload.message_id != self.target_message_id :
            return
        
        guild = client.get_guild(payload.guild_id)
        
        if payload.emoji.name == '🥔' :
            role = discord.utils.get(guild.roles, name = "Potato Lover")
            await payload.member.add_roles(role)
        
        elif payload.emoji.name == '💩' :
            role = discord.utils.get(guild.roles, name = "Chocolate lover")
            await payload.member.add_roles(role)
        
        elif  payload.emoji.name == '🐵' :
            role = discord.utils.get(guild.roles, name = "Funky Monkey")
            await payload.member.add_roles(role)
        
    async def on_message(message) :
    
        if message.author == client.user :
            return
    
        if message.content == 'hello' :
            await message.channel.send('Hello, こんにちは。Mini KN Thinley is here, need help? and i do not bug anymore') 
    
        if message.content == 'so, has the bug been fixed now?' :
            await message.channel.send('Yes UwU, thanks for the maintainence, Admin')

        if message.content == 'why is it only the two of us?' :
            await message.channel.send('I do not have the answer but I am responding to you even though I am a Bot or maybe the others just do not have time to spend on us Admins LOLXD')

        if message.content == 'cool' :
            await message.add_reaction('\U0001F929')

    async def on_message_edit(before , after) :
        await before.channel.send (
        f'{before.author} edited a message \n'
        f'Before: {before.content} \n'
        f'After: {after.content}\n')
    
    
    async def on_reaction_add(reaction, user) :
        await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')

intents = discord.Intents.default()
intents.members = True
client = thebot(intents = intents)

client.run('OTk0MjI2MzM4NDk4MDg0ODc1.GYQZuc.gUW5_7j3Emo9JMyPzUgtBzfT24Kso6-3jY7aM0')

