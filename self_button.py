from tkinter import *
from tkinter import messagebox as box


def generate_resp():
    arr=['THAT', 'WITH', 'HAVE', 'THIS', 'WILL', 'YOUR', 'FROM', 'THEY', 'KNOW', 'WANT', 'BEEN', 'GOOD', 'MUCH', 'SOME', 'TIME', 'VERY', 'WHEN', 'COME', 'HERE', 'JUST', 'LIKE','MAKE', 'MANY', 'MORE', 'ONLY','TAKE', 'THAN', 'THEM', 'WELL', 'WERE']    
    root=Tk()
   
   
    my_resp=MyScore(root,arr)
    root.mainloop()
    
    return my_resp
class MyScore:
    def __init__(self, window, arr):
        self.window=window
        self.response=None
        window.title('Select the target word which you saw')
        window.geometry('1000x800')
        window.configure(background = 'black')
    
        self.label = Label(window, text = 'Select the target word which you saw', fg = 'light green',
                      bg = 'black', font = (None, 30), height = 2)
        self.label.pack(side = TOP)
    
        self.gridFrame = Frame(window, bg='black') # New frame to store buttons
        self.arr=arr

        j=-1
        for i ,val in enumerate(arr):
            self.buttons = Button(self.gridFrame, text = val , width = 10, height = 2, command=lambda string=val: self.get_id(string))
            if i%8 == 0:
                j=j+1
            self.buttons.grid(row=i%8, column=j, pady = 10, padx = 50, sticky=W) 
        
        
        self.gridFrame.pack(side=BOTTOM)           
    

        
    def get_id(self,string):
#            print(string)
            self.get_response(string)
    def get_response(self, string):
        self.response=string
        self.window.destroy()
        
     
if __name__=="__main__":            
    pass
    



