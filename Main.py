import pygame
from tkinter import *
import os


class menu ():
    
    def __init__(self, frame):
        self.frame=frame
        self.i=1
        self.i2=0
        self.freq=44100
        self.pathForLoad=" "
        self.playList=[ ]
        self.nowPlaying=""

        
        pygame.mixer.init(frequency=self.freq, size=-16, channels=1, buffer=4096)
        self.frame = frame
        frame.title("Coursework Music Player")

        playButton=Button(frame, text="play", command=self.playSelected)
        playButton.place(relx=0.3,rely=0.3)

        self.pauseButton=Button(frame, text="pause", command=self.pauseMusic)
        self.pauseButton.place(relx=0.43,rely=0.3)

        fileManger=Button(frame, text="open file manger", command=self.fileManager)
        fileManger.place(relx=0.01,rely=0.01)

        self.playingEntry=Label(frame, text="Now playing:"+self.nowPlaying, bg="white", fg="black")#Now playing
        self.playingEntry.place(relx=0.01, rely=0.12)

        optionsButton=Button(frame, text="Options", command=self.OptionsWindow)
        optionsButton.place(relx=0.38, rely=0.01)

        prewButton=Button(frame, text="prew", command=self.playPrew)
        prewButton.place(relx=0.15,rely=0.3)

        nextButton=Button(frame, text="next", command=self.playNext)
        nextButton.place(relx=0.6,rely=0.3)
        
        lowerFrame=Frame(frame, bg="black")
        lowerFrame.place(relheight=0.5, relwidth=0.98, relx=0.01, rely=0.49)

        self.volumeScroll=Scale(lowerFrame, from_=100, to_=0, fg="black")
        self.volumeScroll.place(relx=0.01, rely=0.01, relheight=0.97, relwidth=0.32)

        buttonVolume=Button(lowerFrame, text="Volume", command=self.volume)
        buttonVolume.place(relx=0.15, rely=0.05)

        self.playListBox=Listbox(lowerFrame, bg="white", fg="black", selectmode=EXTENDED)
        self.playListBox.place(relx=0.34,rely=0.01, relheight=0.97, relwidth=0.55)



    


    def volume(self):
        pygame.mixer.music.set_volume((self.volumeScroll.get())/100)

        
    def playNext(self):
        
        if self.i2>=len(self.playList)-1:
            self.i2=0
        else:
            self.i2=self.i2+1
        pygame.mixer.music.load(self.pathForLoad+"\\"+self.playList[self.i2])
        pygame.mixer.music.play(0)
        self.nowPlaying=self.playList[self.i2]
        self.playingEntry.config(text="Now playing:"+self.nowPlaying)

    
    def playPrew(self):
        if self.i2<=0:
            self.i2=len(self.playList)-1
        else:
            self.i2=self.i2-1
        pygame.mixer.music.load(self.pathForLoad+"\\"+self.playList[self.i2])
        pygame.mixer.music.play(0)
        self.nowPlaying=self.playList[self.i2]
        self.playingEntry.config(text="Now playing:"+self.nowPlaying)
   
        
    def playSelected(self):
        print(self.pathForLoad) 
        pygame.mixer.music.load(self.pathForLoad+"\\"+self.playList[self.i2])
        pygame.mixer.music.play(0)
        self.nowPlaying=self.playList[self.i2]
        self.playingEntry.config(text="Now playing:"+self.nowPlaying)
        self.que()

    def que(self):
        pos=pygame.mixer.music.get_pos()
        pygame.mixer.music.set_volume((self.volumeScroll.get())/100)
        if pos<=-1:
            if self.i2>=len(self.playList)-1:
                self.i2=0
            else:
                self.i2=self.i2+1
            pygame.mixer.music.load(self.pathForLoad+"\\"+self.playList[self.i2])
            pygame.mixer.music.play(0)
            self.nowPlaying=self.playList[self.i2]
            self.playingEntry.config(text="Now playing:"+self.nowPlaying)
        self.frame.after(100, self.que)
        
            
    def pauseMusic(self):
        if self.i==1:
            pygame.mixer.music.pause()
            print("pause")
            self.pauseButton.config(text="pause")
            self.i=2
        else:
            pygame.mixer.music.unpause()
            print("unpause")
            self.pauseButton.config(text="unpause")
            self.i=1
        print("stopMusic command run without any problems")
        

    def fileManager(self):
        self.filemanger_wnd=Toplevel()
        self.filemanger_wnd.title("File manager")
        self.filemanger_wnd.config(bg="gray")
        self.filemanger_wnd.grab_set()
        self.files_list=Listbox(self.filemanger_wnd, bg="white", fg="black", selectmode=EXTENDED)
        self.files_list.pack(side=LEFT)
        scroll=Scrollbar(self.filemanger_wnd,command=self.files_list.yview)
        scroll.pack(side=LEFT,fill=Y)
        self.files_list.config(yscrollcommand=scroll.set)
        frame=Frame(self.filemanger_wnd)
        frame.pack(side=LEFT, padx=10)
        self.path=Entry(frame, bg="white", fg="black")
        self.path.pack(anchor=N)
        btn4=Button(frame,text="make list",command=self.new_lib)
        btn4.pack(fill=X)
        btn5=Button(frame, text="open chosen", command=self.open_chosen)
        btn5.pack(fill=X)
        btn6=Button(frame, text="add selected", command= self.add_to_playlist)
        btn6.pack(fill=X)


    def OptionsWindow(self):
        optionsWindow=Toplevel()
        optionsWindow.title("Options")
        optionsWindow.grab_set()
        

    def open_chosen(self):
        selected=self.loader[(self.files_list.curselection())[0]]
        open_sel=self.path.get()+"\\"+selected
        loader=os.listdir(open_sel)
        self.files_list.delete(0,END)
        for i in loader:
            self.files_list.insert(END, i)

            
    def new_lib(self):
        self.loader=os.listdir(self.path.get())
        self.files_list.delete(0,END)
        for i in self.loader:
            self.files_list.insert(END, i)

    def add_to_playlist(self):
        selected=self.loader[(self.files_list.curselection())[0]]
        print(self.path.get(),selected)
        open_sel=self.path.get()+"\\"+selected
        self.pathForLoad=open_sel
        print(open_sel)
        self.playList=os.listdir(self.pathForLoad)
        print(self.playList)
        self.playListBox.clean()
        for i in self.playList:
            self.playListBox.insert(END,i)
            
        self.filemanger_wnd.destroy()
        
root=Tk()
root.resizable(False,False)
root.geometry("300x300")
Pass_menu=menu(root)
root.mainloop()
