import numpy as np

def fct_1(a, b):
  c = a+b
  d = np.mean([a,b,c])
  return a, b, c, d

def fct_2(b, c):
  f = b**2 + 2*c
  return f

#@title CREATE FINAL DATA
def createMusicData(musicPath):
  
    #read all the filenames
    files=[i for i in os.listdir(musicPath) ]

    #reading each midi file
    notes_array = np.array([read_midi(musicPath+i) for i in files])

    #converting 2D array into 1D array
    notes_ = [element for note_ in notes_array for element in note_]

    #No. of unique notes
    unique_notes = list(set(notes_))

    freq = dict(Counter(notes_))
    frequent_notes = [note_ for note_, count in freq.items() if count>=50]

    #concatenating all 100 audio files
    new_music=[]

    for notes in notes_array:
        temp=[]
        for note_ in notes:
            if note_ in frequent_notes:
                temp.append(note_)            
        new_music.append(temp)
        
    new_music = np.array(new_music)

    #cutting all files to 1000
    diff = 0

    for i in range(100):
        diff = len(new_music[i]) - 1000
        if (diff > 0):
          new_music[i] = new_music[i][:-diff]
        elif (diff < 0):
          for j in range(-diff):
            new_music[i].append(0)

    list(set(new_music.ravel()[0]))


    #DICTIONARY unique notes --> numbers
    #unique_x = np.unique(np.asarray([new_music[i][0:1001] for i in range(100)]).reshape(-1))
    #x_note_to_int = dict((note_, number) for number, note_ in enumerate(unique_x))
    #predicted_notes = [x_int_to_note[i] for i in intSong]

    #preparing input sequences
    x_seq=[]
    for i in new_music:
        temp=[]
        for j in i:
            #assigning unique integer to every note
            temp.append(x_note_to_int[str(j)])
        x_seq.append(temp)

    x_seq = np.array(x_seq)

    x = []
    window_size = 32 #increase
    for i in tqdm(x_seq):
        this_x_ = [] # placeholder
        for j in range(len(i)-window_size):
            this_x_.append(i[j:(j+window_size)])
        x.append(this_x_)

    x_arr = np.asarray(x)
    x_arr_resh = x_arr.reshape((100, 968, 32, 1))

    bigX, bigY = x_arr_resh[:, 0:967, :, :], x_arr_resh[:, 967, :, :]
    bigY = bigY.reshape((100, 32))

    return bigX, bigY
  
  
  
#CSV DATA

def createEmotionData(emotionData):

    new_data = emotionData.groupby('track id').mean().round(0)
    new_data['track_id'] = new_data.index
    final_data = new_data[['track_id', 'calmness', 'power']]

    return final_data

