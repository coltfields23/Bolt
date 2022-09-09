import discord,random,asyncio,aiohttp
from discord.ext import commands 
from googlesearch import search 
from jokeapi import Jokes


class My_Cog(commands.Cog, name='Fun'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="joke", help="random jokes")
    async def print_joke(self, ctx):
            j = await Jokes()
            joke = await j.get_joke() 
            if joke["type"] == "single":
                await ctx.send(joke["joke"])
            else:
                await ctx.send(joke["setup"])
                await ctx.send(joke["delivery"])
    
                    
    @commands.command(name="findajoke", help="find a random joke")
    async def search_joke(self, ctx, search):
            j = await Jokes()
            try:
                joke = await j.get_joke(search_string=search)
                if joke["type"] == "single":
                    await ctx.send(joke["joke"])
                else:
                    await ctx.send(joke["setup"])
                    await ctx.send(joke["delivery"])
            except KeyError:
                await ctx.send("sorry, couldn't find a joke with that in it")
                    
    @commands.command(name="dankmemes", help="random memes from r/dankmemes")
    async def dankmemes(self, ctx):
        embed = discord.Embed()
        
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 20)]['data']['url'])
                await ctx.send(embed=embed)

    @commands.command(help="searches through google")
    async def find(self, ctx,*, query):
    		author = ctx.author.mention
    		await ctx.channel.send(f"Here's your dumb link {author}")
    		async with ctx.typing():
    				for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
    						await ctx.send(j)
    				await ctx.send("Need anymore Info?")
def setup(bot):
    bot.add_cog(My_Cog(bot))
                    