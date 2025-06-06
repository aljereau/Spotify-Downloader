#!/usr/bin/env python3
"""
Main entry point for the Spotify Downloader UI application.
"""

import sys
import os
from spotify_downloader_ui.app import run_app

def main():
    """Entry point for the application when installed as a package."""
    # Add application directory to path
    app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if app_dir not in sys.path:
        sys.path.insert(0, app_dir)
    
    # Run the application
    return run_app()

if __name__ == "__main__":
    sys.exit(main()) 