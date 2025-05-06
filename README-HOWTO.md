# Spotify Downloader - How to Run

This guide explains how to run the Spotify Downloader application.

## Prerequisites

The following dependencies must be installed:

1. **Python 3.7 or higher**
2. **FFmpeg** - Automatically included in the setup
3. **yt-dlp** - Automatically installed with the application

## Running the Application

Two batch files are provided for easy use:

### Command-Line Interface (Recommended)

Run `run_spotify_downloader.bat` to use the command-line interface:

```
run_spotify_downloader.bat [options]
```

Examples:

```
# Download tracks from a Spotify playlist
run_spotify_downloader.bat https://open.spotify.com/playlist/your_playlist_id

# Download tracks with specific format
run_spotify_downloader.bat --format mp3 https://open.spotify.com/playlist/your_playlist_id

# Download tracks to a specific directory
run_spotify_downloader.bat -o "C:\Music" https://open.spotify.com/playlist/your_playlist_id

# Get help and see all options
run_spotify_downloader.bat --help
```

### Graphical User Interface (Experimental)

Run `run_spotify_downloader_gui.bat` to use the graphical interface:

```
run_spotify_downloader_gui.bat
```

Note: The GUI version may not work on all systems. If it fails, the command-line interface will be launched instead.

## Command-Line Options

```
Input Options:
  urls                  One or more Spotify playlist URLs
  -f, --file FILE       Text file containing Spotify playlist URLs (one per line)

Output Options:
  -o, --output-dir OUTPUT_DIR
                        Output directory for downloaded tracks (default: output)
  --format {mp3,m4a,opus,wav}
                        Audio format for downloaded tracks (default: mp3)

Download Options:
  --max-workers MAX_WORKERS
                        Maximum number of concurrent downloads (default: 4)
  --skip-existing       Skip downloading files that already exist
  --retry-count RETRY_COUNT
                        Number of retries for failed downloads (default: 3)

Utility Options:
  --check-deps          Check if required dependencies (yt-dlp, ffmpeg) are installed
```

## Troubleshooting

If you encounter issues:

1. Run the dependency check:
   ```
   run_spotify_downloader.bat --check-deps
   ```

2. Ensure FFmpeg is properly installed:
   ```
   ffmpeg -version
   ```

3. Update Python and all dependencies:
   ```
   pip install --upgrade -r requirements.txt
   ```

## Spotify Authentication

If you need to authenticate with Spotify, use the following command:

```
python -m spotify_downloader_ui.cli auth
```

This will guide you through the authentication process. 