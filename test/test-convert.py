import unittest
from floppy.note import Note

class TestNoteConversion(unittest.TestCase):

    def setUp(self):
        self.seq = [('C1', 24), ('C2', 36), ('C3', 48), ('C4', 60)]

    def test_convert(self):
        for given_note, expected_pitch in (self.seq):
            n, octave = list(given_note)
            note = Note()
            pitch = note.convert(n, octave)
            self.assertEqual(expected_pitch, pitch)

if __name__ == '__main__':
    unittest.main()

