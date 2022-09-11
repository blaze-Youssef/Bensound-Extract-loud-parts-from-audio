from pydub import AudioSegment
from pydub.utils import make_chunks
def get_loudest_parts_onefile(song, x=0.1, outputfile="output.mp3",chunk_length_ms=5000):
    song = AudioSegment.from_wav(song)
    MIN_VAL = x
    li = []
    li1 = []
    average = song.dBFS
    trigger_dbfs = average - average*MIN_VAL

    chunks = make_chunks(song, chunk_length_ms)
    s= 0
    start = False
    for i in chunks:
        if round(trigger_dbfs,1) <= round(i.dBFS,1):
            if not start:
                start = True

            li.append(i)
        elif start==True:
            li1.append(sum(li, AudioSegment.empty()))
            li = []
            start = False


    a = sum(li1, AudioSegment.empty())
    a.export(outputfile, format="mp3")


def get_loudest_parts_onedir(song, x=0.1, outputdir="audios/",chunk_length_ms=5000):
    song = AudioSegment.from_wav(song)
    MIN_VAL = x
    li = []
    li1 = []
    average = song.dBFS
    trigger_dbfs = average - average*MIN_VAL

    chunks = make_chunks(song, chunk_length_ms)
    s= 0
    start = False
    for i in chunks:
        if round(trigger_dbfs,1) <= round(i.dBFS,1):
            if not start:
                start = True

            li.append(i)
        elif start==True:
            li1.append(sum(li, AudioSegment.empty()))
            li = []
            start = False

    for i in range(len(li1)):
        li1[i].export(f"{outputdir}/{i}.mp3", format="mp3")

