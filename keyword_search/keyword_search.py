# Imports
import time
import os
import pdfplumber

# Forklaring av programmet
print('\nVelkommen til \033[1mnøkkelordsøkeren\033[0m...\n')
time.sleep(2)
print('Dette programmet finner alle forekomster av \033[4mordet\033[0m du leter etter i valgt dokument/fil.')
time.sleep(1)
print('Skriv først inn navent på filen + filforlengelsen (f.eks: dokument.pdf) og klikk på \033[4mentertasten\033[0m.')
time.sleep(1)
print('Skriv så inn ditt \033[1mnøkkelord\033[0m. og klikk på \033[4mentertasten\033[0m.') 
time.sleep(1)
print('Etter du har skrevet inn \033[1mnøkkelordet\033[0m, vil programmet hente ut alle forekomster av setningen som omringer ordet + setningen før og etter.')
time.sleep(3)

# Funksjon for å finne filnavn
def find_filename():
    while True:

        # Finner filsti til dokument (hvis fil eksisterer)
        filename = input('\nSkriv inn navnet på filen (med filforlengelse): ')
        search_directory = os.path.expanduser('~/Documents/Python') # Forhåndsdefinerer stien til brukerens mappe hvor dokumentet må plasseres
        full_path = os.path.join(search_directory, filename) # Gjengir hele filstien
        
        if os.path.isfile(full_path):
            print(f'Fil funnet i sti: "{full_path}"\n')
            
            bruke_fil = input('Vil du bruke denne filen? [ja/nei]: ').lower()
            
            if bruke_fil == 'ja':
                keyword = input('\nSkriv in nøkkelordet: ')

                # Åpne pdf-filen
                with pdfplumber.open(full_path) as pdf:
                    #Iterer gjennom hver side i pdf-en
                    for page in pdf.pages:
                        # Hent ut teksten og ta hensyn til layout
                        text = page.extract_text(layout=True) # layout=True hjelper å opprettholde kolonnestruktur

                        
                        print(text)

        else:
            print(f'Fil "{filename}" IKKE funnet i {full_path}.\n')

'''
def find_keyword():
    while True:
        bruke_fil = input('Vil du bruke denne filen? [ja/nei]: ').lower()
        if bruke_fil == 'ja':
            keyword = input('\nSkriv in nøkkelordet: ')
            with pdfplumber.open())
            break
        else:
            print('\nAvslutter...')
            break

'''



if __name__=='__main__':
    find_filename()
    # find_keyword()


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
