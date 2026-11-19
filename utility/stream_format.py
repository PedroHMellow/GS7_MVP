from yt_dlp import YoutubeDL


def format_stream(url: str, max_resolution: int) -> str:
    """Converte o link do YouTube em URL de stream direto (sem baixar)"""

    if not url.startswith(("http://", "https://")):
        return url
    print("\t>Processando stream do YouTube...")

    fmt = (f"bv*[height<={max_resolution}][ext=mp4]/bv*[height<={max_resolution}]"
           "/bv*[ext=mp4]/b")
    opts = {"format": fmt,
            "quiet": True,
            "no_warnings": True,
            "noplaylist": True}
    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url,
                                download=False)
    if info.get("entries"):
        info = info["entries"][0]
    print(f"Stream pronto: formato {info.get('format_id')} ({info.get('height', '?')}p)")
    return info["url"]