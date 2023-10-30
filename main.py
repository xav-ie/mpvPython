#!/usr/bin/env python3
import mpv
player = mpv.MPV(ytdl=True, log_handler=print, loglevel="debug")
player.play('https://www.youtube.com/watch?v=8ABVzmQb2MU')
# player.play('recording.mkv')

player.wait_until_playing()
player.wait_for_playback()
