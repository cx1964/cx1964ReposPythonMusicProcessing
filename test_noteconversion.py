# file: test_noteconversion.py
# functie: pytest test to test note conversions
# 

import pytest
import noteconversion as nc

@pytest.fixture
def input_NoteNameLower():
   noteName = 'C'
   input_NoteName = noteName.lower()
   return input_NoteName

def test_getNote_to_noteValue(input_NoteNameLower):
   assert nc.getNoteValue(input_NoteNameLower) == 0

def test_getNote_to_noteValue_Case_insensitive ():
   noteName = 'f##'
   assert nc.getNoteValue(noteName.lower()) == nc.getNoteValue(noteName.upper())

#toDo:
# Create test for nc.getNoteName()
'''
def test_getNoteName(input_value):
    test_getNoteName(noteValue, enharmonic=False):
   assert nc.getNoteName(noteValue, enharmonic=False) == ''
'''