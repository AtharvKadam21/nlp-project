# Define the grapheme-to-phoneme mappings with examples based on your data
# grapheme_to_phoneme = {
#     'b': ('b', ['bug', 'bubble']),
#     'bb': ('b', ['bubble']),
#     'd': ('d', ['dad', 'add']),
#     'dd': ('d', ['add']),
#     'ed': ('d', ['milled']),
#     'f': ('f', ['fat']),
#     'ff': ('f', ['cliff']),
#     'ph': ('f', ['phone']),
#     'gh': ('f', ['enough']),
#     'lf': ('f', ['half']),
#     'ft': ('f', ['often']),
#     'g': ('g', ['gun']),
#     'gg': ('g', ['egg']),
#     'gh': ('g', ['ghost']),
#     'gu': ('g', ['guest']),
#     'gue': ('g', ['prologue']),
#     'h': ('h', ['hop']),
#     'wh': ('h', ['who']),
#     'j': ('dʒ', ['jam']),
#     'ge': ('dʒ', ['wage']),
#     'g': ('dʒ', ['giraffe']),
#     'dge': ('dʒ', ['edge']),
#     'di': ('dʒ', ['soldier']),
#     'gg': ('dʒ', ['exaggerate']),
#     'k': ('k', ['kit']),
#     'c': ('k', ['cat']),
#     'ch': ('k', ['chris']),
#     'cc': ('k', ['accent']),
#     'lk': ('k', ['folk']),
#     'qu': ('k', ['queen']),
#     'q(u)': ('k', ['rack']),
#     'ck': ('k', ['box']),
#     'x': ('k', ['box']),
#     'l': ('l', ['live']),
#     'll': ('l', ['well']),
#     'm': ('m', ['man']),
#     'mm': ('m', ['summer']),
#     'mb': ('m', ['comb']),
#     'mn': ('m', ['column']),
#     'lm': ('m', ['palm']),
#     'n': ('n', ['net']),
#     'nn': ('n', ['funny']),
#     'kn': ('n', ['know']),
#     'gn': ('n', ['gnat']),
#     'pn': ('n', ['pneumonic']),
#     'mn': ('n', ['mnemonic']),
#     'p': ('p', ['pin']),
#     'pp': ('p', ['dippy']),
#     'r': ('r', ['run']),
#     'rr': ('r', ['carrot']),
#     'wr': ('r', ['wrench']),
#     'rh': ('r', ['rhyme']),
#     's': ('s', ['sit']),
#     'ss': ('s', ['less']),
#     'c': ('s', ['circle']),
#     'sc': ('s', ['scene']),
#     'ps': ('s', ['psycho']),
#     'st': ('s', ['listen']),
#     'ce': ('s', ['pace']),
#     'se': ('s', ['course']),
#     't': ('t', ['tip']),
#     'tt': ('t', ['matter']),
#     'th': ('t', ['thomas']),
#     'ed': ('t', ['ripped']),
#     'v': ('v', ['vine']),
#     'f': ('v', ['of']),
#     'ph': ('v', ['stephen']),
#     've': ('v', ['five']),
#     'w': ('w', ['wit']),
#     'wh': ('w', ['why']),
#     'u': ('w', ['quick']),
#     'o': ('w', ['choir']),
#     'z': ('z', ['zed']),
#     'zz': ('z', ['buzz']),
#     's': ('z', ['his']),
#     'ss': ('z', ['scissors']),
#     'x': ('z', ['xylophone']),
#     'ze': ('z', ['craze']),
#     'se': ('z', ['se']),
#     'ʒ': ('ʒ', ['treasure']),
#     's': ('ʒ', ['division']),
#     'si': ('ʒ', ['azure']),
#     'z': ('ʒ', ['azure']),
#     'tʃ': ('tʃ', ['chip']),
#     'ch': ('tʃ', ['watch']),
#     'tch': ('tʃ', ['future']),
#     'tu': ('tʃ', ['righteous']),
#     'te': ('tʃ', ['watch']),
#     'ʃ': ('ʃ', ['sham']),
#     'sh': ('ʃ', ['ocean']),
#     'ce': ('ʃ', ['sure']),
#     's': ('ʃ', ['special']),
#     'ci': ('ʃ', ['pension']),
#     'si': ('ʃ', ['machine']),
#     'ti': ('ʃ', ['conscience']),
#     'θ': ('θ', ['thongs']),
#     'th': ('θ', ['thongs']),
#     'ð': ('ð', ['leather']),
#     'th': ('ð', ['leather']),
#     'ŋ': ('ŋ', ['ring']),
#     'ng': ('ŋ', ['pink']),
#     'n': ('ŋ', ['tongue']),
#     'ngue': ('ŋ', ['tongue']),
#     'j': ('j', ['you']),
#     'y': ('j', ['onion']),
#     'i': ('j', ['hallelujah']),
#     'æ': ('æ', ['cat']),
#     'a': ('æ', ['plaid']),
#     'ai': ('æ', ['laugh']),
#     'eɪ': ('eɪ', ['bay']),
#     'a': ('eɪ', ['maid']),
#     'ai': ('eɪ', ['weigh']),
#     'eigh': ('eɪ', ['straight']),
#     'aigh': ('eɪ', ['pay']),
#     'ay': ('eɪ', ['foyer']),
#     'er': ('eɪ', ['filet']),
#     'et': ('eɪ', ['eight']),
#     'ei': ('eɪ', ['gauge']),
#     'au': ('eɪ', ['mate']),
#     'a_e': ('eɪ', ['break']),
#     'ea': ('eɪ', ['they']),
#     'ey': ('eɪ', ['they']),
#     'ɛ': ('ɛ', ['end']),
#     'e': ('ɛ', ['bread']),
#     'ea': ('ɛ', ['bury']),
#     'u': ('ɛ', ['friend']),
#     'ie': ('ɛ', ['said']),
#     'ai': ('ɛ', ['many']),
#     'a': ('ɛ', ['leopard']),
#     'eo': ('ɛ', ['heifer']),
#     'ei': ('ɛ', ['aesthetic']),
#     'i:': ('i:', ['be']),
#     'e': ('i:', ['bee']),
#     'ee': ('i:', ['meat']),
#     'ea': ('i:', ['lady']),
#     'y': ('i:', ['key']),
#     'ey': ('i:', ['phoenix']),
#     'oe': ('i:', ['grief']),
#     'ie': ('i:', ['deceive']),
#     'i': ('i:', ['people']),
#     'ei': ('i:', ['quay']),
#     'ɪ': ('ɪ', ['it']),
#     'i': ('ɪ', ['england']),
#     'e': ('ɪ', ['women']),
#     'u': ('ɪ', ['busy']),
#     'ui': ('ɪ', ['guild']),
#     'y': ('ɪ', ['gym']),
#     'ie': ('ɪ', ['sieve']),
#     'aɪ': ('aɪ', ['spider']),
#     'i': ('aɪ', ['sky']),
#     'y': ('aɪ', ['night']),
#     'ie': ('aɪ', ['pie']),
#     'uy': ('aɪ', ['guy']),
#     'ye': ('aɪ', ['stye']),
#     'ai': ('aɪ', ['aisle']),
#     'is': ('aɪ', ['island']),
#     'eigh': ('aɪ', ['height']),
#     'i_e': ('aɪ', ['kite']),
#     'ɒ': ('ɒ', ['swan']),
#     'a': ('ɒ', ['honest']),
#     'ho': ('ɒ', ['maul']),
#     'au': ('ɒ', ['slaw']),
#     'ough': ('ɒ', ['fought']),
#     'oʊ': ('oʊ', ['open']),
#     'o': ('oʊ', ['moat']),
#     'oa': ('oʊ', ['bone']),
#     'o_e': ('oʊ', ['toe']),
#     'oe': ('oʊ', ['sow']),
#     'ow': ('oʊ', ['dough']),
#     'ough': ('oʊ', ['beau']),
#     'eau': ('oʊ', ['brooch']),
#     'oo': ('oʊ', ['sew']),
#     'ew': ('oʊ', ['fruit']),
#     'ʊ': ('ʊ', ['wolf']),
#     'o': ('ʊ', ['look']),
#     'oo': ('ʊ', ['bush']),
#     'ou': ('ʊ', ['would']),
#     'ʌ': ('ʌ', ['lug']),
#     'u': ('ʌ', ['monkey']),
#     'o': ('ʌ', ['blood']),
#     'ou': ('ʌ', ['double']),
#     'u:': ('u:', ['who']),
#     'o': ('u:', ['loon']),
#     'oo': ('u:', ['dew']),
#     'ew': ('u:', ['blue']),
#     'ue': ('u:', ['flute']),
#     'u_e': ('u:', ['shoe']),
#     'ough': ('u:', ['through']),
#     'ui': ('u:', ['fruit']),
#     'oew': ('u:', ['maneuvre']),
#     'ou': ('u:', ['group']),
#     'ɔɪ': ('ɔɪ', ['join']),
#     'oi': ('ɔɪ', ['boy']),
#     'oy': ('ɔɪ', ['buoy']),
#     'aʊ': ('aʊ', ['now']),
#     'ow': ('aʊ', ['shout']),
#     'ou': ('aʊ', ['bough']),
#     'ə': ('ə', ['about']),
#     'a': ('ə', ['ladder']),
#     'er': ('ə', ['pencil']),
#     'i': ('ə', ['dollar']),
#     'ar': ('ə', ['honour']),
#     'our': ('ə', ['augur']),
#     'eəʳ': ('eəʳ', ['chair']),
#     'air': ('eəʳ', ['dare']),
#     'are': ('eəʳ', ['pear']),
#     'ere': ('eəʳ', ['where']),
#     'e': ('eəʳ', ['their']),
#     'ayer': ('eəʳ', ['prayer']),
#     'ɑ:': ('ɑ:', ['arm']),
#     'a': ('ɑ:', ['arm']),
#     'ɜ:ʳ': ('ɜ:ʳ', ['bird']),
#     'ir': ('ɜ:ʳ', ['term']),
#     'er': ('ɜ:ʳ', ['burn']),
#     'ur': ('ɜ:ʳ', ['pearl']),
#     'ear': ('ɜ:ʳ', ['word']),
#     'or': ('ɜ:ʳ', ['journey']),
#     'our': ('ɜ:ʳ', ['myrtle']),
#     'yr': ('ɜ:ʳ', ['myrtle']),
#     'ɔ:': ('ɔ:', ['paw']),
#     'aw': ('ɔ:', ['ball']),
#     'a': ('ɔ:', ['fork']),
#     'or': ('ɔ:', ['poor']),
#     'oor': ('ɔ:', ['fore']),
#     'ore': ('ɔ:', ['board']),
#     'oar': ('ɔ:', ['four']),
#     'our': ('ɔ:', ['taught']),
#     'augh': ('ɔ:', ['war']),
#     'ar': ('ɔ:', ['bought']),
#     'ough': ('ɔ:', ['sauce']),
#     'ɪəʳ': ('ɪəʳ', ['ear']),
#     'ear': ('ɪəʳ', ['steer']),
#     'eer': ('ɪəʳ', ['here']),
#     'ere': ('ɪəʳ', ['tier']),
#     'ʊəʳ': ('ʊəʳ', ['cure']),
#     'ure': ('ʊəʳ', ['tourist'])
# }

# def convert_to_phonemes_with_examples(text):
#     text = text.lower()
#     phoneme_details = []
    
#     i = 0
#     while i < len(text):
#         # Check for multi-letter graphemes first
#         if i < len(text) - 1 and text[i:i + 2] in grapheme_to_phoneme:
#             phoneme, examples = grapheme_to_phoneme[text[i:i + 2]]
#             phoneme_details.append((phoneme, examples))
#             i += 2
#         elif i < len(text) - 2 and text[i:i + 3] in grapheme_to_phoneme:  # Check for three-letter graphemes
#             phoneme, examples = grapheme_to_phoneme[text[i:i + 3]]
#             phoneme_details.append((phoneme, examples))
#             i += 3
#         elif text[i] in grapheme_to_phoneme:
#             phoneme, examples = grapheme_to_phoneme[text[i]]
#             phoneme_details.append((phoneme, examples))
#             i += 1
#         else:
#             # If grapheme not found, keep the original character or handle it
#             phoneme_details.append((text[i], ['N/A']))  # Indicate no example
#             i += 1
            
#     return phoneme_details

# # Example usage
# text = "hello"
# phonetic_representation = convert_to_phonemes_with_examples(text)

# Print the phonetic representation along with example words
# for phoneme, examples in phonetic_representation:
#     print(f"Phoneme: {phoneme}, Examples: {', '.join(examples)}")

from gtts import gTTS

# ARPAbet to IPA mapping
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
                json_output[symbol] = result['IPA'], result['Example']
                tts = gTTS(text=result['Example'], lang='en')
                tts.save(f"static/audio/output{notation_index}.mp3")

            notation_index+=1

        return json_output

