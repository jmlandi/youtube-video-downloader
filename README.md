# YouTube Video Downloader

A simple Python script to download YouTube videos using the `pytube` library. This tool allows you to download videos in the highest available resolution.

## Features

- Download YouTube videos in the highest available resolution
- Automatically creates output directories if they don't exist
- Simple command-line interface
- Error handling for failed downloads

## Prerequisites

- Python 3.6 or higher
- Internet connection

## Installation

1. Clone or download this repository to your local machine
2. Navigate to the project directory:
   ```bash
   cd youtube-video-download
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open the `script.py` file in a text editor
2. Replace `"YOUR_YOUTUBE_VIDEO_URL_HERE"` with the actual YouTube video URL you want to download
3. (Optional) Modify the `download_directory` variable to change the output folder name
4. Run the script:
   ```bash
   python script.py
   ```

### Example

```python
# In script.py, replace this line:
youtube_link = "YOUR_YOUTUBE_VIDEO_URL_HERE"

# With your actual YouTube URL:
youtube_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

## File Structure

```
youtube-video-download/
├── script.py              # Main download script
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── output/               # Default output directory
└── downloaded_videos/    # Custom output directory (created when script runs)
```

## Configuration

You can customize the download behavior by modifying the following variables in `script.py`:

- `youtube_link`: The YouTube video URL to download
- `download_directory`: The folder where videos will be saved (default: "downloaded_videos")

## Function Reference

### `download_youtube_video(video_url, output_path="./output")`

Downloads a YouTube video to the specified path.

**Parameters:**
- `video_url` (str): The URL of the YouTube video
- `output_path` (str, optional): The directory where the video will be saved. Defaults to "./output"

**Returns:**
- None

**Raises:**
- Exception: If the download fails for any reason

## Troubleshooting

### Common Issues

1. **"pytube not found" error**: Make sure you've installed the requirements using `pip install -r requirements.txt`

2. **Download fails**: This could be due to:
   - Invalid YouTube URL
   - Video is private or restricted
   - Network connectivity issues
   - YouTube's anti-bot measures

3. **Permission errors**: Make sure you have write permissions to the output directory

### Solutions

- Try updating pytube to the latest version: `pip install --upgrade pytube`
- Verify the YouTube URL is correct and the video is publicly accessible
- Check your internet connection
- Try downloading a different video to test if the issue is video-specific

## Legal Notice

This tool is for educational purposes only. Please respect YouTube's Terms of Service and copyright laws. Only download videos that you have permission to download or that are in the public domain.

## Dependencies

- [pytube](https://github.com/pytube/pytube): A lightweight, Pythonic, dependency-free library for downloading YouTube videos

## License

This project is open source. Feel free to modify and distribute as needed.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.