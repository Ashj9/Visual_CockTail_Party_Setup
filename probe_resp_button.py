from tkinter import *
from tkinter import messagebox as box


def generate_prob_resp():
    arr=['Yes', 'No']
    root=Tk()
    myFont = font.Font(family='Helvetica', size=12, weight='bold')
   
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
    
        self.label = Label(window, text = 'Was the probe word present?', fg = 'light green', 
                      bg = 'black', font = (None, 40, 'bold'), height = 2)
        self.label.pack(side = TOP)
    
        self.gridFrame = Frame(window, bg='black') 
    
        self.arr=arr

        j=-1
        for i ,val in enumerate(arr):
            self.buttons = Button(self.gridFrame, text = val , width = 10, height = 2,font=(None, 50), command=lambda string=val: self.get_id(string))
            if i%8 == 0:
                j=j+1
            self.buttons.grid(row=i%8, column=j, pady = 50, padx = 50, sticky=W) 
        
        
        self.gridFrame.pack(side=TOP)           
    

        
    def get_id(self,string):
#            print(string)
            self.get_probe_resp(string)
    def get_probe_resp(self, string):
        self.response=string
        self.window.destroy()
        
     
if __name__=="__main__":            
   a=generate_prob_resp()
    



