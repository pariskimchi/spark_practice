## %%file is an Ipython magic function that saves the code cell as a file

from mrjob.job import MRJob

class MRSongCount(MRJob):
    
    # the map step
    # => each line in the text file is read as a key, value pair 
    def mapper(self,_,song):
        #output each line as a tuple of (song_names, 1)
        yield (song,1)
    
    # the reduce step:
    # => combine all tuples with the same key
    # key: song_name 
    # then sum all the value of the tuple, 
    def reducer(self,key,values):
        yield(key,sum(values))
        
if __name__ == "__main__":
    MRSongCount.run()
