#!/usr/bin/env python3
"""
YouTube Video Downloader - Example Usage

This example shows how to use the YouTube video downloader script.
Simply modify the URLs list and run the script.
"""

from script import download_youtube_video

if __name__ == "__main__":
    # Example: Download a single video
    single_video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    
    print("=== Single Video Download Example ===")
    success = download_youtube_video(single_video_url, output_path="./downloads")
    
    if success:
        print("✅ Video downloaded successfully!")
    else:
        print("❌ Video download failed!")
    
    print("\n" + "="*50)
    print("💡 To download multiple videos, edit the youtube_link_list in script.py")
    print("💡 The hybrid approach tries yt-dlp first, then pytube as fallback")
    print("💡 Videos are automatically saved to the ./output directory")