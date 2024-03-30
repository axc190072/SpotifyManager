from setuptools import setup

setup(
    name='SpotifyManager',
    version='1.0',
    description='A Python 3 library written to automate simple features in Spotify',
    author="Anthony Chen",
    author_email="axc190072@utdallas.edu",
    install_requires=[
        'spotipy==2.4.4',
    ],
    packages=['spotify-account']
)
