from midiutil.MidiFile import MIDIFile
from floppy.note import Note

''' Test the range of the drives and some other stuff '''

TestDrives = MIDIFile(3)

pitchmap = {
        0: {
            'lower': 24,
            'upper': 66
            },
        1: {
            'lower': 24,
            'upper':67,
            },
        2: {
            'lower': 24,
            'upper': 60
            }
}

time = 0
duration = 10
volume = 100 #  Makes no difference to floppy drive

print "Try playing C!"
drive = 0
sequence = ['C1', 'C2', 'C3', 'C4']
for note in sequence:
    play = Note()
    n, octave = list(note)
    TestDrives.addTrackName(drive, time, "Position %d" % drive)
    channel = drive

    TestDrives.addNote(drive, channel, play.convert(n, octave), time, duration,
            volume)
    time += duration

print "Trying the lower pitch boundary..."
for drive, pitch in pitchmap.iteritems():
    TestDrives.addTrackName(drive, time, "Position %d" % drive)
    channel = drive

    TestDrives.addNote(drive, channel, pitch['lower'], time, duration, volume)
    time += duration

print "Trying the upper pitch boundary..."
for drive, pitch in pitchmap.iteritems():
    TestDrives.addTrackName(drive, time, "Position %d" % drive)
    channel = drive

    TestDrives.addNote(drive, channel, pitch['upper'], time, duration, volume)
    time += duration

# Try the scale!
duration = 1

for drive, pitch in pitchmap.iteritems():
    print "Trying %d MIDI pitches for drive %d" % (len(range(pitch['lower'],
        pitch['upper'])), drive)
    for n in range(pitch['lower'], pitch['upper']):
        TestDrives.addTrackName(drive, time, "Position %d" % drive)
        channel = drive

        TestDrives.addNote(drive, channel, n, time, duration, volume)
        time += duration

with open("testdrives.mid", "wb") as midi:
    TestDrives.writeFile(midi)

