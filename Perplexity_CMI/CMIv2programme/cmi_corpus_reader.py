###################################################################################
#
# Code-Mixing Corpus Readers
# Björn Gambäck, NTNU 2014-2016.
# contact: <gamback@idi.ntnu.no>
#
# For corpora whose documents contain words tagged with language identifiers.
# The corpus reader routines are based on the NLTK Tagged Corpus Reader.
# 
###################################################################################

from nltk.corpus.reader.tagged import *
import cmi_tagsets as tagsets

import io
import codecs

#########################################################################
#                                                                       #
#                  PREDEFINED CORPUS READERS                            #
#                                                                       #
#########################################################################

###################################################################################
#
#    If defining a new corpus reader, it will need to (at least) specify:
#    a. The encoding scheme (e.g., utf8 or utf16).
#    b. The character separating words from tags.
#    c. How utterance boundaries are marked (e.g., by newline characters, '\n').
#    d. Whether paragraph information is included in the corpus.
#
#    Some corpora might not be in an easily processed format and hence could
#    require some preprocessing / cleaning. See the example preprocessing
#    routines for the FIRE anf EMNLP corpora given at the end of this file.
#
###################################################################################

###################### Das & Gambäck ####################################

class HindiCodeMixedCorpusReader(TaggedCorpusReader):
    """
    A reader for Das & Gambäck's Hindi Code-Mixed corpus, using '$' as a separator.
    Utterance boundaries are marked by newline characters ('\n').
    Paragraph information is not included in the corpus, so each paragraph
    returned by ``self.paras()`` and ``self.tagged_paras()`` contains
    a single sentence.
    """
    def __init__(self, root, fileids, encoding='utf8', tagset=None):
        TaggedCorpusReader.__init__(
            self, root, fileids, sep='$',
            word_tokenizer=WhitespaceTokenizer(),
                 sent_tokenizer=RegexpTokenizer('\n', gaps=True),
                 para_block_reader=read_blankline_block,

#            sent_tokenizer=RegexpTokenizer('\n'),
#            para_block_reader=self._read_block,
#            encoding=encoding,
            tagset=tagsets.dastags)

    def _read_block(self, stream):
        return read_regexp_block(stream, r'.*', r'.*_\.')

class BengaliCodeMixedCorpusReader(TaggedCorpusReader):
    """
    A reader for Das & Gambäck's Bengali Code-Mixed corpus, using '£' as a separator.
    Utterance boundaries are marked by newline characters ('\n').
    Paragraph information is not included in the corpus, so each paragraph
    returned by ``self.paras()`` and ``self.tagged_paras()`` contains
    a single sentence.
    """
    def __init__(self, root, fileids, encoding='utf8', tagset=None):
        TaggedCorpusReader.__init__(
            self, root, fileids, sep='£',
#            word_tokenizer=LineTokenizer(),
#            sent_tokenizer=RegexpTokenizer('\n'),
#            para_block_reader=self._read_block,
#            encoding=encoding,
            tagset=tagsets.dastags)

    def _read_block(self, stream):
        return read_regexp_block(stream, r'.*', r'.*_\.')

########################### NITA ########################################

class NITAHindiCodeMixedCorpusReader(TaggedCorpusReader):
    """
    A corpus reader for the UTF-16 NITA EN-HI corpora, using '§' as a separator.
    Utterance boundaries are marked by newline characters ('\n').
    Paragraph information is not included in the corpus, so each paragraph
    returned by ``self.paras()`` and ``self.tagged_paras()`` contains
    a single sentence.
    """
    def __init__(self, root, fileids, encoding='utf16', tagset=None):
        TaggedCorpusReader.__init__(
            self, root, fileids, sep='§',
            word_tokenizer=WhitespaceTokenizer(),
                 sent_tokenizer=RegexpTokenizer('\n', gaps=True),
                 para_block_reader=read_blankline_block,

#            sent_tokenizer=RegexpTokenizer('\n'),
#            para_block_reader=self._read_block,
#            encoding=encoding,
            tagset=tagsets.nitatags)

    def _read_block(self, stream):
        return read_regexp_block(stream, r'.*', r'.*_\.')

class NITABengaliCodeMixedCorpusReader(TaggedCorpusReader):
    """
    A corpus reader for the UTF-16 NITA Bengali Code-Mixed corpus, using '£' as a separator.
    Utterance boundaries are marked by newline characters ('\n').
    Paragraph information is not included in the corpus, so each paragraph
    returned by ``self.paras()`` and ``self.tagged_paras()`` contains
    a single sentence.
    """
    def __init__(self, root, fileids, encoding='utf16', tagset=None):
        TaggedCorpusReader.__init__(
            self, root, fileids, sep='£',
#            word_tokenizer=LineTokenizer(),
#            sent_tokenizer=RegexpTokenizer('\n'),
#            para_block_reader=self._read_block,
#            encoding=encoding,
            tagset=tagsets.nitatags)

    def _read_block(self, stream):
        return read_regexp_block(stream, r'.*', r'.*_\.')

##################### Nguyen & Dogruöz ##################################

class DutchCodeMixedCorpusReader(TaggedCorpusReader):
    """
    A reader for Nguyen & Dogruöz' Dutch-Turkish code-mixed chat corpus,
    using '/' as a separator.
    Utterance boundaries are marked by newline characters ('\n').
    Paragraph information is not included in the corpus, so each paragraph
    returned by ``self.paras()`` and ``self.tagged_paras()`` contains
    a single sentence.
    The tagset marks words as Dutch or Turkish - everything else is 'skip',
    """
    def __init__(self, root, fileids, encoding='utf8', tagset=None):
        TaggedCorpusReader.__init__(
            self, root, fileids, sep='/',
#            word_tokenizer=LineTokenizer(),
#            sent_tokenizer=RegexpTokenizer('\n'),
#            para_block_reader=self._read_block,
#            encoding=encoding,
            tagset=tagsets.ndtags)

    def _read_block(self, stream):
        return read_regexp_block(stream, r'.*', r'.*_\.')

####################### Vyas et al. #####################################

class VyasHindiCodeMixedCorpusReader(TaggedCorpusReader):
    """
    A corpus reader for Vyas et al.'s Hindi Code-Mixed corpus,
    using '/' as a separator.
    Utterance boundaries are marked by newline characters ('\n').
    Paragraph information is not included in the corpus, so each paragraph
    returned by ``self.paras()`` and ``self.tagged_paras()`` contains
    a single sentence.
    """
    def __init__(self, root, fileids, encoding='utf16', tagset=None):
        TaggedCorpusReader.__init__(
            self, root, fileids, sep='/',
            word_tokenizer=WhitespaceTokenizer(),
                 sent_tokenizer=RegexpTokenizer('\n', gaps=True),
                 para_block_reader=read_blankline_block,

#            sent_tokenizer=RegexpTokenizer('\n'),
#            para_block_reader=self._read_block,
#            encoding=encoding,
            tagset=tagsets.vyastags)

    def _read_block(self, stream):
        return read_regexp_block(stream, r'.*', r'.*_\.')

########################### FIRE ########################################
    
class FIRECodeMixedCorpusReader(TaggedCorpusReader):
    """
    A reader for the FIRE shared task code-mixed corpora,
    using '\' as a separator.
    Utterance boundaries are marked by newline characters ('\n').
    Paragraph information is not included in the corpus, so each paragraph
    returned by ``self.paras()`` and ``self.tagged_paras()`` contains
    a single sentence.
    The tagset marks words as English or the Indian language of the
    specific corpus, or affixed, everything else is tagged 'O' (other).
    """
    def __init__(self, root, fileids, encoding='utf8', tagset=None):
        TaggedCorpusReader.__init__(
            self, root, fileids, sep='\\',
#            word_tokenizer=LineTokenizer(),
#            sent_tokenizer=RegexpTokenizer('\n'),
#            para_block_reader=self._read_block,
#            encoding=encoding,
            tagset=tagsets.firetags)

    def _read_block(self, stream):
        return read_regexp_block(stream, r'.*', r'.*_\.')

############### EMNLP Code-Switching Workshop #############################
    
class CSWS14CodeMixedCorpusReader(TaggedCorpusReader):
    """
    A reader for the EMNLP 2014 workshop shared task code-mixed corpora,
    using '/' as a separator.
    Utterance boundaries are marked by newline characters ('\n').
    Paragraph information is not included in the corpus, so each paragraph
    returned by ``self.paras()`` and ``self.tagged_paras()`` contains
    a single sentence.
    The tagset marks words as English or the language of the
    specific corpus, or NE. Everything else is tagged 'other'.
    """
    def __init__(self, root, fileids, encoding='utf8', tagset=None):
        TaggedCorpusReader.__init__(
            self, root, fileids, sep='/',
#            word_tokenizer=LineTokenizer(),
#            sent_tokenizer=RegexpTokenizer('\n'),
#            para_block_reader=self._read_block,
#            encoding=encoding,
            tagset=tagsets.csws14tags)

    def _read_block(self, stream):
        return read_regexp_block(stream, r'.*', r'.*_\.')

class CSWS16CodeMixedCorpusReader(TaggedCorpusReader):
    """
    A reader for the EMNLP 2016 workshop shared task code-mixed corpora,
    using '/' as a separator.
    Utterance boundaries are marked by newline characters ('\n').
    Paragraph information is not included in the corpus, so each paragraph
    returned by ``self.paras()`` and ``self.tagged_paras()`` contains
    a single sentence.
    The tagset marks words as English or the language of the
    specific corpus, or NE. Everything else is tagged 'other'.
    """
    def __init__(self, root, fileids, encoding='utf8', tagset=None):
        TaggedCorpusReader.__init__(
            self, root, fileids, sep='/',
#            word_tokenizer=LineTokenizer(),
#            sent_tokenizer=RegexpTokenizer('\n'),
#            para_block_reader=self._read_block,
#            encoding=encoding,
            tagset=tagsets.csws16tags)

    def _read_block(self, stream):
        return read_regexp_block(stream, r'.*', r'.*_\.')


#########################################################################
# Return a reader for a pre-defined corpus based on the language ID.
# The corpora names are hardcoded here. They shouldn't be, of course.
#
def corpus_reader(lang):
    # When testing on a smaller corpus
    if lang == 'test':
        return NITAHindiCodeMixedCorpusReader('', 'hndtest.txt')

    # Das and Gambäck's English-Bengali corpus
    elif lang == 'bngtw':
        return BengaliCodeMixedCorpusReader('', 'en_bn_hi_lang-Final.txt')

    # The NITA English-Hindi corpora: in total, for tweets and for facebook
    elif lang == 'hndtot':
        return NITAHindiCodeMixedCorpusReader('', '2583_Final_Gold__Lang_UB.txt')
    elif lang == 'hndtw':
        return NITAHindiCodeMixedCorpusReader('', '1181_TW_Final_Gold_Lang_UB.txt')
    elif lang == 'hndfb':
        return NITAHindiCodeMixedCorpusReader('', '1402_FB_Final_Gold_Lang_UB.txt')

    # Nguyen & Dogruöz' Dutch-Turkish corpus 
    elif lang == 'ned':
        return DutchCodeMixedCorpusReader('', 'dong.txt')

    # Vyas et al.'s English-Hindi corpus
    elif lang == 'vyas':
        return VyasHindiCodeMixedCorpusReader('', 'Vyas.txt')

    # The main FIRE English-Indian corpora: Bengali, Hindi, Gujarati and Kannada
    elif lang == 'firebng':
        return FIRECodeMixedCorpusReader('', 'BanglaEnglish_LIonly_AnnotatedDev.txt')
    elif lang == 'firehnd':
        return FIRECodeMixedCorpusReader('', 'HindiEnglish_LIonly_AnnotatedDev.txt')
    elif lang == 'firegur':
        return FIRECodeMixedCorpusReader('', 'GujaratiEnglish_LIonly_AnnotatedDev.txt')
    elif lang == 'firekan':
       return FIRECodeMixedCorpusReader('', 'KannadaEnglish_LIonly_AnnotatedDev.txt')

    # The EMNLP 2014 workshop English-other corpora: Mandarin, Nepali and Spanish
    elif lang == 'cswsman':
        return CSWS14CodeMixedCorpusReader('', 'mandarinTrain.txt')
    elif lang == 'cswsnep':
        return CSWS14CodeMixedCorpusReader('', 'nepali-english-final-training-data.txt')
    elif lang == 'cswsesp':
        return CSWS14CodeMixedCorpusReader('', 'en_es_training_offsets.txt')

    # The EMNLP 2014 workshop Arabic standard/dialectal corpus
    elif lang == 'cswsarb':
        return CSWS14CodeMixedCorpusReader('', 'arabicTrain-clean.txt')

    # The EMNLP 2016 workshop English-Spanish corpora: training and development
    elif lang == 'cswsest':
        return CSWS16CodeMixedCorpusReader('', 'emnlp16_enestrain.txt')
    elif lang == 'cswsesd':
        return CSWS16CodeMixedCorpusReader('', 'emnlp16_enesdev.txt')

    else:
        print('unknown language')

#########################################################################
# Preprocessing routines for some of the corpora.
# The processed corpus is output as "clean.txt".

##########################
# for FIRE corpora containing the original (encoded) strings, too
#
def preprocess_fire(corpus):
    cleanfile = open('clean.txt', 'w')
    orgfile = open(corpus, 'r')
    line = orgfile.readline()
    while line != '':
        newwords=[]
        words = line.split()
        #print(words)
        for word in words:
            #print(word)
            head = word.split('=')[0]
            newwords += head + ' '
        newwords+=("\n")
        cleanfile.write(''.join(newwords))
        line = orgfile.readline()
    cleanfile.close()
    orgfile.close()

##########################
# for EMNLP 2014 CS workshop corpora containing only offsets and annotation
#
def preprocess_csws14(corpus):
    cleanfile = open('clean.txt', 'w')
    orgfile = open(corpus, 'r')
    line = orgfile.readline()
    key = ''
    sentence = []
    while line != '':
        items = line.split()
        if items[0] != key:
            sentence += "\n"
            cleanfile.write(''.join(sentence))
            sentence = []
            key = items[0]
        string = items[0] + ":" + items[2] + "-" + items[3] + "/" + items[4]
        sentence += string + ' '
        line = orgfile.readline()
    cleanfile.write(''.join(sentence))
    cleanfile.close()
    orgfile.close()

##########################
# for EMNLP 2016 CS workshop corpora containing offsets, tokens and annotations
#
def preprocess_csws16(corpus):
    cleanfile = open('clean.txt', 'w', encoding='utf-8')
    orgfile = open(corpus, 'r', encoding='utf-8')
    line = orgfile.readline()
    key = ''
    sentence = []
    while line != '':
        items = line.split()
        if items[0] != key:
            sentence += "\n"
            cleanfile.write(''.join(sentence))
            sentence = []
            key = items[0]
        if len(items) != 6:
            print(items[0] + ":" + items[2]) 
        string = items[0] + ":" + items[-2] + "/" + items[-1]
        sentence += string + ' '
        line = orgfile.readline()
    cleanfile.write(''.join(sentence))
    cleanfile.close()
    orgfile.close()
