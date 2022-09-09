import discord,requests,ast
from discord.ext import commands 
from listofmuscles import muscledict


class My_Cog(commands.Cog, name='Workout'):
    def __init__(self, bot):
        self.bot = bot
            
    @commands.command(name="inspire", help="motivational quotes")
    async def inspire(self, ctx):
        r =requests.get('https://api.goprogram.ai/inspiration')
        dictionary = r.text
        dict1 = ast.literal_eval(dictionary)
        dict1.items()
        await ctx.send(f"{dict1['quote']} - {dict1['author']}")

    @commands.command(name="searchmuscles", help ="searches through muscles and shows workouts")
    async def searchmuscle(self, ctx,nameofmuscle):
        embed=discord.Embed(title=nameofmuscle, color=0xFF2B00)
        musclesjoined = '\n'.join(muscledict[nameofmuscle])
        embed.add_field(name="Exercise names", value=musclesjoined)
        await ctx.send(embed=embed)
        
    @commands.command(name="muscles", help="shows possible muscles to search")
    async def muscle(self, ctx):
        embed=discord.Embed(title="Muscles to search for: ", description = "abs\nlowerabs\nobliques\nupperabs\nlats\nrhomboids\nbiceps\ncalves\nchest\nlegs\nhamstrings\nquads\nlowerback\nshoulders\ndelts+traps\nrotatorcuff\ntriceps",
                    color=0xFF2B00)
        await ctx.send(embed=embed)
    
    @commands.command(name="1rm", help= "calculates one rep maxes")
    async def onerm(self, ctx, weight, reps):
        weight = int(weight)
        reps = int(reps)
        onerm = weight/(1.0278 - 0.0278 * reps)
        onerm = str(round(onerm, 2))
        embed=discord.Embed(title=onerm)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(My_Cog(bot))
                        