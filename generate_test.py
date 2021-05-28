from signal_utils import gen_impulse, klatt_filter
from data_utils import read_formants_from_file, save_to_wav


fs = 44100
formants = read_formants_from_file('formants.txt')

for formant in formants:
    temp = formants[formant]
    pulse = gen_impulse(fs=fs, f0=temp[0])
    r1 = klatt_filter(pulse, fs=fs, f=temp[3])
    r2 = klatt_filter(r1, fs=fs, f=temp[2])
    r3 = klatt_filter(r2, fs=fs, f=temp[1])

    save_to_wav(f'data_test/{formant}', r3, fs=fs)