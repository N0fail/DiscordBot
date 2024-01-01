from music_sources.youtube import YTDLSource


def add_commands(bot):
    @bot.command(name='play', help='Plays a song from YouTube')
    async def play(ctx, url):
        if not ctx.message.author.voice:
            await ctx.send("You are not connected to a voice channel")
            return

        channel = ctx.message.author.voice.channel
        if not ctx.voice_client:
            await channel.connect()

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {player.title}')

    @bot.command(name='stop', help='Stops the music and leaves the voice channel')
    async def stop(ctx):
        await ctx.voice_client.disconnect()
