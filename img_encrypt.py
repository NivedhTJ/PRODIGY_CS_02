def encrypt_decrypt_image(path, key):
    try:
        path = path.strip('"') 
        
        print('The path of the file:', path) 
        print('Key for encryption/decryption:', key) 
        
        with open(path, 'rb') as fin: 
            image = fin.read()        
      
        image = bytearray(image) 
        
        for index, values in enumerate(image):
            image[index] = values ^ key
        
        with open(path, 'wb') as fin: 
            fin.write(image)
        
        print('Operation Done...')
    
   
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
        
        if operation not in ('E', 'D'):
            raise ValueError('Invalid operation. Please enter E for encryption or D for decryption.')
        
        path = input(r'Enter path of the Image: ')
        key = int(input('Enter Key for encryption/decryption of Image: '))
        
        encrypt_decrypt_image(path, key) 
    except ValueError as ve:
        print(f'Error: {ve}')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    main()

