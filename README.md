mhd-bingo
=========

Bingo cards for Music Hack Day. Created for MHD London 2013.

To adapt for future use
-----------------------
* bingocards.tex is a test file to work out formatting issues
* intro.tex contains text at top of bingo card
* thanks.tex contains text at bottom of bingo card
* cardgenerator.py generates LaTeX file and content of bingo squares
* squares.txt is the list of content for the bingo squares


To generate bingo cards
-----------------------
Run 
> python cardgenerator.py N 
where N is the number of cards you would like generated.

Typeset the generated file generatedcards.tex which renders generatedcards.pdf.
