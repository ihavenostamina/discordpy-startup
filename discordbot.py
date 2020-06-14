import discord
from discord.ext import commands
import os

#discord
bot = commands.Bot(command_prefix="$")
token = os.environ['Njg1ODkzMDA0NjA2ODMyNjY2.XuaZhA.yQkWZ18qVzpO0YXXBPVycWvUby0']

if not discord.opus.is_loaded():
    discord.opus.load_opus("heroku-buildpack-libopus")

@bot.command(aliases=["connect","summon"]) #connectやsummonでも呼び出せる
async def join(ctx):
    """Botをボイスチャンネルに入室させます。"""
    voice_state = ctx.author.voice

    if (not voice_state) or (not voice_state.channel):
        await ctx.send("先にボイスチャンネルに入っている必要があります。")
        return

    channel = voice_state.channel

    await channel.connect()
    print("connected to:",channel.name)


@bot.command(aliases=["disconnect","bye"])
async def leave(ctx):
    """Botをボイスチャンネルから切断します。"""
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("Botはこのサーバーのボイスチャンネルに参加していません。")
        return

    await voice_client.disconnect()
    await ctx.send("ボイスチャンネルから切断しました。")


@bot.command(aliases=["chanchan","c"]v)
async def play(ctx):
    """指定された音声ファイルを流します。"""
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("Botはこのサーバーのボイスチャンネルに参加していません。")
        return

    if not ctx.message.attachments:
        await ctx.send("ファイルが添付されていません。")
        return

    await ctx.message.attachments[0].save("chanchan.mp3")

    ffmpeg_audio_source = discord.FFmpegPCMAudio("chanchan.mp3")
    voice_client.play(ffmpeg_audio_source)

    await ctx.send("再生しました。")

bot.run(token)
