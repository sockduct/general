####################################################################################################
# Note:  This code won't work on Windows from the interpreter because sub-processes in Windows
#        don't inherit everything from their parent like they do in Posix-type systems using
#        fork.  It works fine when run as a script.  This code will work fine from Posix systems
#        either as a script or from the interpreter.
#
#        From StackOverflow:  This is happening because on Windows, worker() needs to be pickled
#        and sent to the child process via IPC. In order for the child to unpickle worker(), it
#        needs to be able to import it from the parent's __main__ module. When this happens in a
#        normal Python script, the child can re-import your script, and __main__ will contain all
#        the functions declared at the top-level of your script, so it works fine. However, in the
#        interactive interpreter, functions you've defined while in the interpreter can't simply be
#        re-imported from a file like in a normal script, so they will not be in __main__ in the
#        child. 
#
import multiprocessing

def worker(num):
    '''multi-process worker function'''
    print('Worker {}:  {}'.format(multiprocessing.current_process(), num))
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()

