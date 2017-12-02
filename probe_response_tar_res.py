#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 12:31:43 2017

@author: ashish
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 12:25:27 2017

@author: ashish
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 00:18:28 2017

@author: ashish
"""

import pygame as pg
import time
import numpy as np
import self_button
import probe_resp_button
black=(0,0,0)
white=(255,255,255)
gray=(128,128,128)
target_array=['THAT', 'WITH', 'HAVE', 'THIS', 'WILL', 'YOUR', 'FROM', 'THEY', 'KNOW', 'WANT', 'BEEN']
raw_arr=['THAT', 'WITH', 'HAVE', 'THIS', 'WILL', 'YOUR', 'FROM', 'THEY', 'KNOW', 'WANT', 'BEEN', 'GOOD', 'MUCH', 'SOME', 'TIME', 'VERY', 'WHEN', 'COME', 'HERE', 'JUST', 'LIKE','MAKE', 'MANY', 'MORE', 'ONLY','TAKE', 'THAN', 'THEM', 'WELL', 'WERE']

probe='XXXXXXXXXXX'


class Word_Disp:
    
    
    def __init__(self,disp_height,disp_width,sequence_len,no_of_trials,separation,add_probe):
        self.disp_height=disp_height
        self.disp_width=disp_width
        self.sequence_len=sequence_len
        self.no_of_trials=no_of_trials
        self.tar_pos=0
        self.selected_target=None
        self.separation=separation
        self.shuffled_arr={}
        self.add_probe=add_probe
        self.word_arr_generator(raw_arr,target_array,probe)
        self.Disp_words(self.shuffled_arr)  
        
        
    def distractor_objects(self,text, font):
        text_surface=font.render(text, True, black )
        return text_surface, text_surface.get_rect()
    def target_objects(self,text, font):
        text_surface=font.render(text, True, white )
        return text_surface, text_surface.get_rect()
    
    def distractor_generator(self,inp_arr):
        np.random.shuffle(inp_arr)
        np.random.shuffle(inp_arr)
        np.random.shuffle(inp_arr)
        return inp_arr[0:sequence_len]
    def target_selector(self,tar_arr):
        ind=np.random.randint(0,9)
        return tar_arr[ind]

    
        
    def word_arr_generator(self,raw_arr,tar_arr,probe):
        self.shuffled_arr=self.distractor_generator(raw_arr)
        self.tar_pos=np.random.randint(6,15)
     
        self.selected_target = tar_arr[np.random.randint(0,len(tar_arr)) ]
        self.shuffled_arr[self.tar_pos]= self.selected_target;
          
        probe_pos=self.separation+self.tar_pos
        if self.add_probe:
             self.shuffled_arr[probe_pos]=probe
        self.separation=probe_pos-self.tar_pos
        

    

# =============================================================================
#     def word_arr_disp(self,text):
#         large_text=pg.font.Font(pg.font.get_default_font(),100)
#         text_surface, text_box=self.text_objects(text, large_text)
#         text_box.center=((disp_width/2,disp_height/2))
#         disp.blit(text_surface,text_box)
#         pg.display.update()
# =============================================================================
        
    def Disp_words(self,word_arr):
       for i in range(len(word_arr)):                        
            large_text=pg.font.Font(pg.font.get_default_font(),100)
            time.sleep(0.01)
            disp.fill(gray)
            pg.display.update()
            if i!=self.tar_pos:
                text_surface, text_box=self.distractor_objects(word_arr[i], large_text)
            else:
                text_surface, text_box=self.target_objects(word_arr[i], large_text)
            text_box.center=((disp_width/2,disp_height/2))
            disp.blit(text_surface,text_box)
            pg.display.update()
            time.sleep(0.1)
    
       
        

#word_disp('Are you ready?')
disp_height=800
disp_width=800
sequence_len=22
no_of_trials=4
separation={}  
score=0
result_of_trial=np.zeros(no_of_trials)
result_of_probe=np.zeros(no_of_trials)
response_rcvd={}
probe_resp_rcvd={}
generated_trail={}
probe_present=np.random.choice([0, 1], size=(48,), p=[1./2,1./2])
if __name__ =="__main__":    
    for i in range(no_of_trials):
        separation[i]=np.random.randint(2,8)
        if (int(separation[i]/2) != separation[i]/2 ):
            separation[i] +=1
            
        pg.init()  
        disp=pg.display.set_mode((disp_width,disp_height))
        pg.display.set_caption('First Game')
        generated_trail[i]=Word_Disp(disp_height,disp_width,sequence_len,no_of_trials,separation[i],probe_present[i])
        disp.fill(gray)
        pg.display.update()               
        disp.fill(gray)
        pg.display.update()               
        
        pg.quit()
        
        
        my_resp=self_button.generate_resp()
#        self_button.my_resp.window.mainloop()
        response_rcvd[i]=my_resp.response
        my_prob_resp=probe_resp_button.generate_prob_resp()
        probe_resp_rcvd[i]=my_prob_resp.response
        if response_rcvd[i]==generated_trail[i].selected_target:
            score=score+1
            result_of_trial[i]=1
        else:
            result_of_trial[i]=0
            
        if probe_present[i]==1 and probe_resp_rcvd[i]=='Yes':
            result_of_probe[i]=2# true hit
        elif probe_present[i]==1 and probe_resp_rcvd[i]=='No':
            result_of_probe[i]=-1# miss
        elif probe_present[i]==0 and probe_resp_rcvd[i]=='Yes':
            result_of_probe[i]=-2 #false detection
        elif  probe_present[i]==0 and probe_resp_rcvd[i]=='No':
            result_of_probe[i]= 1 #
#            print('Congratulations, you have done it correctly')
        print('Trial No,', i+1, ', Sequence generated, ', generated_trail[i].shuffled_arr, ',', 'Target Presented, '+ generated_trail[i].selected_target +', ' + 'Response Given, ' + response_rcvd[i] + ', '+'Was Probe Present? ,', probe_present[i], ', Separation if req: ,', separation[i], ',Result of Trial: ,' , result_of_trial[i], ', Result of Probe:, ',result_of_probe[i])
       
        
# =============================================================================
#crashed= False
#while not crashed:
#      for event in pg.event.get():
#          if event.type == pg.QUIT:
#              crashed = True
#      final_word_arr,current_tar,separation = word_arr_generator(raw_arr,target_array,probe)
#      Disp_words(final_word_arr)
# =============================================================================
     
     
           