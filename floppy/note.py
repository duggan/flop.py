"""An attempt to match notes to MIDI pitches.

Uses this table as a reference: http://tonalsoft.com/pub/news/pitch-bend.aspx
"""

class Note:

    # Notes higher than C4 are a bit risky
    octave_range = [1,2,3,4]

    # Mapping notes to pitches
    notes = {
            # Octave n
            'C':lambda n: (n+1)*12, 'C#':lambda n: ((n+1)*12)+1,
            'Db':lambda n: ((n+1)*12)+1,
            'D':lambda n: ((n+1)*12)+2, 'D#':lambda n: ((n+1)*12)+3,
            'Eb':lambda n: ((n+1)*12)+3,
            'E':lambda n: ((n+1)*12)+4,
            'F':lambda n: ((n+1)*12)+5, 'F#':lambda n: ((n+1)*12)+6,
            'Gb':lambda n: ((n+1)*12)+6,
            'G':lambda n: ((n+1)*12)+7, 'G#':lambda n: ((n+1)*12)+8,
            'Ab':lambda n: ((n+1)*12)+8,
            'A':lambda n: ((n+1)*12)+9, 'A#':lambda n: ((n+1)*12)+10,
            'Bb':lambda n: ((n+1)*12)+10,
            'B':lambda n: ((n+1)*12)+11
            }

    def __init__(self):
        pass

    def convert(self, note, octave=1):
        return self.notes[note](int(octave))
