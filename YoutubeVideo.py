# 37th github project --> Youtube Video Downloader
print('----------Youtube Video Downloader----------')
import yt_dlp

def download(url, output_dir="downloads"):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",   # best quality video + audio
        "merge_output_format": "mp4",           # merged output as mp4
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("YouTube URL: ").strip()
    download(url)
    print("Done.")