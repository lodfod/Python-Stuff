# program to split audio segments into 60 second intervals, for use in data training sets, uses PyDub
# by Archish Arun 

from pydub import AudioSegment
from pydub.utils import make_chunks
import shutil, os

parent_dir = '/Users/archisharun/Desktop/AudioSplicing' # change to your path!!! windows example: C:\Documents\AudioSplicing

def splice(parent_dir, name):
    podcast = AudioSegment.from_file(name , "mp3") 
    print('podcast '+name+' located')
    chunk_length_ms = 60*1000 

    
    directory = name+'chunks'
    path = os.path.join(parent_dir, directory)

    os.mkdir(path)
    os.chdir(path)
    print('changed directory to '+path)

    chunks = make_chunks(podcast, chunk_length_ms) 
    chunkfiles = []

    #Export all of the individual chunks as wav files
    for i, chunk in enumerate(chunks):
        chunk_name = name+"chunk{0}.mp3".format(i)
        chunkfiles.append(chunk_name)
        chunk.export(chunk_name, format="mp3")

    os.chdir(parent_dir)
    print('returned to parent dir')
    return None


def main():
    mp3_files = [f for f in os.listdir(parent_dir) if f.endswith('.mp3')]

    for name in mp3_files:
        splice(parent_dir, name)
    return None

if __name__ == "__main__": main()
