def encrypt_decrypt_image(path, key):
    try:
        path = path.strip('"')  # Remove surrounding quotes if any
        
        print('The path of the file:', path) #storing file path
        print('Key for encryption/decryption:', key) #storing key for encryption
        
        with open(path, 'rb') as fin: #reads the image with the image path provided and opens it in read binary mode
            image = fin.read()        #The with statement ensures the file is properly closed after the block executes.
                                      #The as fin part assigns the file object returned by open(path, 'rb') to the variable fin.
                                      # use fin to read from or write to the file.
      
        image = bytearray(image) # Converting image into byte array 
                                 # It is easier to perform encryption easily on numeric data
        
        for index, values in enumerate(image): # Performing XOR operation on each value of bytearray
            image[index] = values ^ key
        
        with open(path, 'wb') as fin: # Opening the file and writing encrypted data to the image
            fin.write(image)
        
        print('Operation Done...')
    
    #FileNotFoundError: Catches errors when the specified file path is incorrect.
                             #ValueError: Catches errors when the entered key is not an integer.
                                        #Exception: Catches all other exceptions and prints a user-friendly error message.
    except FileNotFoundError:
        print('Error: The file was not found. Please check the path and try again.')
    except IOError as e:
        print(f'IO Error: {e}')
    except ValueError as ve:
        print(f'Error: {ve}')
    except Exception as e:
        print(f'An error occurred: {e}')

def main():
    print("Starting the encryption/decryption script...")
    try:
        operation = input('Do you want to (E)ncrypt or (D)ecrypt an image? (E/D): ').strip().upper()
        #strip function to remove whitespace 
        #upper function to change lowercase letter to uppercase
        
        if operation not in ('E', 'D'):
            raise ValueError('Invalid operation. Please enter E for encryption or D for decryption.')
        
        path = input(r'Enter path of the Image: ')
        key = int(input('Enter Key for encryption/decryption of Image: '))
        
        encrypt_decrypt_image(path, key) #function call for encrypting/decrypting image file
    
    except ValueError as ve:
        print(f'Error: {ve}')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    main()

