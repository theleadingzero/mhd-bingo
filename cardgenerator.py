import random 
import argparse

parser = argparse.ArgumentParser(description='Generate Music Hack Day bingo cards.')
parser.add_argument('number', metavar='N', type=int, nargs='+',
                   help='number of cards to generate')

args = parser.parse_args()
number_cards = args.number[0]

# LaTeX content
preamble = ""
postamble = ""

# Open file and read in squares text
squares_file = open( 'squares.txt', 'r' )
print '   ...Opened file'

squares = []

# Put into list
for line in squares_file:
	squares.append( line.strip() )

squares_file.close()

for i in range( number_cards):
	# Pull out 24 random squares
	card = random.sample( squares, 24 )

 
# Create output file
output_tex = open('generatedcards.tex', 'w')
# tex preamble
output_tex.write( "\documentclass[a4]{article}\n\usepackage{xstring}\n\usepackage{graphicx}\n" )
output_tex.write( "\usepackage{tikz}\n\usetikzlibrary{calc}\n\usepackage{helvet}\n\usepackage{geometry}\n" )
output_tex.write( "\geometry{verbose,tmargin=30pt,bmargin=90pt,lmargin=90pt,rmargin=90pt}\n" )
output_tex.write( "\def\NumOfColumns{5}\n\def\Sequence{1/A/1/15, 2/B/16/30, 3/C/31/45, 4/D/46/60, 5/E/61/71}\n" )
output_tex.write( "\\renewcommand*{\\familydefault}{\sfdefault}\n\\newcommand{\Size}{2.75cm}\n" )
output_tex.write( "\\tikzset{Square/.style={\n\tinner sep=0pt,\n\ttext width=\Size,\n\tminimum size=\Size,\n\tdraw=black,\n\tfill=white,\n\talign=center,\n\t}\n}\n" )
# tex body
output_tex.write( "\\begin{document}\n")
output_tex.write( "\input{./intro}\n" )
# thanks
output_tex.write(" \\vspace{0.5cm}\n\\noindent\nThanks to @plamere, @alsothings, @sydlawrence, @xhochy, @karltryggvason, @miguelpellitero for their financial support towards prizes and printing! " )
output_tex.write( "See https://www.hackerleague.org/hackathons/music-hack-day-london-2013/hacks/mhd-bingo for more info.\n" )
output_tex.write( "\\end{document}")
# close file
output_tex.close()