# file: test_noteconversion.py
# functie: pytest test to test note conversions
# 

import pytest
import noteconversion as nc

@pytest.fixture
def input_NoteNameLower():
   input_NoteName = 'c'
   return input_NoteName

def test_getNote_to_noteValue(input_NoteNameLower):
   assert getNoteValue(input_NoteNameLower) == 0

'''
def test_getNote_to_noteValue(input_value):
    test_getNoteName(noteValue, enharmonic=False):
   assert getNoteValue(noteName) == ''
'''