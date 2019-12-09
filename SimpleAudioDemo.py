import numpy as np
import simpleaudio as sa

player_notes = {  
    'C': ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C'],
    'C#': ['C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#'],
    'Db' : ['Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab','A','Bb','B', 'C', 'Db'],
    'D': ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D'],
    'D#': ['D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#'],
    'Eb' : ['Eb', 'E', 'F', 'Gb', 'G', 'Ab','A','Bb','B', 'C', 'Db', 'D', 'Eb'],
    'E': ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E'],
    'F' : ['F','Gb', 'G', 'Ab','A','Bb','B', 'C', 'Db','D', 'Eb', 'E', 'F'],
    'F#': ['F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F'],
    'Gb' : ['Gb', 'G', 'Ab','A','Bb','B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb'],
    'G': ['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G'],
    'G#': ['G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'],
    'Ab' : ['Ab','A','Bb','B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab'],
    'A': ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A'],
    'A#': ['A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#'],
    'Bb' : ['Bb','B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab','A', 'Bb'],
    'B': ['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'],
}

rootFreqs = {}
rootFreqs['A'] = 440.0
rootFreqs['A#'] = 466.1637615180899
rootFreqs['Bb'] = 466.1637615180899
rootFreqs['B'] = 493.8833012561241 
rootFreqs['C'] = 523.2511306011972
rootFreqs['C#'] = 554.3652619537442
rootFreqs['Db'] = 554.3652619537442
rootFreqs['D'] = 587.3295358348151
rootFreqs['D#'] = 622.2539674441618
rootFreqs['Eb'] = 622.2539674441618
rootFreqs['E'] = 659.2551138257398
rootFreqs['F'] = 698.4564628660078
rootFreqs['F#'] = 739.9888454232688
rootFreqs['Gb'] = 739.9888454232688
rootFreqs['G'] = 783.9908719634985
rootFreqs['G#'] = 830.6093951598903
rootFreqs['Ab'] = 830.6093951598903
# print(rootFreqs)

# Finds the frequency of the particular note step half-steps away 
def note_freq(root_freq, step=0):
    return root_freq * 2 ** (step / 13)

def populateNoteFrequencies(key_freq=440):
    note_frequencies = [ note_freq(key_freq, i) for i in range(13) ]
    return note_frequencies

# print("Chromatic notes starting with {}: {}".format('A',populateNoteFrequencies()))

scaleFreqTables = {}
for k in rootFreqs.keys():
    scaleFreqTables[k] = populateNoteFrequencies(rootFreqs[k])

# for k in rootFreqs.keys():
#     print(k + ": {}".format(scaleFreqTables[k]))

# scales used loosely for tone patterns
scales = {
    'major': [0, 2, 4, 5, 7, 9, 11, 12],
    'minor': [0, 2, 3, 5, 7, 8, 10, 12],
    'hexBlues': [0, 3, 5, 6, 7, 10, 12],
    'pentMajor': [0, 2, 4, 7, 9],
    'pentMinor': [0, 3, 5, 7, 10],
    'pentAltered': [0, 2, 3, 7, 9],
    'bnotes': [0, 4, 7, 9, 10, 9, 7, 4], # basis of chord change sequences
    'tnotes': [0, 4, 7, 10, 0, 10, 7, 4],
}

def findNotes(key):
    L = player_notes[key]
    return L

def playFreq(freq=440):
    # get timesteps for each sample, T is note duration in seconds
    sample_rate = 44100
    T = 0.25
    t = np.linspace(0, T, T * sample_rate, False)

    # # generate sine wave notes
    # A_note = np.sin(A_freq * t * 2 * np.pi)
    # Csh_note = np.sin(Csh_freq * t * 2 * np.pi)
    # E_note = np.sin(E_freq * t * 2 * np.pi)

    A_note = np.sin(freq * t * 2 * np.pi)

    # concatenate notes
    # audio = np.hstack((A_note, Csh_note, E_note))    #
    audio = np.hstack((A_note))    #
    # normalize to 16-bit range
    audio *= 32767 / np.max(np.abs(audio))
    # convert to 16-bit data
    audio = audio.astype(np.int16)

    # start playback
    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)

    # wait for playback to finish before exiting
    play_obj.wait_done()

# playFreq()


import logging


logging.basicConfig(level=logging.DEBUG, format=' %(message)s')

# def showScaleNotes(scale='major', key='C'):
#     result = []
#     notes = findNotes(key)
#     #logging.debug(keyScaleNotes)
#     for i in scales[scale]:
#         result.append(notes[i])
#     logging.debug(scale + ": " + str(result))
#     return result

def playScaleNotes(scale='major', key='C'):
    resultNotes = []
    resultFreqs = []
    notes = findNotes(key)
    freqs = scaleFreqTables[key]
    print("len(notes) = {}".format(len(notes)))
    for i in scales[scale]:
        # if i < len(notes)-1:
        resultNotes.append(notes[i])
        resultFreqs.append(freqs[i])

    print(key + " " + scale + " : " + str(resultNotes))
    # print("Frequencies: {}".format(resultFreqs))
    playNoteFreqs(resultFreqs)
    # return (resultNotes, resultFreqs)

def playNotes(inNotes):
    noteFreqs = [ rootFreqs[note] for note in inNotes ]
    for f in noteFreqs:
        playFreq(f)
        
def playNoteFreqs(freqs):
    #    playNoteFreqs(scale, key, notes, freqs)
    for f in freqs:
        playFreq(f)
        

fifths = {
    'A': 'E',
    'E': 'B',
    'B': 'Gb',
    'Gb': 'Db',
    'Db': 'Ab',
    'Ab': 'Eb',
    'Eb': 'Bb',
    'Bb': 'F',
    'F': 'C',
    'C': 'G',
    'G': 'D',
    'D': 'A',
}

def circleOfFifths(scale):
    k = 'C'
    for i in range(12):
        playScaleNotes(scale, key=k)
        k = fifths[k]

# x for i in ['C', 'D', 'E', 'F', 'G', 'A', 'B']:
def demoScales(key='C'):
    playScaleNotes(scale='major', key=key)
    playScaleNotes(scale='minor', key=key)
    playScaleNotes(scale='pentMajor', key=key)
    playScaleNotes(scale='pentMinor', key=key)
    playScaleNotes(scale='hexBlues', key=key)
    playScaleNotes(scale='bnotes', key=key)
    playScaleNotes(scale='pentAltered', key=key)

def play145():
    playScaleNotes(scale='bnotes', key='C')
    playScaleNotes(scale='bnotes', key='C')
    playScaleNotes(scale ='bnotes', key='F')
    playScaleNotes(scale='bnotes', key='C')
    playScaleNotes(scale='bnotes', key='G')
    playScaleNotes(scale='bnotes', key='F')
    playScaleNotes(scale='bnotes', key='C')
    playScaleNotes(scale='tnotes', key='G')


#demoScales('A')
# play145()

# demoScales('E')
# Returns
# E major : ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E']
# E minor : ['E', 'F#', 'G', 'A', 'B', 'C', 'D', 'E']
# E pentMajor : ['E', 'F#', 'G#', 'B', 'C#', 'E']
# E pentMinor : ['E', 'G', 'A', 'B', 'D', 'E']
# E hexBlues : ['E', 'G', 'A', 'A#', 'B', 'D', 'E']
# E bnotes : ['E', 'G#', 'B', 'C#', 'D', 'C#', 'B', 'G#']
# E pentAltered : ['E', 'F#', 'G', 'B', 'C#', 'E']


# circleOfFifths('pentMajor')
# circleOfFifths('pentMinor')

# a_minor_seventh = ['A', 'C', 'E', 'G']
# playNotes(a_minor_seventh)

# playScaleNotes(scale='tnotes', key='G')

# playScaleNotes(scale='bnotes', key='G')

# playScaleNotes(scale='minor', key='G')

playScaleNotes()

