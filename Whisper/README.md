# Whisper
> A simple application of [Whisper API](https://github.com/openai/whisper).

Whisper is a simple Python script to utilize Whisper API from OpenAI. It can help you transcribe a local audio file into text, or translate it into English.

## Using Whisper.py
You can use it in these steps:
1. Install OpenAI SDK (if you don't have Python 3 or pip installed, install them first)
```
pip install openai
```
2. Get your API key from [OpenAI](https://platform.openai.com)
3. Download Whisper.py and insert your personal API key
4. Save the modified file
5. Run Whisper.py
```
python3 ~/Whisper.py
```

The script should show results in the terminal.

## Using Whisper_Pro.py
If you need to transcribe a large file (over 25 MB), please use ```Whisper_Pro.py```. 

Unlike ```Whisper.py```, ```Whisper_Pro.py``` will slice mp3 files into pieces, then transcribe them into a single file ```output.txt```.

> Fun fact: this project involves the participation of ChatGPT.

