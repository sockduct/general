def greet():
    print('Greetings!')

if __name__ == '__main__':
    greet()
else:
    print('__name__ not "__main__", but {} - no greeting'.format(__name__))

