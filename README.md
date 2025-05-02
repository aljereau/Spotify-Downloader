# Spotify Playlist Extractor

A powerful tool for extracting and analyzing track information from Spotify playlists, with a focus on discovering "hidden gems" - tracks with high potential but low popularity.

## Features

- **Extract Track Information**: Get detailed information about all tracks in a Spotify playlist
- **Multiple Playlist Processing**: Analyze multiple playlists in one go
- **Hidden Gems Analysis**: Discover lesser-known but high-quality tracks using a sophisticated scoring system
- **Spotify Playlist Creation**: Create new Spotify playlists from discovered hidden gems
- **Comprehensive Analytics**: Generate detailed analytics about tracks, artists, and popularity distribution
- **Multi-Market Support**: Handle playlists from different Spotify markets
- **Batch Processing**: Process playlists in batches with retry capability

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/spotify-playlist-extractor.git
   cd spotify-playlist-extractor
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your Spotify API credentials:
   ```
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   SPOTIFY_USERNAME=your_username
   SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
   ```

## Usage

### Basic Usage

Process a single playlist:
```bash
python src/spotify_playlist_extractor.py https://open.spotify.com/playlist/your_playlist_id
```

Process multiple playlists:
```bash
python src/spotify_playlist_extractor.py https://open.spotify.com/playlist/id1 https://open.spotify.com/playlist/id2
```

Process playlists from a file:
```bash
python src/spotify_playlist_extractor.py --file playlists.txt
```

### Hidden Gems Analysis

Generate a hidden gems report:
```bash
python src/spotify_playlist_extractor.py URL --hidden-gems
```

Customize hidden gems criteria:
```bash
python src/spotify_playlist_extractor.py URL --hidden-gems --min-pop=5 --max-pop=35 --min-score=25 --top-gems=20
```

### Playlist Creation

Create a Spotify playlist from hidden gems:
```bash
python src/spotify_playlist_extractor.py URL --hidden-gems --create-playlist
```

Customize the created playlist:
```bash
python src/spotify_playlist_extractor.py URL --hidden-gems --create-playlist --playlist-name "Amazing Underground Tracks" --playlist-description "My favorite undiscovered songs" --playlist-public
```

## How Hidden Gems Scoring Works

Tracks are scored on a 0-50 point scale based on several factors:

- **Popularity**: Lower popularity tracks get higher scores (0-20 points)
- **Artist Collaboration**: Tracks with multiple artists get a bonus (0-10 points)
- **Track Duration**: Extended tracks (5-9 minutes) get a bonus (0-10 points)
- **Release Type**: Focused releases (singles/EPs with fewer tracks) get a bonus (0-10 points)

## Output Structure

Each playlist gets its own folder with:
- `playlist_name_tracks.txt`: Detailed track information
- `playlist_name_links.txt`: Track links for easy sharing/playing
- `playlist_name_analytics.txt`: Analytics report with detailed metrics
- `playlist_name_hidden_gems_*.txt`: Hidden gems report (if requested)
- `Downloads/`: Directory for downloaded tracks (future feature)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Spotipy](https://github.com/plamere/spotipy) - The Python library for the Spotify Web API
- Spotify Web API for providing the data access 