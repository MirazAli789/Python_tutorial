import os

if __name__ == "__main__":
    print("Welcome to robospeaker")
    x = input("Enter word: ")
    command = f"powershell -Command \"Add-Type -AssemblyName System.Speech; $synthesizer = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer; $synthesizer.Speak('Hello, {x}.')\""
    os.system(command)
