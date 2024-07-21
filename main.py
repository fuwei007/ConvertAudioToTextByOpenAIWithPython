from openai import OpenAI
client = OpenAI(api_key="")

converter = client.audio.transcriptions.create(
    model="whisper-1",
    file=open("audio.mp3", "rb")
)
print(converter.text)

