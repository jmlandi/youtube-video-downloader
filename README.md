# YouTube Video Downloader

A robust Python script to download YouTube videos using both `pytube` and `yt-dlp` libraries with automatic fallback. This hybrid approach ensures maximum reliability and compatibility with YouTube's frequent API changes.

## Features

- **Hybrid download system** - Uses both pytube and yt-dlp with automatic fallback
- **Automatic URL cleaning** - Removes playlist and radio parameters
- **High-quality downloads** - Downloads videos in the highest available resolution (up to 1080p)
- **Batch processing** - Download multiple videos from a list
- **Detailed progress tracking** - Shows download progress and statistics
- **Error handling** - Comprehensive error handling with helpful messages
- **Auto-creates directories** - Automatically creates output directories

## Prerequisites

- **Python 3.13** or higher
- Internet connection

## Installation

1. **Install Python 3.13**:
   - Download from [python.org](https://www.python.org/downloads/)
   - Or use a version manager like `pyenv`:
     ```bash
     pyenv install 3.13.0
     pyenv local 3.13.0
     ```

2. **Clone or download this repository** to your local machine

3. **Navigate to the project directory**:
   ```bash
   cd youtube-video-download
   ```

4. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   ```

5. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Edit the script** to add your video URLs:
   ```python
   # In script.py, modify the youtube_link_list
   youtube_link_list = [
       'https://www.youtube.com/watch?v=YOUR_VIDEO_ID',
       'https://www.youtube.com/watch?v=ANOTHER_VIDEO_ID',
       # Add more URLs as needed...
   ]
   ```

2. **Run the script**:
   ```bash
   python script.py
   ```

3. **Watch the magic happen**:
   - The script will automatically clean URLs (remove playlist parameters)
   - Try yt-dlp first (most reliable method)
   - Fall back to pytube if yt-dlp fails
   - Show detailed progress and final statistics

### Quick Example

For a single video download, check out `example.py`:
```bash
python example.py
```

This demonstrates how to use the download function programmatically.

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
├── script.py              # Main hybrid download script
├── example.py             # Usage example for single video downloads
├── requirements.txt       # Python dependencies
├── README.md             # This documentation
├── .python-version       # Python version specification (3.13)
├── output/               # Default output directory (created automatically)
└── .venv/                # Virtual environment (created during setup)
```

## Configuration

You can customize the download behavior by modifying the following variables in `script.py`:

- `youtube_link_list`: List of YouTube video URLs to download
- `output_directory`: The folder where videos will be saved (default: "./output")
- `prefer_ytdlp`: Set to `True` to try yt-dlp first (recommended), `False` for pytube first

### Advanced Configuration

For yt-dlp options, modify the `ydl_opts` dictionary in the `download_with_ytdlp` function:
```python
ydl_opts = {
    'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
    'format': 'best[height<=1080]',  # Max 1080p quality
    'quiet': False,  # Set to True to reduce output
}
```

## Function Reference

### `download_youtube_video(video_url, output_path="./output", prefer_ytdlp=True)`

Downloads a YouTube video using hybrid approach (tries both yt-dlp and pytube).

**Parameters:**
- `video_url` (str): The URL of the YouTube video
- `output_path` (str, optional): The directory where the video will be saved. Defaults to "./output"
- `prefer_ytdlp` (bool, optional): If True, try yt-dlp first. Defaults to True

**Returns:**
- `bool`: True if download successful, False otherwise

### `clean_youtube_url(url)`

Cleans YouTube URLs by removing playlist and radio parameters.

**Parameters:**
- `url` (str): The original YouTube URL

**Returns:**
- `str`: Cleaned YouTube URL with only the video ID

## Troubleshooting

### Common Issues

1. **"pytube not found" or "yt-dlp not found" error**: 
   - Make sure you've activated your virtual environment
   - Install requirements: `pip install -r requirements.txt`

2. **HTTP Error 400: Bad Request**: 
   - The hybrid script automatically handles this by trying yt-dlp first
   - URLs are automatically cleaned to remove problematic parameters
   - If both methods fail, the video might be restricted or private

3. **Python version issues**:
   - Ensure you're using Python 3.13 or higher
   - Check with: `python --version`
   - Use `pyenv` or similar tools to manage Python versions

4. **Download fails**: This could be due to:
   - Invalid YouTube URL
   - Video is private or restricted
   - Network connectivity issues
   - YouTube's anti-bot measures
   - Geographic restrictions

5. **Permission errors**: Make sure you have write permissions to the output directory

### Solutions

- **Update dependencies**: `pip install --upgrade pytube yt-dlp`
- **Try individual URLs**: Test with a single known-working video first
- **Check video accessibility**: Ensure the video is public and accessible in your region
- **Verify Python version**: Use Python 3.13 for best compatibility
- **Check network**: Ensure stable internet connection

## Legal Notice

This tool is for educational purposes only. Please respect YouTube's Terms of Service and copyright laws. Only download videos that you have permission to download or that are in the public domain.

## Dependencies

- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)**: Primary downloader - A robust, actively maintained YouTube downloader
- **[pytube](https://github.com/pytube/pytube)**: Fallback downloader - Lightweight, Pythonic YouTube video library

The hybrid approach uses yt-dlp as the primary method (more reliable) and falls back to pytube if needed, ensuring maximum download success rate.

## License

This project is open source. Feel free to modify and distribute as needed.

## Why This Hybrid Approach?

- **Reliability**: YouTube frequently changes their API, breaking single-method downloaders
- **Fallback Safety**: If one method fails, the other usually works
- **Best of Both Worlds**: yt-dlp's robustness + pytube's simplicity
- **Future-Proof**: Adapts to YouTube's changes automatically

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## Performance Notes

- **yt-dlp**: Generally more reliable but slightly slower
- **pytube**: Faster but more prone to breaking with YouTube updates  
- **Hybrid**: Best reliability with reasonable performance