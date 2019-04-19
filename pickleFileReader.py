import os
import pickle

def getValue():
    if os.path.isfile('pickle_abc'):
        with open('pickle_abc', 'rb') as f:
            try:
                return (pickle.load(f))
            except Exception:
                pass 
    with open('pickle_abc', 'wb') as f:
        pickle.dump(0, f)
        return (pickle.load(f))

getValue()
