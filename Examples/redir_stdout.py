import sys
 
OUTPUT_FILE = 'C:\Temp\example.txt'

def redirect_to_file(text, verbose=False):
    if verbose:
        print 'Redirecting stdout to {}...'.format(OUTPUT_FILE)

    original = sys.stdout
    sys.stdout = open(OUTPUT_FILE, 'w')
    print('This is your redirected text:')
    print(text)
    sys.stdout = original
 
    print('This string goes to stdout, NOT the file!')
 
# Redirecting stdout/stderr:
if __name__ == '__main__':
    redirect_to_file('Python rocks!', verbose=True)

