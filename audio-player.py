import keyboard
import pygame
import os

# Inicializa o sistema de áudio sem latência
pygame.mixer.init()

# Dicionário mapeando as teclas aos arquivos de som na pasta local 'memes'
SOUND_MAPPING = {
    'F13': 'memes/risada.mp3',
    'F14': 'memes/palmas.mp3',
    'F15': 'memes/mãe-tem-café.mp3',
}

def play_sound(file_path):
    if os.path.exists(file_path):
        print(f"Reproduzindo: {file_path}")
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    else:
        print(f"Erro: Arquivo {file_path} não encontrado!")

print("Aguardando atalhos do Stream Deck... (Pressione Ctrl+C para encerrar)")

# Registra os ouvintes globais para cada tecla
for key, sound_file in SOUND_MAPPING.items():
    keyboard.add_hotkey(key, play_sound, args=[sound_file])

# Mantém o script ativo escutando as teclas no sistema operacional
keyboard.wait()
