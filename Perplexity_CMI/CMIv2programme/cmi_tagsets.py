###################################################################################
#
# Tagsets Used by Code-Mixing Corpus Readers
# Björn Gambäck, NTNU 2014-2016.
# contact: <gamback@idi.ntnu.no>
#
###################################################################################

#########################################################################
#                                                                       #
#                           PREDEFINED TAGSETS                          #
#                                                                       #
#########################################################################

# Tagset used by Das & Gambäck
# * Das, A. and Gambäck, B. (2013).
# "Code-Mixing in Social Media Text: The Last Language Identification Frontier?"
# Traitement Automatique des Langues, 54(3):41–64.
# * Das, A. and Gambäck, B. (2014).
# "Identifying languages at the word level in code-mixed Indian social media text."
# Proc. of the 11th International Conference on Natural Language Processing (ICON),
# pages 169–178, Goa, India.
dastags = ['EN',
          'EN+BN_SUFFIX',
          'EN+HI_SUFFIX',
          'BN',
          'BN+EN_SUFFIX',
          'HI',
          'HI+EN_SUFFIX',
          'NE',
          'NE+EN_SUFFIX',
          'NE+BN_SUFFIX',
          'NE+HI_SUFFIX',
          'ACRO',
          'ACRO+EN_SUFFIX',
          'ACRO+BN_SUFFIX',
          'ACRO+HI_SUFFIX',
          'UNIV',
          'UNDEF']

# Tagset used for the NITA annotated corpora:
# * Jamatia, A., Gambäck, B., and Das, A. (2015).
# "Part-of-speech tagging for code-mixed English-Hindi Twitter and Facebook chat messages."
# Proc. of the 10th International Conference on Recent Advances in
# Natural Language Processing (RANLP), pages 239–248, Hissar, Bulgaria.
# * Rudrapal, D., Jamatia, A., Chakma, K., Das, A. and Gambäck, B. (2015).
# "Sentence Boundary Detection for Social Media Text."
# Proc. of the 12th International Conference on Natural Language Processing (ICON),
# pages 91-97, Trivandrum, India.
# * Jamatia, A., Gambäck, B., and Das, A. (2016).
# "Collecting and Annotating Indian Social Media Code-Mixed Corpora."
# Proc. of the 17th International Conference on Intelligent Text Processing
# and Computational Linguistics (CICLING), Konya, Turkey.
nitatags = ['EN',
          'BN',
          'HI',
          'MIXED',
          'NE',
          'ACRO',
          'UNIV',
          'UNDEF']

# Tagset used by Nguyen, D. and Dogruöz, A. S. (2013).
# "Word level language identification in online multilingual communication."
# Proc. of the Conference on Empirical Methods in Natural Language Processing (EMNLP),
# pages 857–862, Seattle, Washington.
ndtags = ['NL','TR','SKIP']

# Tagset used by Vyas Y., Gella S., Sharma J., Bali K., and Choudhury M. (2014).
# "POS tagging of English-Hindi code-mixed social media content."
# Proc. of the Conference on Empirical Methods in Natural Language Processing (EMNLP),
# pages 974–979, Doha, Qatar.
vyastags = ['E','H','F','O']

# Tagset used for the FIRE 2014 and 2015 shared task annotated corpora.
# Sequiera, R., Choudhury, M., Gupta, P., Rosso, P., Kumar, S., Banerjee, S.,
# Naskar, S.K., Bandyopadhyay, S., Chittaranjan, G., Das, A., and Chakma, K.
# "Overview of FIRE-2015 shared task on mixed script information retrieval."
# Proc. of the 7th Forum for Information Retrieval Evaluation (FIRE),
# pages 21-27, Gandhinagar, India.
firetags = ['E', 'E+BN_SUFFIX', 'E+HI_SUFFIX',
            'B', 'B+EN_SUFFIX',
            'H', 'H+EN_SUFFIX',
            'G',
            'K',
            'MIX',
            'O']

# Tagsets used for the EMNLP code-switching workshop shared task annotation.
# Solorio, T., Blair, E., Maharjan, S., Bethard, S., Diab, M., Gohneim, M.,
# Hawwari, A., AlGhamdi, F., Hirschberg, J., Chang, A., and Fung, P.
# "Overview for the first shared task on language identification in code-switched data."
# Proc. of the 1st Workshop on Computational Approaches to Code Switching, pages 62–72.
# At the 2014 Conference on Empirical Methods in Natural Language Processing, Doha, Qatar. 
csws14tags = ['LANG1',
            'LANG2',
            'MIXED',
            'AMBIGUOUS',
            'NE',
            'OTHER']

# The UNK and FW tags were added to the tagset for the 2016 CS workshop.
csws16tags = ['LANG1',
            'LANG2',
            'FW',
            'MIXED',
            'AMBIGUOUS',
            'NE',
            'OTHER',
            'UNK']

#########################################################################
# Return the mono-lingual language tags, as defined by each tagset.
#
def langtags(tagset):
    if tagset == dastags:
        langs = tagset[0:7]
    elif tagset == nitatags:
        langs = tagset[0:3]
    elif tagset == ndtags:
        langs = tagset[0:2]
    elif tagset == vyastags:
        langs = tagset[0:2]
    elif tagset == firetags:
        langs = tagset[0:9]
    elif tagset == csws14tags:
        langs = tagset[0:2]
    elif tagset == csws16tags:
        langs = tagset[0:3]
    else:
        print("Unknown tagset")

    return langs
