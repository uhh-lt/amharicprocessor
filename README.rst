Amharic Segmenter and tokenizer
-------------------------------

This is a simple script that split an Amharic document into different
sentences and tokenes. If you find an issue, please let us know in the
GitHub `Issues <https://github.com/uhh-lt/amharicprocessor/issues>`__

The Segmenter is part of the ``Semantic Models for Amharic`` Project
|image0|

Usage 
-------
Install the segmenter: ``pip install amseg``

Tokenization and Segmentation
-------------------------------
Use the following code for sentence segmentation and word tokenization

::

    from amseg.amharicSegmenter import AmharicSegmenter
    sent_punct = [] 
    word_punct = [] 
    segmenter = AmharicSegmenter(sent_punct,word_punct) 
    words = segmenter.amharic_tokenizer("እአበበ በሶ በላ።") 
    sentences = segmenter.tokenize_sentence("እአበበ በሶ በላ። ከበደ ጆንያ፤ ተሸከመ፡!ለምን?")

Outputs

    words = ['እአበበ', 'በሶ', 'በላ', '።']

    sentences = ['እአበበ በሶ በላ።', 'ከበደ ጆንያ፤ ተሸከመ፡!', 'ለምን?']

Romanization and Normalization
-------------------------------
The following code show cases how to normalize and romanize a given Amharic text

::

    from amseg.amharicNormalizer import AmharicNormalizer as normalizer
    from amseg.amharicRomanizer import AmharicRomanizer as romanizer
    normalized = normalizer.normalize('ሑለት ሦስት')
    romanized = romanizer.romanize('ሑለት ሦስት')

Outputs 
    > normalized = 'ሁለት ሶስት' 
    > romanized = 'ḥulat śosət'

Transliteration to Amharic Fidel
---------------------------------
The following code show cases how to transliterate a given latin script text to Amahric Fidel script text

::

    from amseg.amharicTranslitrator import AmharicTranslitrator as  transliterator
    transliterated = transliterator.transliterate('misa belah')

Outputs 
    > transliterated = 'ሚሳ በላህ' 

Publications
------------

To cite the Amharic segmenter/tokenizer tool, use the following
`paper <https://www.mdpi.com/1999-5903/13/11/275>`__

::

    @Article{fi13110275,
    AUTHOR = {Yimam, Seid Muhie and Ayele, Abinew Ali and Venkatesh, Gopalakrishnan and Gashaw, Ibrahim and Biemann, Chris},
    TITLE = {Introducing Various Semantic Models for Amharic: Experimentation and Evaluation with Multiple Tasks and Datasets},
    JOURNAL = {Future Internet},
    VOLUME = {13},
    YEAR = {2021},
    NUMBER = {11},
    ARTICLE-NUMBER = {275},
    URL = {https://www.mdpi.com/1999-5903/13/11/275},
    ISSN = {1999-5903},
    DOI = {10.3390/fi13110275}
    }

.. |image0| image:: https://github.com/uhh-lt/amharicmodels/raw/master/logo.png
   :target: https://github.com/uhh-lt/amharicmodels/
