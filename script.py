from pytube import YouTube
import os

def download_youtube_video(video_url, output_path="./output"):
    """
    Downloads a YouTube video to the specified path.

    Args:
        video_url (str): The URL of the YouTube video.
        output_path (str): The directory where the video will be saved.
                          Defaults to the current directory.
    """
    try:
        yt = YouTube(video_url)
        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()

        print(f"Downloading: {yt.title}...")
        video_stream.download(output_path=output_path)
        print(f"Download complete! Video saved to: {os.path.join(output_path, video_stream.default_filename)}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace with the actual YouTube video URL you want to download
    youtube_link = "YOUR_YOUTUBE_VIDEO_URL_HERE"
    
    # Specify the desired output directory (optional)
    download_directory = "downloaded_videos" 
    os.makedirs(download_directory, exist_ok=True) # Create directory if it doesn't exist

    download_youtube_video(youtube_link, download_directory)