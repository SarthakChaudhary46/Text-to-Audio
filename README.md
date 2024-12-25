# Text-to-Speech Conversion with gTTS

This Python script allows you to convert any text into speech and save it as an MP3 file. You can input a multi-line story or text, and the program will automatically generate an MP3 file with the spoken version of the text. It also supports automatic playback depending on your platform (Windows, macOS, or Linux).

## Requirements

Before running the script, make sure you have the following installed:

1. **Python 3.x** (any version 3.x will work)
2. **gTTS (Google Text-to-Speech)** - Python library for converting text to speech.
   - To install it, run:
     ```bash
     pip install gTTS
     ```

3. **Platform-specific utilities:**
   - Windows: Uses `start` to play the audio.
   - macOS: Uses `open` to play the audio.
   - Linux: Uses `xdg-open` to play the audio.

The script should work out of the box, but make sure that your system supports the audio playback command specific to your platform.

## How to Use

### Step 1: Run the Script
Once you've installed the required dependencies, you can run the script. You’ll be prompted to enter the text you want to convert to speech.

### Step 2: Enter Your Text
You will be prompted to enter the text to be converted to speech. Type in your text and press **Enter** after each line. Once you are done typing your text, type `DONE` on a new line to finish the input.

Example:
Enter the text you want to convert to speech. Type 'DONE' on a new line when you're finished: It was a quiet afternoon when I decided to take the old trail I’d heard about for years but never dared to explore. You know, the one that everyone says is haunted, that no one really talks about, but no one’s brave enough to walk down? I didn’t believe in ghosts… or at least, that’s what I thought. "DONE"


### Step 3: The Script Will Convert the Text to Speech
Once you enter the text and type `DONE`, the script will:

1. Convert your text into speech using Google's TTS engine (gTTS).
2. Save the generated speech as an MP3 file with an auto-incrementing filename (e.g., `output1.mp3`, `output2.mp3`, etc.).
3. Play the generated MP3 file automatically on your system (based on your operating system: Windows, macOS, or Linux).

### Type "DONE" on a new line when you're finished: This is a test text. DONE Audio saved as output1.mp3


- The MP3 file will be saved in the same directory as the script.
- If you’re using Windows, the audio will automatically start playing.
- On macOS, it will open the file using the default media player.
- On Linux, it will use `xdg-open` to play the file.

