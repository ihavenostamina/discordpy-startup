import discord
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='&')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command(aliases=["s","summon"]) #connectやsummonでも呼び出せる
async def join(ctx):
    """Botをボイスチャンネルに入室させます。"""
    voice_state = ctx.author.voice

    if (not voice_state) or (not voice_state.channel):
        await ctx.send("先にボイスチャンネルに入っている必要があります。")
        return

    channel = voice_state.channel

    await channel.connect()
    print("connected to:",channel.name)


@bot.command(aliases=["disconnect","d"])
async def leave(ctx):
    """Botをボイスチャンネルから切断します。"""
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("Botはこのサーバーのボイスチャンネルに参加していません。")
        return

    await voice_client.disconnect()
    await ctx.send("ボイスチャンネルから切断しました。")


@bot.command(aliases=["c"])
async def chanchan(ctx):
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("chanchan.mp3")
    voice_client.play(ffmpeg_audio_source) 

@bot.command(aliases=["w"])
async def wind(ctx):
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("wind.mp3")
    voice_client.play(ffmpeg_audio_source)
    
@bot.command(aliases=["o"])
async def maru(ctx):
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("o.mp3")
    voice_client.play(ffmpeg_audio_source)    

@bot.command(aliases=["x"])
async def batu(ctx):
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("x.mp3")
    voice_client.play(ffmpeg_audio_source)
        
@bot.command(aliases=["b"])
async def bomb(ctx):
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("bomb.mp3")
    voice_client.play(ffmpeg_audio_source)
    
@bot.command(aliases=["e"])
async def ee(ctx):
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("ee.mp3")
    voice_client.play(ffmpeg_audio_source)
        
@bot.command(aliases=["k"])
async def kyaa(ctx):
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("kyaa.mp3")
    voice_client.play(ffmpeg_audio_source)

@bot.command(aliases=["h"])
async def hahaha(ctx):
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("hahaha.mp3")
    voice_client.play(ffmpeg_audio_source)

@bot.command(aliases=["f"])
async def fufufu(ctx):
    voice_client = ctx.message.guild.voice_client
    ffmpeg_audio_source = discord.FFmpegPCMAudio("fufufu.mp3")
    voice_client.play(ffmpeg_audio_source)

bot.run(token)
