# file: music_3.py
# doc: https://www.analyticsvidhya.com/blog/2020/01/how-to-perform-automatic-music-generation/

#converting 2D array into 1D array
notes_ = [element for note_ in notes_array for element in note_]

#No. of unique notes
unique_notes = list(set(notes_))
print(len(unique_notes))