#!/usr/bin/env python3
import os
import sys

import json
from json.decoder import JSONDecodeError

from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106

from PIL import ImageFont

from threading import Thread

import sys
import spotipy
import spotipy.util as util

import configparser

# Accessing the config file, all values can be accessed like you would with a dictionary
config = configparser.ConfigParser()
config.read('config.txt')
credentialValues = config['Credentials']

client_id = credentialValues['client_id']
client_secret = credentialValues['client_secret']
redirect_uri = credentialValues['redirect_uri']
username = credentialValues['username']

scope = 'user-read-playback-state'


class Song:
    def __init__(self, trackName, artists, durationMs, progressMs, shuffleState, isPlaying):
        self.trackName = trackName
        self.artists = artists
        self.durationMs = durationMs
        self.progressMs = progressMs
        self.shuffleState = shuffleState
        self.isPlaying = isPlaying

    try:
        self.token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    except (AttributeError, JSONDecodeError):
        os.remove(".cache-{}".format(username))

    def reload(self):
        if self.token:
            sp = spotipy.Spotify(auth=token)

            try:
                playback = sp.current_playback()
                self.trackName = playback['']
                self.artists = playback['item']['artists'][0]['name']
                self.durationMs = playback['item']['duration_ms']
                self.progressMs = playback['progress_ms']
                self.shuffleState = playback['shuffle_state']
                self.isPlaying = playback['is_playing']
            except TypeError:
                print("Nothing is playing")
        else:
            print("Unable to retrieve current playback - Can't get token for ", username)

    def __str__(self):
        print("Track: ", self.trackName)
        print("Artist: ", self.artists)
        print("Duration_Ms: ", self.durationMs)
        print("Progress_Ms: ", self.progressMs)
        print("Shuffle_State: ", self.shuffleState)
        print("Is_Playing: ", self.isPlaying)


if __name__ == "__main__":
    try:
        cSong = Song()
    except KeyboardInterrupt:
        pass
