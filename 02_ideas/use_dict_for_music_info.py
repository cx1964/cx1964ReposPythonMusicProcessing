# file: use_dict_for_music_info.py


music_info=dict()
# create the time info for both staves
x0=[['m1', 1],['m1', 2], ['m1', 3], ['m2', 1], ['m2', 2], ['m2', 3]]
x1=x0
music_info['x0']=x0
music_info['x1']=x1
# create the note value info for both staves
y0=[0,1,2,3,4,5]
y1=[6,7,8,9,10,11]
music_info['y0']=y0
music_info['y1']=y1
print(music_info)
for t in ['x0', 'x1']:
    print(music_info[t])
for n in ['y0', 'y1']:
    print(music_info[n])