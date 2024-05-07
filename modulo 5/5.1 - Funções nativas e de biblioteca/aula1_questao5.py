import emoji

emojis = {
    ":smile:": "😊",
    ":heart:": "❤️",
    ":thumbs_up:": "👍",
    ":fire:": "🔥",
    ":rocket:": "🚀"
}

print("Lista de Emojis Disponíveis:")
for texto, emoji_codificado in emojis.items():
    print(texto, ":", emoji_codificado)

frase_codificada = input("\nDigite uma frase codificada com emojis: ")

frase_decodificada = emoji.emojize(frase_codificada, use_aliases=True)
print("Frase decodificada com emojis:")
print(frase_decodificada)