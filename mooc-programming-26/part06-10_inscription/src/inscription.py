addressed_to = input('Whom should I sign this to:')
file_name = input('Where shall I save it:')

with open(file_name, 'w') as example:
    example.write(f'Hi {addressed_to}, we hope you enjoy learning Python with us! Best, Mooc.fi Team')