# SPOTIFYMANAGER

## Description

SpotifyManager is a Python 3 library written to automate simple features on Spotify

## Installation (On work)

If you already have [Python3](http://www.python.org/) on your system you can install the library simply by downloading the distribution, unpack it and install in the usual fashion:

```bash
python3 setup.py install
```

You can also install it using a popular package manager with

```bash
pip3 install SpotifyManager
```

or

```bash
easy_install SpotifyManager
```

## Dependencies

- [Spotipy](https://github.com/plamere/spotipy) - spotify-account requires spotipy to be installed
- [Requests](https://github.com/kennethreitz/requests) - spotipy requires the requests package to be installed
- Spotify Premium - premium is required to use the library


## Quick Start

To get started, simply install spotify-account, create a spotifyAccount object and call methods:

```python
from spotify_manager import SpotifyManager
sm = SpotifyManager(SPOTIFY_USERNAME, SPOTIFY_CLIENT_ID, 
                                    SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI)

sm.play_song('eminem mockingbird')
# Mockingbird - Eminem is now running on your device

print(sm.get_current_song_info())
>>> {'name': 'Eminem - Mockingbird', 'uri': 'spotify:track:17baAghWcrewNOcc9dCewx'}, 
    'artists': {'all': 'Eminem', 'main': {'name': 'Eminem', 
    'uri': 'spotify:artist:7dGJo4pcD2V6oG8kP0tJRR'}}, 'album': {'name': 
    'Curtain Call (Deluxe)', 'uri': 'spotify:album:71xFWYFtiHC8eP99QB30AA'}, 
    'playlist': {'is_active': False, 'uri': None}}

sm.play_similar_from_current_artist()
# My Band - D12 is now running on your device, followed by a list of another 19 related songs (customizable)
```

