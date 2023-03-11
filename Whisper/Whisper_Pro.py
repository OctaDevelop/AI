import openai
from pydub import AudioSegment

# Enter your own API key from OpenAI
openai.api_key = ""

print("Target:")
print("1. Audio Transcription")
print("2. Audio Translation")
print("3. Audio Transcription and Translation")

choice = input("Please input 1, 2, or 3, then press enter:")
if choice == "1" or choice == "2" or choice == "3":
    file_path = input("Enter file path: ")
    
    # 将音频文件切成 10 分钟的块
    audio = AudioSegment.from_file(file_path)
    chunk_length_ms = 10 * 60 * 1000
    chunks = list(audio[::chunk_length_ms])
    for i, chunk in enumerate(chunks):
        chunk.export(f"{file_path}_{i}.mp3", format="mp3")

    with open("output.txt", "w") as f:
        # 为每个块执行所选操作
        if choice == "1":
            for i, chunk in enumerate(chunks):
                with open(f"{file_path}_{i}.mp3", "rb") as audio_file:
                    transcript = openai.Audio.transcribe("whisper-1", audio_file)
                transcript_text = transcript["text"]
                f.write(f"Transcription for {file_path}_{i}.mp3:\n{transcript_text}\n")
        elif choice == "2":
            for i, chunk in enumerate(chunks):
                with open(f"{file_path}_{i}.mp3", "rb") as audio_file:
                    transcript = openai.Audio.translate("whisper-1", audio_file)
                transcript_text = transcript["text"]
                f.write(f"Translation for {file_path}_{i}.mp3:\n{transcript_text}\n")
        else:
            for i, chunk in enumerate(chunks):
                with open(f"{file_path}_{i}.mp3", "rb") as audio_file:
                    transcript = openai.Audio.transcribe("whisper-1", audio_file)
                with open(f"{file_path}_{i}.mp3", "rb") as audio_file:
                    translate = openai.Audio.translate("whisper-1", audio_file)
                transcript_text = transcript["text"]
                translate_text = translate["text"]
                f.write(f"Transcription for {file_path}_{i}.mp3:\n{transcript_text}\n")
                f.write(f"Translation for {file_path}_{i}.mp3:\n{translate_text}\n")
else:
    print("Invalid input. Please enter 1, 2, or 3.")
