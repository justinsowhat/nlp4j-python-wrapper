NLP4J Python Wrapper
====================

Introduction
------------
This is a python wrapper for the [common-line tools](https://emorynlp.github.io/nlp4j/quickstart/install.html) of [NLP4J](https://emorynlp.github.io/nlp4j/).
 
I wrote it because for a current project that I'm working on is heavily python-based, and just to keep my codes and pipeline together,
having a python wrapper makes my life slight easier. 

Also, a nice thing about NLP4J is that their POS tagger is trained on some clinical notes/texts, so if you are working on clinical NLP,
it's a nice alternative to cTAKES. For more details on their models, [this page](https://emorynlp.github.io/nlp4j/supplements/english.html).


Dependencies
------------
For this to work, you will need to download the [common-line binaries](https://emorynlp.github.io/nlp4j/quickstart/install.html)
and untar it somewhere. Also, if you want to use pre-trained English models and their English lexica, please check out [this page](https://emorynlp.github.io/nlp4j/supplements/english.html).


Instructions
------------
clone this git repo or download it as a zip file and then unzip it.
cd into the directory in terminal, then run:
    ```python setup.py install```

Then test in python to validate that the binaries and the wrapper are working:
```
>>> import nlp4j_wrapper
>>> BINARIES_PATH=/absolute/path/to/bin
>>> nlp4j_wrapper.version(BINARIES_PATH)

========================================
NLP4J Version 1.1.3
Contact: choi@mathcs.emory.edu
Webpage: http://emorynlp.github.io/nlp4j
========================================
```

To train a model (NER, POS or Dependencies), these are the minimal arguments:
```
>>> CONFIG=/absolute/path/to/config.xml
>>> TRAIN_PATH=/absolute/path/to/train_files
>>> nlp4j_wrapper.version(BINARIES_PATH, CONFIG, TRAIN_PATH, 'pos')
```
For more details on training parameters as well as the config file, please go to [this page](https://emorynlp.github.io/nlp4j/quickstart/train.html).

To decode (i.e.) a file, these are the minimal arguments:
```
>>> INPUT_FILE = /absolute/path/to/input_file.txt
>>> nlp4j_wrapper.decode(BINARIES_PATH, CONFIG, INPUT_FILE)

Loading ambiguity classes

Loading word clusters

Loading word embeddings

Loading named entity gazetteers

Loading tokenizer

Loading part-of-speech tagger

Loading morphological analyzer

Loading named entity recognizer

Loading dependency parser

input_file.txt

```
For more details on decoding parameters as well as the config file, please go to [this page](https://emorynlp.github.io/nlp4j/quickstart/decode.html).

Please note that all the paths in the config file as well as arguments have to absolute.

License
-------
####MIT 
Copyright (c) 2016 Justin So

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
