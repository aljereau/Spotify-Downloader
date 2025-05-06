"""
Main application class for the Spotify Downloader UI.
"""

import sys
import logging
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QSettings, Qt

from spotify_downloader_ui.views.main_window import MainWindow
from spotify_downloader_ui.services.config_service import ConfigService
from spotify_downloader_ui.services.error_service import ErrorService

logger = logging.getLogger(__name__)

class SpotifyDownloaderApp:
    """Main application class for the Spotify Downloader UI."""
    
    def __init__(self):
        """Initialize the application."""
        # Set application information for QSettings
        QApplication.setApplicationName("Spotify Downloader UI")
        QApplication.setOrganizationName("SpotifyTools")
        QApplication.setApplicationVersion("0.1.0")
        
        # Create Qt application
        self.app = QApplication(sys.argv)
        
        # Set high DPI attributes (must be done before any widgets are created)
        self.app.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
        self.app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)
        
        # Initialize services
        self.config_service = ConfigService()
        self.error_service = ErrorService()
        
        # Apply settings
        self._apply_settings()
        
        # Create main window
        self.main_window = MainWindow(
            config_service=self.config_service,
            error_service=self.error_service
        )
        
        logger.info("Application initialized")
    
    def _apply_settings(self):
        """Apply application settings."""
        # Load theme settings
        settings = QSettings()
        theme = settings.value("appearance/theme", "light")
        if theme == "dark":
            # TODO: Apply dark theme stylesheet
            pass
        else:
            # TODO: Apply light theme stylesheet
            pass
    
    def run(self):
        """Run the application."""
        logger.info("Starting application")
        self.main_window.show()
        return self.app.exec()


def run_app():
    """Run the Spotify Downloader UI application."""
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("spotify_downloader_ui.log")
        ]
    )
    
    # Start application
    try:
        app = SpotifyDownloaderApp()
        return app.run()
    except Exception as e:
        logger.exception("Unhandled exception in application")
        return 1


if __name__ == "__main__":
    sys.exit(run_app()) 