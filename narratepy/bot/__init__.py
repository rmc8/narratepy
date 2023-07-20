import os
import asyncio
import pathlib
import platform
from datetime import datetime
from collections import defaultdict, deque

import discord
from discord.ext import commands
from dotenv import load_dotenv

from .voice import Voice, NO_MP3
from .data_obj import VoiceSettings

ffmpeg_path = pathlib.Path("./ffmpeg").resolve()
os.environ["PATH"] += os.pathsep + str(ffmpeg_path)
load_dotenv(".env")

if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
intents = discord.Intents.all()
CMD_PREFIX: str = "?"
bot = commands.Bot(intents=intents, command_prefix=CMD_PREFIX)
queue_dict = defaultdict(deque)
v = Voice()


def play(vc, queue):
    if not queue or vc.is_playing():
        return
    source = queue.popleft()
    vc.play(source, after=lambda e: play(vc, queue))


def enqueue(vc, guild, source):
    queue = queue_dict[guild.id]
    queue.append(source)
    if not vc.is_playing():
        play(vc, queue)


@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}!")


@bot.event
async def on_message(message):
    print("---on_message_start---")
    print("#message.content:" + message.content)
    print("---on_message_end---")

    # mp3 path
    now = datetime.now()
    mp3_path: str = f"./voice/voice_{now:%Y%m%d_%H%M%S}.mp3"
    p = pathlib.Path(mp3_path)
    mp3_path_abs: str = str(p.resolve())

    # Cmd
    if message.content.strip().lower() == f"{CMD_PREFIX}join":
        await message.author.voice.channel.connect()
    elif message.content.strip().lower() == f"{CMD_PREFIX}bye":
        await message.guild.voice_client.disconnect()

    # Voice
    vs = VoiceSettings(voice=1, rate=150)
    display_name : str = message.author.display_name
    mp3_path: bool = v.create_mp3(
        display_name=display_name,
        text=message.content,
        mp3_path=mp3_path_abs,
        voice_settings=vs,
    )
    if mp3_path != NO_MP3 and not message.content.startswith(CMD_PREFIX):
        source = discord.FFmpegPCMAudio(mp3_path_abs)
        enqueue(
            vc=message.guild.voice_client,
            guild=message.guild,
            source=source,
        )
    await bot.process_commands(message)


async def run():
    async with bot:
        await bot.start(os.environ.get("DISCORD_TOKEN"))
