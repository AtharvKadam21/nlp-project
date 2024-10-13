from flask import Flask, render_template, request
from gtts import gTTS
import os

directory = 'static/audio'
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)  # Delete the file
    except Exception as e:
        print(f"Error deleting file {file_path}: {e}")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        user_input = request.form['user_input']
        # Process the input and generate output strings
        output_data = main(user_input)
        output_strings = []
        for key, value in output_data.items():
            # Now value is a dictionary, so we can access it correctly
            formatted_output = f"{key}: IPA = {value['IPA']}, Example = {value['Example']}"
            output_strings.append(formatted_output)
        return render_template('index.html', output_strings=output_strings)
    return render_template('index.html', output_strings=None)

arpabet_to_ipa = {
    "AA": {"IPA": "ɑː", "Example": "father"},
    "AE": {"IPA": "æ", "Example": "cat"},
    "AH": {"IPA": "ʌ", "Example": "cup"},
    "AO": {"IPA": "ɔː", "Example": "thought"},
    "AW": {"IPA": "aʊ", "Example": "how"},
    "AY": {"IPA": "aɪ", "Example": "my"},
    "EH": {"IPA": "ɛ", "Example": "bed"},
    "ER": {"IPA": "ɜːr", "Example": "her"},
    "EY": {"IPA": "eɪ", "Example": "say"},
    "HH": {"IPA": "h", "Example": "hat"},
    "IH": {"IPA": "ɪ", "Example": "sit"},
    "IY": {"IPA": "iː", "Example": "see"},
    "OW": {"IPA": "oʊ", "Example": "go"},
    "OY": {"IPA": "ɔɪ", "Example": "boy"},
    "UH": {"IPA": "ʊ", "Example": "put"},
    "UW": {"IPA": "uː", "Example": "blue"},
    "B": {"IPA": "b", "Example": "bed"},
    "D": {"IPA": "d", "Example": "dog"},
    "G": {"IPA": "ɡ", "Example": "go"},
    "K": {"IPA": "k", "Example": "cat"},
    "P": {"IPA": "p", "Example": "pig"},
    "T": {"IPA": "t", "Example": "top"},
    "F": {"IPA": "f", "Example": "fish"},
    "V": {"IPA": "v", "Example": "van"},
    "TH": {"IPA": "θ", "Example": "think"},
    "DH": {"IPA": "ð", "Example": "this"},
    "S": {"IPA": "s", "Example": "see"},
    "Z": {"IPA": "z", "Example": "zoo"},
    "SH": {"IPA": "ʃ", "Example": "she"},
    "ZH": {"IPA": "ʒ", "Example": "measure"},
    "M": {"IPA": "m", "Example": "man"},
    "N": {"IPA": "n", "Example": "no"},
    "NG": {"IPA": "ŋ", "Example": "sing"},
    "L": {"IPA": "l", "Example": "leg"},
    "R": {"IPA": "r", "Example": "red"},
    "Y": {"IPA": "j", "Example": "yes"},
    "W": {"IPA": "w", "Example": "we"},
}

file_path = 'cmudict_SPHINX_40.txt'

def search_word_in_file(file_path, search_word):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Split the line into the word and its notation
        parts = line.strip().split('\t')  # Assuming the file uses tab as delimiter
        if len(parts) > 1:
            word = parts[0]
            notation = parts[1]
            if word.lower() == search_word.lower():  # Case insensitive search
                return notation

    return None  # Return None if the word is not found

def get_ipa_and_example(arpabet_symbol):
    """Retrieve IPA notation and example word from ARPAbet symbol."""
    return arpabet_to_ipa.get(arpabet_symbol.upper(), None)

def main(user_input):
    search_word = user_input
    notation = search_word_in_file(file_path, search_word)

    if notation:
        phonetic_representation = notation.split()
        notation_index = 0
        json_output = {}        
        for symbol in phonetic_representation:
            result = get_ipa_and_example(symbol)
            if result:
                # print(f"ARPAbet: {symbol}, IPA: {result['IPA']}, Example: {result['Example']}")
                json_output[symbol] = {
                    'IPA': result['IPA'],
                    'Example': result['Example']
                }
                tts = gTTS(text=result['Example'], lang='en')
                tts.save(f"static/audio/{symbol}.mp3")

            notation_index+=1

        return json_output


if __name__ == '__main__':
    app.run(debug=True)
