"""PPTX Expert version information."""

__version__ = "1.0.0"
__version_info__ = (1, 0, 0)
__author__ = "ppt-expert contributors"
__license__ = "MIT"

def get_version() -> str:
    """Get version string."""
    return __version__

def get_version_info() -> tuple:
    """Get version tuple."""
    return __version_info__

if __name__ == "__main__":
    print(f"PPTX Expert v{__version__}")
