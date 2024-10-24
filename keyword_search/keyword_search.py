# Imports
import time
import os
import pdfplumber
import re

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
        self.txt_filename = None  # Sti for konvertert .txt fil

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


    # Konverterer pdf til tekstfil
    def convert_pdf_to_txt(self):
        self.txt_filename = os.path.splitext(self.full_path)[0] + '.txt'
        
        with pdfplumber.open(self.full_path) as pdf:
            with open(self.txt_filename, 'w', encoding='utf-8') as txt_file:
                for i, page in enumerate(pdf.pages):
                    # Extract text without layout
                    text = page.extract_text(layout=False)
                    if text:
                        cleaned_text = self.clean_text(text)  # Post-process the text
                        txt_file.write(f"\n--- Page {i + 1} ---\n")
                        txt_file.write(cleaned_text)
                        txt_file.write('\n')  # Separate pages with a new line
        print(f"PDF er konvertert til tekstfil: {self.txt_filename}\n")



    def clean_text(self, text):
        # 1. Merge lines that don't end with punctuation (., !, ?)
        cleaned_text = re.sub(r'(?<![.!?])\n', ' ', text)  # Merge lines without sentence-ending punctuation

        # 2. Remove multiple line breaks and replace them with a single newline
        cleaned_text = re.sub(r'\n+', '\n', cleaned_text)

        # 3. Replace multiple spaces with a single space
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

        # 4. Fix broken words with hyphens at line ends (e.g., "exam-\nple" -> "example")
        cleaned_text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', cleaned_text)

        # 5. Ensure a single space after punctuation marks like ., !, or ?
        cleaned_text = re.sub(r'(?<=[.!?]) +', ' ', cleaned_text)

        # 6. Optional: Strip leading and trailing whitespace
        cleaned_text = cleaned_text.strip()

        return cleaned_text


        
    # Søker etter nøkkelord i .txt filen og printer ut fulle setninger der den finnes
    def find_keyword_in_txt(self):
        while True:
            keyword_counter = 0
            keyword = input('\nSkriv inn nøkkelordet: ').lower()

            # Leser filinnholdet i .txt
            with open(self.txt_filename, 'r', encoding='utf-8') as txt_file:
                text = txt_file.read().lower()  # Read the entire content as lowercase

            # Split the text into sentences (using '.' as a sentence delimiter for simplicity)
            #sentences = text.split('.')
            sentences = re.split(r'(?<=[.!?])\s+', text)

            # Søk etter nøkkelrodet i setninger og print de som matcher
            matching_sentences = []
            for sentence in sentences:
                if keyword in sentence:
                    matching_sentences.append(sentence.strip())
                    keyword_counter += sentence.count(keyword)

            if matching_sentences:
                self.progress_bar(3)
                print("\nSetninger med nøkkelordet:\n")
                for sentence in matching_sentences:
                    print(f'- {sentence.strip()}.')

                print(f'\nTotalt antall funn av "{keyword}": {keyword_counter}\n')
                break
            else:
                print(f'Ingen treff på "{keyword}". Prøv på nytt.')

    # Progresjonsbaranimasjon
    def progress_bar(self, duration):
        time.sleep(5)
        print()
        total_steps = 20
        for step in range(total_steps):
            time.sleep(duration / total_steps)
            progress = ("#" * (step + 1)).ljust(total_steps)
            print(f"\r[{progress}] {int((step + 1) / total_steps * 100)}%", end="", flush=True)
        print()


if __name__=='__main__':
    my_function = MyFunctions()
    my_function.find_filename()
    my_function.convert_pdf_to_txt()
    my_function.find_keyword_in_txt()

