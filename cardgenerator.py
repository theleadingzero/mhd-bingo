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

squares = []

# Put into list
for line in squares_file:
	squares.append( line.strip() )

squares_file.close()

# positions of squares in grid
positions = [ 0.5, 1.5, 2.5, 3.5, 4.5 ]
 
# Create output file
output_tex = open('generatedcards.tex', 'w')
# tex preamble
output_tex.write( "\documentclass[a4]{article}\n\usepackage{xstring}\n\usepackage{graphicx}\n" )
output_tex.write( "\usepackage{tikz}\n\usetikzlibrary{calc}\n\usepackage{helvet}\n\usepackage{geometry}\n\hyphenation{executive}\n\hyphenation{Musicmetric}\n" )
output_tex.write( "\geometry{verbose,tmargin=30pt,bmargin=90pt,lmargin=90pt,rmargin=90pt}\n" )
output_tex.write( "\def\NumOfColumns{5}\n\def\Sequence{1, 2, 3, 4, 5}\n" )
output_tex.write( "\\renewcommand*{\\familydefault}{\sfdefault}\n\\newcommand{\Size}{3cm}\n" )
output_tex.write( "\\tikzset{Square/.style={\n\tinner sep=0pt,\n\ttext width=\Size*0.8,\n\tminimum size=\Size,\n\tdraw=black,\n\tfill=white,\n\talign=center,\n\t}\n}\n" )
# tex body
output_tex.write( "\\begin{document}\n")

for i in range( number_cards ):
	# instructions
	output_tex.write( "\input{./intro}\n" )
	# bingo card
	output_tex.write( "\\begin{center}\n" )
	output_tex.write( "\\begin{tikzpicture}[draw=black, ultra thick, x=\Size,y=\Size]\n" )

	card = random.sample( squares, 25 )
	for px in positions:
		for py in positions:
			sq = card.pop()
			node_text = "\\node [Square] at (%s, %s) { %s };\n" % (px, py, sq)
			output_tex.write( node_text )

	output_tex.write( "\\node [Square, fill=lightgray] at (2.5, 2.5) { International Executive Hack };\n" )
	output_tex.write( "\end{tikzpicture}\n\end{center}\n")
	# thanks
	output_tex.write( "\input{./thanks}\n")
# end of document
output_tex.write( "\\end{document}")
# close file
output_tex.close()