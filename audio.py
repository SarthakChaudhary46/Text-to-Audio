from gtts import gTTS
import os
import platform

# Function to find the next available output file (output1.mp3, output2.mp3, etc.)
def get_next_filename():
    i = 1
    while os.path.exists(f"output{i}.mp3"):
        i += 1
    return f"output{i}.mp3"

# Get multiline input for the story
print("Enter the text you want to convert to speech. Type 'DONE' on a new line when you're finished:")

story_lines = []
while True:
    line = input()
    if line.strip().lower() == "done":  # Exit condition when user types "DONE"
        break
    story_lines.append(line)

# Join all lines into a single string
text = "\n".join(story_lines)

# Create a TTS object with the selected language
tts = gTTS(text=text, lang='en', slow=False)

# Get the next available filename
output_filename = get_next_filename()

# Save the generated speech as an MP3 file
tts.save(output_filename)
print(f"Audio saved as {output_filename}")

# Platform-specific audio playback
system_platform = platform.system()

if system_platform == "Windows":
    os.system(f"start {output_filename}")  # For Windows
elif system_platform == "Darwin":
    os.system(f"open {output_filename}")  # For macOS
elif system_platform == "Linux":
    os.system(f"xdg-open {output_filename}")  # For Linux
else:
    print("Unsupported platform for automatic audio playback.")
