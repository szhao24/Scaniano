import pygame
import keyboard

# Initialize pygame mixer
pygame.mixer.init()

#Note Dictionary
#May need to update path to note library
note_dictionary = {
    "C4": r"ScanianoProject\noteLib\c4.wav",
    "D4": r"ScanianoProject\noteLib\d4.wav",
    "E4": r"ScanianoProject\noteLib\e4.wav",
    "F4": r"ScanianoProject\noteLib\f4.wav",
    "G4": r"ScanianoProject\noteLib\g4.wav",
    "A4": r"ScanianoProject\noteLib\a4.wav",
    "B4": r"ScanianoProject\noteLib\b4.wav",
    "C5": r"ScanianoProject\noteLib\c5.wav"
}

# Initialize pygame
pygame.init()

note_list = []
#Add notes to list
while (True):
    notes = input("input note (or type 'play'): ")
    if (notes == 'play'):
        break;
    elif notes in note_dictionary:
        note_list.append(notes)
    else:
        print("Please input a valid note")

#viewing note list for debugging    
print(note_list)

list_index = 0
print("Press space to play the next note")

#play notes from queue at the pace of user tapping space bar
while list_index < len(note_list):
    if keyboard.is_pressed("space"):
        sound = pygame.mixer.Sound(note_dictionary[note_list[list_index]])
        sound.play()
        list_index += 1
        while keyboard.is_pressed("space"):
            pass
    if keyboard.is_pressed("q"):
        break

#necessary delay for final note as there is no audio with no delay for pygame
pygame.time.delay(int(2000))

pygame.quit()
