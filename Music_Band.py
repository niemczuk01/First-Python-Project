class MusicBand:
    def __init__(self, name):
        self.name = name
        self.members = {}
        self.song_list = []
    
        
    def add_member(self, name, role):
        self.members[name] = role
    
    def remove_member(self, name):
        if name in self.members:
            del self.members[name]
        
    def release_song(self, song_title):
        self.song_list.append(song_title)
        
    def list_songs(self):
        print (f"{self.song_list}")
    
    def list_members(self):
        for name, role in self.members.items():
            print(f"{name} - {role}")
    
        
def main():
    band = MusicBand("Wandering Monks")
    band.add_member("Punky Monk", "The singer")
    band.add_member("Funky Monk", "The bassist")
    band.add_member("Clunky Monk", "The guitarist") 
    band.add_member("Chunky Monk", "The drummer")
    band.list_members()
    band.release_song("One with nothing")
    band.release_song("Winston")
    band.list_songs()
    band.remove_member("Chunky Monk")
    band.add_member("Junky Monk", "The drummer")
    band.list_members()
  

if __name__ == "__main__":
    main()
