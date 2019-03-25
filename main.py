import pyperclip
import time
import os


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


def cls():
    """
    Commented out - bootleg "clear console" for Pycharm,
    use while writing, and switch to "os.system..." line when
    packing into .exe

    for getting coordinates:
    time.sleep(2)
    print(pyautogui.position())

    launch program, and move cursor to the simulated console window,
    after 2s you'll get coordinates to put as pyautogui.click() arguments
    :return:
    """

    # time.sleep(0.1)
    # pyautogui.click(x=778, y=832)
    # pyautogui.hotkey('ctrl', 'l')

    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:
        cls()
        print("1. Convert a '.txt' file")
        print("2. Convert word/sentence")
        print("0. Exit")
        op = input()
        cls()
        if op == '1':
            filename = input("Drag and drop file you want to convert,\nand press Enter: ")

            if filename.endswith(".txt"):
                with open(filename, 'r') as file:
                    filelines = (file.read()).splitlines()

                converted_file_lines = []

                if set(''.join(filelines)) == {'0', '1'}:

                    for line in filelines:
                        converted_file_lines.append(text_from_bits(line))
                else:
                    for line in filelines:
                        converted_file_lines.append(text_to_bits(line))

                with open(filename, 'w') as file:
                    file.write("\n".join(converted_file_lines))
            print('Your file was converted')
            time.sleep(3)
        elif op == '2':
            while True:
                cls()
                sentence = input('Write or copy a word/sentence or binary sequence:\n')
                bin_sentence = None
                x = None
                try:
                    bin_sentence = "".join(sentence.split())
                    if set(bin_sentence) == {'0', '1'}:
                        x = True
                except:
                    x = False

                if x:
                    # binary to text

                    sentence = text_from_bits(bin_sentence)

                elif not x:
                    # text to binary

                    sentence = text_to_bits(sentence)
                    pyperclip.copy(sentence)

                print(sentence)
                control = input("Sentence was copied to clipboard,"
                                "\npress any button to continue, press 'Q' to go back to menu\n")

                if control.casefold() == 'q':
                    break

        else:
            break


if __name__ == '__main__':
    main()
