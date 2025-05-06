# Spotify Downloader

A Python application with GUI for downloading and analyzing Spotify playlists.

## Features

- Extract track information from Spotify playlists
- Analyze track metadata including popularity, genres, and audio features
- Generate detailed reports with playlist analytics
- Modern Qt-based user interface
- Find "hidden gems" (lesser-known tracks) in playlists
- Export track lists and links

## Requirements

- Python 3.8+
- FFmpeg (for audio processing)
- Spotify API credentials

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/Spotify-Downloader.git
   cd Spotify-Downloader
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Spotify API credentials:
   - Create an application at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
   - Set environment variables or create a `.env` file:
     ```
     SPOTIFY_CLIENT_ID=your_client_id
     SPOTIFY_CLIENT_SECRET=your_client_secret
     SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
     ```

4. Install FFmpeg:
   - **Windows**: Download from [FFmpeg.org](https://ffmpeg.org/download.html) and add to PATH
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg` or equivalent

## Usage

### GUI Mode

Run the application with:
```bash
python -m spotify_downloader_ui.main
```

The interface allows you to:
1. Enter a Spotify playlist URL
2. Set output options
3. Process and analyze the playlist
4. View detailed results

### Command Line Mode

For CLI usage (advanced features):
```bash
python -m src.spotify_playlist_extractor --help
```

Example CLI commands:
```bash
# Process a single playlist
python -m src.spotify_playlist_extractor "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF"

# Find hidden gems with custom popularity range
python -m src.spotify_playlist_extractor "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF" --hidden-gems --min-pop=5 --max-pop=30
```

## Project Structure

- `src/` - Core functionality and CLI interface
- `spotify_downloader_ui/` - GUI implementation using PySide6/Qt

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 