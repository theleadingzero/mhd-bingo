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

card = []
for i in range( number_cards):
	# Pull out 24 random squares
	card = random.sample( squares, 25 )


positions = [ 0.5, 1.5, 2.5, 3.5, 4.5 ]
 
# Create output file
output_tex = open('generatedcards.tex', 'w')
# tex preamble
output_tex.write( "\documentclass[a4]{article}\n\usepackage{xstring}\n\usepackage{graphicx}\n" )
output_tex.write( "\usepackage{tikz}\n\usetikzlibrary{calc}\n\usepackage{helvet}\n\usepackage{geometry}\n" )
output_tex.write( "\geometry{verbose,tmargin=30pt,bmargin=90pt,lmargin=90pt,rmargin=90pt}\n" )
output_tex.write( "\def\NumOfColumns{5}\n\def\Sequence{1, 2, 3, 4, 5}\n" )
output_tex.write( "\\renewcommand*{\\familydefault}{\sfdefault}\n\\newcommand{\Size}{2.75cm}\n" )
output_tex.write( "\\tikzset{Square/.style={\n\tinner sep=0pt,\n\ttext width=\Size,\n\tminimum size=\Size,\n\tdraw=black,\n\tfill=white,\n\talign=center,\n\t}\n}\n" )
# tex body
output_tex.write( "\\begin{document}\n")

for i in range( number_cards ):
	# instructions
	output_tex.write( "\input{./intro}\n" )
	# bingo card
	output_tex.write( "\\begin{center}\n" )
	output_tex.write( "\\begin{tikzpicture}[draw=black, ultra thick, x=\Size,y=\Size]\n" )
	print len(card)
	for px in positions:
		for py in positions:
			sq = card.pop()
			node_text = "\\node [Square] at (%s, %s) { %s };\n" % (px, py, sq)
			output_tex.write( node_text )
	# output_tex.write( "\\foreach \\row in \Sequence{%\n\\foreach \col in \Sequence {%\n" )
	# output_tex.write( "\def\NodeText{ \\row }\n\pgfmathsetmacro{\ColRowProduce}{\col*\\row}\n" )
	# output_tex.write( "\IfEq{\ColRowProduce}{9}{\n\\node [Square] at ($(\col,-\\row)-(0.5,0.5)$) { Free Space};\n}\n" )
	# output_tex.write( "{\n\\node [Square] at ($(\col,-\\row)-(0.5,0.5)$) {\Huge \NodeText};\n}\n}\n}\n" )


	output_tex.write( "\end{tikzpicture}\n\end{center}\n")
	# thanks
	output_tex.write(" \\vspace{0.5cm}\n\\noindent\nThanks to @plamere, @alsothings, @sydlawrence, @xhochy, @karltryggvason, @miguelpellitero for their financial support towards prizes and printing! " )
	output_tex.write( "See https://www.hackerleague.org/hackathons/music-hack-day-london-2013/hacks/mhd-bingo for more info.\n" )
	output_tex.write( "\\newpage")
# end of document
output_tex.write( "\\end{document}")
# close file
output_tex.close()