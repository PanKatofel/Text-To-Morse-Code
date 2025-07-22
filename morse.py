letter_to_morse = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    ' ': ' '
}
morse_to_letter = {value: key for key, value in letter_to_morse.items()}

class Morse(list):
    """Class which represents Morse code"""
    pass


def encode(text: str) -> Morse:
    """Encoding text to Morse code"""
    text = text.lower()
    list_text = list(text)
    morse = Morse()

    # Intentional skip of char which are not in list
    for letter in list_text:
        if letter in letter_to_morse:
            morse.append(letter_to_morse[letter])

    return morse


def decode(morse: Morse) -> str:
    """Decoding Morse code to text"""
    text = ""

    for code in morse:
        if code in morse_to_letter:
            text = text + morse_to_letter[code]
        else:
            raise ValueError(f"Unknown Morse code: {code}")

    return text


print(f"Input: Hello\n")

morse_value = encode("Hello")
print(f"Morse: {morse_value}")
decoded_value = decode(morse_value)
print(f"Decoded Value: {decoded_value}")
