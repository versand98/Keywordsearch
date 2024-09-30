# Imports
import time
import os

# Forklaring av programmet
print('\nVelkommen til \033[1mnøkkelordsøkeren\033[0m...\n')
time.sleep(2)
print('Dette programmet finner alle forekomster av \033[4mordet\033[0m du leter etter i valgt dokument/fil.')
time.sleep(2)
print('Skriv først inn navent på filen + filforlengelsen (f.eks: dokument.pdf) og klikk på \033[4mentertasten\033[0m.')
time.sleep(2)
print('Skriv så inn ditt \033[1mnøkkelord\033[0m. og klikk på \033[4mentertasten\033[0m.') 
time.sleep(2)
print('Etter du har skrevet inn \033[1mnøkkelordet\033[0m, vil programmet hente ut alle forekomster av setningen som omringer ordet + setningen før og etter.\n')
time.sleep(4)

def find_filename():
    ask_again = True
    while ask_again == True:

        filename = input('Skriv inn navnet på filen (med filforlengelse): ')
        search_directory = os.path.expanduser('~/Documents/Python') # Define the path to the user's folder where document is placed
        full_path = os.path.join(search_directory, filename) # Construct the full path
        
        if os.path.isfile(full_path):
            print(f'Fil funnet i sti: "{full_path}"')
            break
        else:
            print(f'\nFil "{filename}" IKKE funnet i søk.')



if __name__=='__main__':
    find_filename()


'''
def progress_bar(duration):
    time.sleep(5)
    print()
    total_steps = 20  # Length of the progress bar
    for step in range(total_steps):
        time.sleep(duration / total_steps)  # Distributes sleep time evenly
        progress = ("#" * (step + 1)).ljust(total_steps)
        print(f"\r[{progress}] {int((step + 1) / total_steps * 100)}%", end="", flush=True)

progress_bar(3)  # 3-second progress bar
'''
