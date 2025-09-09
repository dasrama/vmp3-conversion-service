import subprocess


def convert_to_mp3(input_file: str, output_file: str):
    try:
        subprocess.run(
            ["ffmpeg", "-i", input_file, "-vn", "-acodec", "libmp3lame", output_file],
            check=True
        )
        print(f"Converted {input_file} → {output_file}")
    except subprocess.CalledProcessError as e:
        print(f" ffmpeg failed: {e}")
        