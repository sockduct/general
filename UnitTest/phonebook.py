####################################################################################################
# Unit Testing with Python - Module 1
####################################################################################################
class Phonebook:
    def __init__(self):
        self.entries = {}
    
    def add(self, name, number):
        self.entries[name] = number
    
    def lookup(self, name):
        return self.entries[name]
    
    def is_consistent(self, verbose=False):
        for elmt in self.entries:
            if verbose:
                print('Examining {}...'.format(elmt))
            for inner in self.entries:
                if verbose:
                    print('Inner entry is {}...'.format(inner))
                # Don't compare element to itself
                if inner == elmt:
                    if verbose:
                        print('Skipping...')
                    continue
                elif str(self.entries[inner]).startswith(str(self.entries[elmt])):
                    if verbose:
                        print('Error:  {} ({}) is a prefix of {} ({})'.format(self.entries[elmt],
                              elmt, self.entries[inner], inner))
                    return False
        return True

    def get_names(self):
        return self.entries.keys()

    def get_numbers(self):
        return self.entries.values()

