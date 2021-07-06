import os
HERE=os.getcwd()
PATH_METADATA=os.path.join(HERE,'corpus','metadata.xls')
PATH_TXT=os.path.join(HERE,'corpus','text')
import lltk
from tqdm import tqdm
import pandas as pd
import numpy as np

def get_corpus():
    return lltk.Corpus(
        name='AWS',
        path_txt='/Users/tobywarner/Dropbox/textmining/corpora/aws/text',
        path_metadata='/Users/tobywarner/Dropbox/textmining/corpora/aws/metadata.xls'
    )

def get_corpus2():
    return lltk.Corpus(
        name='Chicago1',
        path_txt='/Users/tobywarner/Dropbox/textmining/corpora/chicago/txt',
        path_metadata='/Users/tobywarner/Dropbox/textmining/corpora/chicago/metadata.csv'
    )

def get_corpus3():
    return lltk.Corpus(
        name='MarkMark1',
        path_txt='/Users/tobywarner/Dropbox/textmining/corpora/markmark/txt',
        path_metadata='/Users/tobywarner/Dropbox/textmining/corpora/markmark/metadata.csv'
    )
