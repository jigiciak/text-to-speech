import ast
import soundfile as sf


def read_formants_from_file(path):
    f = open(path, encoding='utf8')
    content = f.read()
    formants = ast.literal_eval(content)
    f.close()

    return formants


def save_to_wav(filename, signal, fs):
    sf.write(f'{filename}.wav', signal, fs)