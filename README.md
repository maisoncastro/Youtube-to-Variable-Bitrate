# Youtube-to-Variable-Bitrate
This script allows you to convert YouTube videos to Variable Bitrates

## Requirements

- Python
- `yt-dlp` library
- `ffmpeg` (for audio extraction and format conversion)

## Installation

1. Install `yt-dlp`:
\```bash
pip install yt-dlp
\```

2. Ensure you have `ffmpeg` installed on your system. The installation process varies based on your operating system.

## Usage

1. Copy the script provided below into a file named `youtube_to_mp3.py`.
2. Replace `YOUR_YOUTUBE_VIDEO_URL_HERE` with the YouTube video URL you wish to download.
3. Run the script:
\```bash
python youtube_to_mp3.py
\```
4. The downloaded MP3 will be saved in the current directory with its title as the filename and `.mp3` as the extension.

## Notes

- The MP3 extraction can take some time depending on the video's length and the computer's hardware capabilities.
- Audio output will be in the same folder as script.
