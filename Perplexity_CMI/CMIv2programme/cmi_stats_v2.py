###################################################################################
#
# Code-Mixing Corpus Calculation
# Björn Gambäck, NTNU 2014-2016.
# contact: <gamback@idi.ntnu.no>
#
# For corpora whose documents contain words tagged with language identifiers.
# 
###################################################################################
#
# Prerequisites:
# 1. NLTK
# 2. Python >= v3
#
###################################################################################
#
# Usage (if you're using a predefined corpus and tagset, skip to step 4 or 5!):
#
# 1. Define the tagset of the corpus, unless it's one of the predefined tagsets
#    given in the file cmi_tagsets.py (see that file for descriptions):
#    a. dastags used by Das and Gambäck
#    b. nitatags used in the NITA corpora
#    c. ndtags used by Nguyen & Dogruöz
#    d. vyastags used by Vyas et al.
#    e. firetags used in the FIRE shared task
#    f. csws14tags used in the EMNLP 2014 CS workshop shared task
#    g. csws16tags used in the EMNLP 2016 CS workshop shared task
#
# 2. If introducing a new tagset, define
#    a. which tags are language tags in the langtags/1 mapping in cmi_tagsets.py.
#    b. which tags map to which language. See further maptags/3 below.
#    Also check if some tags/words need special treatment, see cmi_one_utterance/3.
#
# 3. Define a corpus reader class, unless it's one of the predefined corpus readers
#    given in the file cmi_corpus_reader.py.
#
# 4. Add the corpus file name and its language ID to codemix/1 in cmi_corpus_reader.py.
#   (The corpora file names are currently hardcoded in that function. Sorry for that!)
#
# 5. Calculate the code-mixing of the entire corpus using cmi_stats/2.
#    A typical usage is:
#
#       >>> cmi_stats('ned', tagsets.ndtags)
#
#    where 'ned' says that the Dutch corpus should be the one processed and
#    tagsets.ndtags that it's annotated with the tagset of Nguyen & Dogruöz.
# 
#    Another example:
#
#       >>> cmi_stats('cswsest', tagsets.csws16tags)
#
#    where 'cswsest' is the 2016 EMNLP code-switching workshop English-Spanish
#    training corpus and tagsets.csws16tags that year's version of the tagset.
#
#    The system output statistics come in seven groups, as follows:
#       1. Cc = the overall CMI value for the entire corpus.
#       2. The total number of utterances and the number of code-mixed utterances.
#       3. The fraction (%) of mixed and non-mixed utterances, respectively.
#       4. The average code-mixing per utterance (Cu) in the mixed utterances
#           and overall in the corpus.
#       5. The number of utterance-internal code-switching points overall;
#           average number of switches inside the mixed utterances and
#           average for all utterances; the number of switches between utterances
#           and the fraction of switches between utterances.
#       6. The fraction of mixed utterances in different Cu intervals together with
#           the average number of switch points in each of those intervals.
#       7. The number and fraction of words annotated with each tag in the tagset.
#
###################################################################################

###################################################################################
#
# The Code-Mixing Index is further described in the following two papers:
#
# [CMI v2] Gambäck, B. and Das, A.: Comparing the level of code-switching in corpora.
# Proc. of the 10th International Conference on Language Resources and Evaluation (LREC).
# Portoroz, Slovenia (May 2016), pp 1850–1855.
#
# [CMI v1] Gambäck, B. and Das, A.: On measuring the complexity of code-mixing.
# Proc. of the 1st Workshop on Language Technologies for Indian Social Media (Social-India).
# Goa, India (Dec 2014), pp. 1-7.
#
###################################################################################

import cmi_tagsets as tagsets
import cmi_corpus_reader as creader


#########################################################################
#                                                                       #
#                       MAPPING OF LANGUAGE TAGS                        #
#                      FOR THE PREDEFINED TAGSETS                       #
#                  (See the definitions of the predefined               #
#                   tagsets at the beginning of the file.)              #
#                                                                       #
#########################################################################


#########################################################################
# Calculate the number of words tagged by each language tag, including
# defining which language any mixed words belong to, for each tagset.
#
# Return the number of words tagged as belonging to any language
# and the number of non-language words in the utterance, as well as
# the number of words belonging to the utterance's matrix language
# (dominating language) and that matrix language itself.
#
def maptags(tags, tagset, prevmatrix):

    if tagset == tagsets.dastags:
        eng = tags[0] + tags[1] + tags[2]   # EN + EN+{HI|BN}_SUFFIX
        bng = tags[3] + tags[4]             # BN + BN+EN_SUFFIX
        hnd = tags[5] + tags[6]             # HN + HN+EN_SUFFIX
        #ne = tags[7]  + tags[10]
        #acro = tags[11] + tags[13] + tags[14]
        ## While this option is based on the suffixes of NEs and ACROs
        eng += tags[8] + tags[12]           # eng above + {NE|ACRO}+EN_SUFFIX
        bng += tags[9] + tags[13]           # bng above + {NE|ACRO}+BN_SUFFIX
        hnd += tags[10] + tags[14]          # hnd above + {NE|ACRO}+HI_SUFFIX
        ne = tags[7]
        acro = tags[11]

        other = tags[15] + tags[16]
        nonlang = ne + acro + other
        lang = eng + bng + hnd
        #domlang = max(eng,bng,hnd)       
        lang1 = eng
        lang2 = max(bng,hnd)

    elif tagset == tagsets.nitatags:
        eng = tags[0]
        bng = tags[1]
        hnd = tags[2]
        mix = tags[3]
        nonlang = tags[4] + tags[5] + tags[6] + tags[7]
        lang = eng + bng + hnd + mix
        lang1 = eng
        lang2 = max(bng,hnd)

    elif tagset == tagsets.ndtags:
        lang1 = tags[0] # ned
        lang2 = tags[1] # tur
        nonlang = tags[2]
        lang = lang1 + lang2

    elif tagset == tagsets.vyastags:
        lang1 = tags[0]
        lang2 = tags[1]
        error = tags[2] + tags[3]
        nonlang = 0
        lang = lang1 + lang2 + error

    elif tagset == tagsets.firetags:
        eng = tags[0] + tags[1] + tags[2]
        bng = tags[3] + tags[4]
        hnd = tags[5] + tags[6]
        gur = tags[7] 
        kan = tags[8]
        mix = tags[9]
        nonlang = tags[10]
        lang = eng + bng + hnd + gur + kan + mix
        #domlang = max(eng,bng,hnd,gur,kan)
        lang1 = eng
        lang2 = max(bng,hnd,gur,kan)

    elif tagset == tagsets.csws14tags:
        lang1 = tags[0]
        lang2 = tags[1]
        mix = tags[2] + tags[3]
        nonlang = tags[4] + tags[5]
        lang = lang1 + lang2 + mix

    elif tagset == tagsets.csws16tags:
        lang1 = tags[0]
        lang2 = tags[1]
        fw = tags[2]
        mix = tags[3] + tags[4]
        nonlang = tags[5] + tags[6] + tags[6]
        lang = lang1 + lang2 + fw + mix
        
    else:
        print("Unknown tagset")

    # This isn't strictly correct for corpora mixing more than two languages,
    # since no inter-utterance switchpoint will be added in case the matrix
    # language of two utterances switches between two non-English languages.
    # (Since lang1 is here assumed always to be the number of English words,
    # while lang2 gives the most frequent other language of the utterance.)
    # Needs fixing! - BG 160322 
    if lang1 > lang2:
        matrixlang = 'lang1'
        nummatrix = lang1
    elif lang2 > lang1:
        matrixlang = 'lang2'
        nummatrix = lang2
    else:
        matrixlang = prevmatrix
        nummatrix = lang1

    return lang, nonlang, nummatrix, matrixlang

#########################################################################
#                                                                       #
#                      Cu = CODE-MIXING PER UTTERANCE                   #
#                                                                       #
#########################################################################

#########################################################################
# Check if the switchpoint counter P should be increased.
#
# Increase P if the current word's tag is one of the language tags _and_
# the most recent preceeding language-tagged word had another language tag
# (which is given by the value of the currlang argument).
#
def switchpoint(tag, tagset, P, currlang):
    langs = tagsets.langtags(tagset)
    if currlang == 0 and (tag in langs):
        # first language tagged word: change currlang, but not P
        return P, tag
    elif tag != currlang and (tag in langs):
        # increase P and change currlang
        return P+1, tag
    else:
        # no change of P and currlang
        return P, currlang
    
#########################################################################
# Calculate Cu, the code-mixed index for one utterance.
#
# Insert an intra-utterance switch point, P, for each language change
# inside the utterance, as returned from the switchpoint/4 function. 
# Add an inter-utterance switch, delta, if the utterance's matrix language
# differs from prevmatrix, the matrix language of the previous utterance.
#
# The relevant formula used to calculate Cu for an utterance x is:
#
#   Cu(x) = 100 * [N(x)- max{t}(x) + P(x)] / 2*N(x)   : N(x) > 0
#   Cu(x) = 0   : N(x) = 0
#
# where N(x) is the number of tokens that belong to any of the languages in
# the utterance x (i.e., all the tokens except for language independent ones);
# max{t}(x) is the number of tokens in x belonging to the matrix language
# (i.e., the most frequent language in the utterance x); and
# P(x) the number of switching points inside the utterance x.
#
# The second clause defines Cu(x) to be 0 for utterances containing
# no words that belong to any of the languages in the corpus (N=0).
# Cu is also 0 for monolingual utterances (since then max{t}=N and P=0).
# 
def cmi_one_utterance(utterance, tagset, prevmatrix):
    P = 0
    currlang = 0
    tags = [0 for x in range(len(tagset))]
    for i in range(len(utterance)):
        word,tag = utterance[i]
        if word:
            # special cases for words that contain unwanted symbols
            if word[0] == '[':
                if word == '[object' or word == '[img':
                    # for Nguyen & Dogruöz' NED-TUR corpus, where html
                    # links sometimes are prefixed by '[object' or '[img'.
                    # those superfluous prefixes are thus removed here.
                    continue
                else:
                    # for the FIRE corpora, where NEs sometimes are
                    # included in brackets, that must be removed.
                    tags[len(tagset)-1] += 1
                    continue
        if tag == '' or tag is None:
            print("No tag for word", word)
        elif tag in tagset:
            tags[tagset.index(tag)] += 1
            P, currlang = switchpoint(tag, tagset, P, currlang)
        else:
            # for Das & Gambäck's ENG-BNG corpus, where suffix tags can
            # be prefixed by 'wlcm:'; that prefix needs to be stripped.
            tail = tag.partition(':')[2]
            if tail in tagset:
                tags[tagset.index(tail)] += 1
            else:
                print("Unknown tag", tag, "for word", word, "adding to UNDEF")
                tags[len(tagset)-1] += 1

    lang, nonlang, nummatrix, matrixlang = maptags(tags, tagset, prevmatrix)

    # add an inter-utterance switch point if the matrix languages differ
    if matrixlang == prevmatrix or prevmatrix == 0:
        delta = 0
    else:
        delta = 1
    
    if lang == 0:
        return 0, P, delta, tags, prevmatrix
    else:
        return 1 - (nummatrix - P)/lang, P, delta, tags, matrixlang

#########################################################################
#                                                                       #
#                              MAIN ROUTINE                             #
#                      Cc = CODE-MIXING FOR A CORPUS                    #
#                                                                       #
#########################################################################

#########################################################################
# Calculate code-mixed index and tag usage for an entire corpus
#
# The relevant formula used to calculate Cc of an utterance x is:
#
#   Cc(x) = 100/U * [ 1/2 * Sum{1 - [max{t}(x)-P(x)]/N(x) + delta(x)} + [5/6]*S ]
#
# where U is the total number of utterances in the corpus
# and S the number of utterances that contain any switching.
#
# The Sum is over all the utterances in the corpus (so x = 1 to U);
# max{t}(x) is the number of tokens in each utterance x belonging to
# its matrix language (i.e., the most frequent language in the utterance);
# P(x) is the number of switching points inside each utterance x;
# N(x) is the number of tokens that belong to any of the languages in
# the utterance (i.e., all the tokens except for language independent ones);
# delta(x) is 1 if a switching point precedes the utterance and 0 otherwise.
#
# The 5/6 weighting of S (the number of utterances containing switching)
# comes from the "Reading Ease" readability score [Flesch 1948] which,
# based on psycho-linguistic experiments, similarly weights the frequency
# of words per sentence as 1.2 times the number of syllables per word.
# 
def cmi_stats(lang, tagset):

    # initialisation
    nonmix = 0
    mix = 0
    cmitot = 0
    Ptot = 0
    cmi10 = cmi20 = cmi30 = cmi40 = cmiinf = 0
    P10 = P20 = P30 = P40 = Pinf = 0
    inter = 0
    matrixlang = 0
    tagstot = [0 for x in range(len(tagset))]

    corpus = creader.corpus_reader(lang)
    utterances = corpus.tagged_sents()
    num = len(utterances)
    if num == 0:
        print("Empty corpus")
        return

    # Calculate Cu, the CMI value for each utterance, as well as the
    # switch-points, P (intra-utterance) and delta (inter-utterance)
    for i in range(num):
        cmi, P, delta, tags, matrixlang = cmi_one_utterance(utterances[i], tagset, matrixlang)
        inter += delta
        for x in range(len(tagset)):
            tagstot[x] += tags[x]
        if cmi == 0:
            nonmix += 1
        else:
            mix += 1
            cmitot += cmi + delta
            Ptot += P

            # to produce statistics for different CMI intervals
            cmi *= 50
            if cmi <= 10:
                cmi10 += 1
                P10 += P
            elif cmi <= 20:
                cmi20 += 1
                P20 += P
            elif cmi <= 30:
                cmi30 += 1
                P30 += P
            elif cmi <= 40:
                cmi40 += 1
                P40 += P
            else:
                cmiinf += 1
                Pinf += P

    # Calculate Cc, the mixing of the entire corpus
    cmitot = cmitot/2
    Cc = (cmitot + 5*mix/6) / num
    
    # Print CMI values and overall corpus statistics
    print("\n***********************************")
    print("Language / corpus:", lang)
    print()
    print("Cc:                   {:6.2f}".format(100 * Cc))
    print()
    print("Num of utterances:    {:6d}".format(num))
    print("Num of mixed:         {:6d}".format(mix))
    #print("Num of tokens:        {:6d}".format(len(corpus.words())))
    #print("Num of unique tokens: {:6d}".format(len(set(corpus.words()))))
    print()
    print("Fraction non-mixed:   {:6.2f}".format(100 * nonmix / num))
    print("Fraction mixed:       {:6.2f}".format(100 * mix / num))
    print()
    if mix > 0:
        print("Average Cu mixed:     {:6.2f}".format(100 * cmitot / mix))
    print("Average Cu total:     {:6.2f}".format(100 * cmitot / num))
    print()
    print("Num of switches:      {:6d}".format(Ptot))
    if mix > 0:
        print("Average P mixed:      {:6.2f}".format(Ptot / mix))
    print("Average P total:      {:6.2f}".format(Ptot / num))
    print("Num of interswitches: {:6d}".format(inter))
    print("Fraction interswitch: {:6.2f}".format(100 * inter / num))
    print()

    # Print statistics for different CMI intervals
    print("Fraction 0 < C <= 10: {:6.2f}".format(100 * cmi10 / num))
    if cmi10 > 0:
        print("Avg P for C = (0,10]: {:6.2f}".format(P10 / cmi10))
    print("Fraction 10 < C <= 20:{:6.2f}".format(100 * cmi20 / num))
    if cmi20 > 0:
        print("Avg P for C = (10,20]:{:6.2f}".format(P20 / cmi20))
    print("Fraction 20 < C <= 30:{:6.2f}".format(100 * cmi30 / num))
    if cmi30 > 0:
        print("Avg P for C = (20,30]:{:6.2f}".format(P30 / cmi30))
    print("Fraction 30 < C <= 40:{:6.2f}".format(100 * cmi40 / num))
    if cmi40 > 0:
        print("Avg P for C = (30,40]:{:6.2f}".format(P40 / cmi40))
    print("Fraction C > 40:      {:6.2f}".format(100 * cmiinf / num))
    if cmiinf > 0:
        print("Avg P for C > 40:     {:6.2f}".format(Pinf / cmiinf))
    print()    

    # Print the number of words annotated with each tag 
    print("\n******** Tags ***********  %  *****")
    w = 0
    for x in range(len(tagset)):
        w += tagstot[x]
    for x in range(len(tagset)):
        print(tagset[x].ljust(15), repr(tagstot[x]).rjust(6), " {:6.2f}".format(100*tagstot[x]/w))
    print("Total:", repr(w).rjust(15))
    print("\n***********************************\n\n")


#########################################################################
#                                                                       #
#                              HELP ROUTINES                            #
#                                                                       #
#########################################################################

#########################################################################
# Help routines for debugging and printing
#
def count_tag(tag, utterances, corpus):
    dict = {}
    for i in range(utterances):
        for w,t in corpus.tagged_sents()[i]:
            if t == tag:
                if w in dict:
                    dict[w] += 1
                else:
                    dict[w] = 1
    return dict

### typical usage
# >>> print_dict(count_tag('UNIV', 100, codemix('bng')))
#
def print_dict(dict):
    for i in range(1,100):
        print("***** {:3d} *****".format(i))
        for a,b in dict.items():
            if b == i:
                print(a)

