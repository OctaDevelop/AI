import openai
# Enter your own API key from OpenAI
openai.api_key = ""

print("Target:")
print("1. Audio Transcription")
print("2. Audio Translation")
print("3. Audio Transcription and Translation")

choice = input("Please input 1 or 2, then press enter:")
if choice == "1":
    file_path = input("Enter file path: ")
    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    transcript_text = transcript["text"]
    print(transcript_text)
elif choice == "2":
    file_path = input("Enter file path: ")
    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.translate("whisper-1", audio_file)
    transcript_text = transcript["text"]
    print(transcript_text)
elif choice == "3":
    file_path = input("Enter file path: ")
    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    with open(file_path, "rb") as audio_file:
        translate = openai.Audio.translate("whisper-1", audio_file)
    transcript_text = transcript["text"]
    translate_text = translate["text"]
    print(transcript_text)
    print(translate_text)

else:
    print("Invalid input. Please enter 1, 2 or 3.")
