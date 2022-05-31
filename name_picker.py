import pygame, sys
from pygame.locals import *
import random

file_name = "students.txt"
temp_names = []

# Initialize program
pygame.init()

# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()

# Setting up color objects
BLUE  = (36, 138, 212)
RED   = (229, 90, 34)
GREEN = (28, 235, 40)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((800,800))
pygame.display.set_caption("Name Picker")

# pick a font you have and set its size
myfont = pygame.font.SysFont("arial", 100)


DISPLAYSURF.fill(BLUE)
pygame.display.update()

#---------------------------
# Open a file and import text information and create data-maps
names_file = open(file_name, "r")
lines = names_file.readlines()

master_dict = {}
count = 0

current_key = ""
for line in lines:
    count += 1
    
    line = line.strip()
    split_line = line.split("\t")
    
  
    if '*' == split_line[0][0]:
        current_key = split_line[0]
        master_dict[current_key] = {}
    else:
    
        temp_key = split_line[0]
        first = int(split_line[1])
        second = int(split_line[2])
        third = int(split_line[3])
        fourth = int(split_line[4])
        master_dict[current_key][temp_key] = [first, second, third, fourth]

names_file.close()
    
"""
master_dict = { '8A': {'noah_8a': [0,0,0,0],'chris_8a': [0,0,0,0]},
                '7A': {'greg_7a': [0,0,0,0],'kate_7a': [0,0,0,0]}
                }
"""
         

#select which class
classes = list(master_dict.keys())
print("Please type the name of a class: ", classes)
value = input()

# create class data map
class_dict = master_dict[value]

selected_name = ""

response = False

# Beginning Game Loop
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
    
            master_dict[value] = class_dict
  
            names_file = open(file_name, "w")            

            for class_code in master_dict:
                names_file.write(class_code)
                names_file.write("\n")
                
                class_dict = master_dict[class_code]
                
                for student_name in class_dict:
                    names_file.write(student_name)
                    names_file.write("\t")
                    names_file.write(str(class_dict[student_name][0]))
                    names_file.write("\t")
                    names_file.write(str(class_dict[student_name][1]))
                    names_file.write("\t")
                    names_file.write(str(class_dict[student_name][2]))
                    names_file.write("\t")
                    names_file.write(str(class_dict[student_name][3]))
                    names_file.write("\n")

            # Close opend file
            names_file.close()
            
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and not response:
                #create a tempory list of names by searching the datamap to find who has the lowest total
                minimum = 300

                for name in class_dict:
                    total = class_dict[name][0]  
                    if total < minimum: #for more randomness, have total < minimum + 1
                        minimum = total
                        

                temp_names = []
                for name in class_dict:
                    total = class_dict[name][0]
                    if total == minimum:
                        temp_names.append(name)
       

                # pick random name from temp names list
                idx = random.randint(0, len(temp_names) - 1)
                selected_name = temp_names[idx] 
                response = True

            if event.key == K_1 and response:
                class_dict[selected_name][0] += 1
                response = False
                
            if event.key == K_2 and response:
                # refused to answer question 
                class_dict[selected_name][0] += 1
                class_dict[selected_name][1] += 1
                response = False
                
            if event.key == K_3 and response:
                # limited answer
                class_dict[selected_name][0] += 1
                class_dict[selected_name][2] += 1
                response = False
                
            if event.key == K_4 and response:
                # strong answer
                class_dict[selected_name][0] += 1
                class_dict[selected_name][3] += 1
                response = False
                
    # print selected name
    DISPLAYSURF.fill(BLUE)
    
    if response:
        pygame.draw.circle(DISPLAYSURF, RED, (50, 50), 50)
        pygame.draw.circle(DISPLAYSURF, WHITE, (50, 150), 50)
    else:
        pygame.draw.circle(DISPLAYSURF, WHITE, (50, 50), 50)
        pygame.draw.circle(DISPLAYSURF, GREEN, (50, 150), 50)
        
    label = myfont.render(selected_name, 1, BLACK)
    ##DISPLAYSURF.blit(label, (300, 300))
    text_rect = label.get_rect(center=(800/2, 800/2))
    DISPLAYSURF.blit(label, text_rect)
   
    # response modification
    pygame.display.update()
    
    FramePerSec.tick(FPS)
