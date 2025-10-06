from pytube import YouTube
import yt_dlp
import os
import re

def clean_youtube_url(url):
    """
    Clean YouTube URL by removing playlist and radio parameters.
    
    Args:
        url (str): The original YouTube URL
        
    Returns:
        str: Cleaned YouTube URL with only the video ID
    """
    try:
        # Extract video ID from various YouTube URL formats
        video_id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url)
        if video_id_match:
            video_id = video_id_match.group(1)
            return f"https://www.youtube.com/watch?v={video_id}"
        else:
            return url
    except Exception:
        return url

def download_with_pytube(video_url, output_path):
    """
    Try to download using pytube.
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()
        
        print(f"[PYTUBE] Downloading: {yt.title}...")
        video_stream.download(output_path=output_path)
        print(f"[PYTUBE] Download complete!")
        return True
    except Exception as e:
        print(f"[PYTUBE] Failed: {e}")
        return False

def download_with_ytdlp(video_url, output_path):
    """
    Try to download using yt-dlp.
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        ydl_opts = {
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'format': 'best[height<=1080]',
            'quiet': False,  # Set to True to reduce output
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            print(f"[YT-DLP] Title: {info.get('title', 'Unknown')}")
            print(f"[YT-DLP] Starting download...")
            ydl.download([video_url])
            print(f"[YT-DLP] Download complete!")
            
        return True
    except Exception as e:
        print(f"[YT-DLP] Failed: {e}")
        return False

def download_youtube_video(video_url, output_path="./output", prefer_ytdlp=True):
    """
    Downloads a YouTube video using either pytube or yt-dlp as fallback.

    Args:
        video_url (str): The URL of the YouTube video.
        output_path (str): The directory where the video will be saved.
        prefer_ytdlp (bool): If True, try yt-dlp first, else try pytube first.
    """
    try:
        os.makedirs(output_path, exist_ok=True)
        
        # Clean the URL to remove playlist parameters
        clean_url = clean_youtube_url(video_url)
        print(f"Original URL: {video_url}")
        print(f"Cleaned URL: {clean_url}")
        
        # Try both methods
        methods = [
            ("yt-dlp", download_with_ytdlp),
            ("pytube", download_with_pytube)
        ] if prefer_ytdlp else [
            ("pytube", download_with_pytube),
            ("yt-dlp", download_with_ytdlp)
        ]
        
        for method_name, method_func in methods:
            print(f"\nTrying {method_name}...")
            if method_func(clean_url, output_path):
                return True
            else:
                print(f"{method_name} failed, trying next method...")
        
        print("All download methods failed!")
        return False

    except Exception as e:
        print(f"An error occurred with URL {video_url}: {e}")
        return False

if __name__ == "__main__":
    
    # List of YouTube video URLs to download
    youtube_link_list = [
        'https://www.youtube.com/watch?v=49P7Oy3hQRE',
        'https://www.youtube.com/watch?v=_CK4O1_Bvxg',
        'https://www.youtube.com/watch?v=C4HeeSug3J8',
        'https://www.youtube.com/watch?v=l-FxY25lYzY',
        'https://www.youtube.com/watch?v=DaiCG20lyyY',
        'https://www.youtube.com/watch?v=y-brPQQhL_o',
    ]
    
    # Define the output directory
    output_directory = "./output"
    
    # Set prefer_ytdlp=True to try yt-dlp first (recommended)
    prefer_ytdlp = True
    
    # Download each video in the list
    successful_downloads = 0
    failed_downloads = 0
    
    for i, youtube_link in enumerate(youtube_link_list, 1):
        print(f"\n{'='*60}")
        print(f"Downloading video {i}/{len(youtube_link_list)}")
        print(f"{'='*60}")
        
        success = download_youtube_video(
            youtube_link, 
            output_path=output_directory,
            prefer_ytdlp=prefer_ytdlp
        )
        
        if success:
            successful_downloads += 1
        else:
            failed_downloads += 1
        
        print("-" * 60)
    
    print(f"\n{'='*60}")
    print(f"DOWNLOAD SUMMARY")
    print(f"{'='*60}")
    print(f"Successful downloads: {successful_downloads}")
    print(f"Failed downloads: {failed_downloads}")
    print(f"Total videos processed: {len(youtube_link_list)}")
    print(f"Success rate: {(successful_downloads/len(youtube_link_list)*100):.1f}%")