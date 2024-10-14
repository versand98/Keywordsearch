# Imports
import time
import os
import pdfplumber

# Forklaring av programmet
print('\nVelkommen til \033[1mnøkkelordsøkeren\033[0m...\n')
time.sleep(2)
print('Dette programmet finner alle forekomster av \033[4mordet\033[0m du leter etter i valgt dokument/fil.')
print('Skriv først inn navent på filen + filforlengelsen (f.eks: dokument.pdf) og klikk på \033[4mentertasten\033[0m.')
print('Skriv så inn ditt \033[1mnøkkelord\033[0m. og klikk på \033[4mentertasten\033[0m.') 
print('Etter du har skrevet inn \033[1mnøkkelordet\033[0m, vil programmet hente ut alle forekomster av setningen som omringer ordet + setningen før og etter.')
time.sleep(3)


class MyFunctions:
    def __init__(self):
        self.filename = None
        self.search_directory = os.path.expanduser('~/Documents/Python') # Forhåndsdefinerer stien til brukerens mappe hvor dokumentet må plasseres
        self.full_path = None

# Funksjon for å finne filnavn
    def find_filename(self):
        while True:

            # Finner filsti til dokument (hvis fil eksisterer)
            self.filename = input('\nSkriv inn navnet på filen (med filforlengelse): ')
           
            self.full_path = os.path.join(self.search_directory, self.filename) # Gjengir hele filstien
            
            if os.path.isfile(self.full_path):
                print(f'Fil funnet i sti: "{self.full_path}"\n')
                break

            else:
                print(f'Fil "{self.filename}" IKKE funnet.\n')
        

    def find_keyword(self):
        while True:
        
            keyword_counter = 0
            keyword = input('\nSkriv in nøkkelordet: ').lower()

            with pdfplumber.open(self.full_path) as pdf:
                #Iterer gjennom hver side i pdf-en
                for page in pdf.pages:
                    # Hent ut teksten og ta hensyn til layout
                    text = page.extract_text(layout=True).lower() # layout=True hjelper å opprettholde kolonnestruktur

                    keyword_counter += text.count(keyword)

            if keyword in text:
                for i, keyword in text:
                    print(i)
                print(f'Totalt antall funn av {keyword}: {keyword_counter}')
                break
                
            else:
                print(f'Ingen treff på {keyword}')

    

                




if __name__=='__main__':
    my_function = MyFunctions()
    my_function.find_filename()
    my_function.find_keyword()


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
