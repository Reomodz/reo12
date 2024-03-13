import os
import sys
import marshal

def deobfuscate_code(obfuscated_code):
    return marshal.loads(obfuscated_code)

def MainMenu():
    try:
        os.system('clear')  # Clear the screen
        banner()
        
        file = input("Enter the name of the obfuscated file: ")
        if not os.path.isfile(file):
            sys.exit("\nFile Not Found!")
        
        with open(file, 'rb') as f:  # Open file in binary mode
            obfuscated_code = f.read()

        decrypted_code = deobfuscate_code(obfuscated_code)
        print("\nDecrypted Code:\n")
        print(decrypted_code.decode())  # Decode bytes to string for printing
        
    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit()

def banner():
    print(' ╔═════════════════════════════════╗\n ║          PyObfuscate            ║\n ║  Simple Python Code Obfuscator  ║\n ║  Author : Tahmid Rayat          ║\n ║  Github : Github.com/HTR-TECH   ║\n ╚═════════════════════════════════╝\n')

if __name__ == "__main__":
    MainMenu()
