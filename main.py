from concurrent.futures import ThreadPoolExecutor
from spellchecker import SpellChecker
import threading


def correct_word(word):
    spell = SpellChecker(language='pt')
    print(f"\nThread atual: {threading.current_thread().name}, texto:{word}\n")
    return spell.correction(word) or word


def main():
    text = input("Digite seu texto aqui: ")

    words = text.split()

    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = [executor.submit(correct_word, word) for word in words]

        corrected_words = [future.result() for future in futures]

    corrected_text = ' '.join(corrected_words)
    print(corrected_text)


if __name__ == '__main__':
    main()