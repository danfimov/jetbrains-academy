def choose():
    formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list',
                  'unordered-list', 'new-line']

    formatter = input('Choose a formatter: ')

    if formatter == '!done':
        return True

    if formatter == '!help':
        print('Available formatters: plain bold italic header\
 link inline-code ordered-list unordered-list new-line')
        print('Special commands: !help !done')
        return False

    if formatter not in formatters:
        print('Unknown formatting type or command')
        return False


while True:
    if choose():
        break
