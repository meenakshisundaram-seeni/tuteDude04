try:
    with open('sample.txt', 'rt') as file:
        print('Reading File Content:')
        for i, line in enumerate(file, 1):
            print(f'Line {i}: {line.strip()}')
except FileNotFoundError:
    print('Error: The file sample.txt was not found.')
except Exception as err:
    print(f'An unexpected error occurred: {err}')
