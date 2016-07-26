import sys
import re
import optimizer


def divideBrainFuck(brainfuck):
	reducer = lambda x,y: x + [y] if y != x[-1][0] or y in "[]<" else x[:-1] + [x[-1]+y]
	return reduce(reducer,[[brainfuck[0]]]+list(brainfuck[1:]))


def compile(brainfuck):
	key = {"+":"{}(({}))({()<({}[()]<<>({}<>)>)>}{})<>(({}%s)<<>{({}[()]<({}<>)<>>)}{}>)",
	       "-":"{}(({}))({()<({}[()]<<>({}<>)>)>}{})<>(({}[%s])<<>{({}[()]<({}<>)<>>)}{}>)",
	       ">":"({}<(({}%s))>)",
	       "<":"(<>)<>({}<((({}))){(<{}{}(({}[()]))<>{}<>>)}{}>)",
	       "[":"{}(({}))({()<({}[()]<<>({}<>)>)>}{})<>(({})<><{({}[()]<({}<>)<>>)}{}>){",
	       "]":"{}(({}))({()<({}[()]<<>({}<>)>)>}{})<>(({})<><{({}[()]<({}<>)<>>)}{}>)}"}
	filler = lambda x: key[x] if x in "[]<" else key[x[0]]%("()"*len(x))
	return "(({})(<>))" + "".join(map(filler, divideBrainFuck(brainfuck))) + "{}{}<>"

if __name__ == "__main__":
	commandLineArgs = sys.argv
	if len(commandLineArgs) != 3:
		print "Please pass a input and output file."
		print "(Usage: python %s BrainFuck BrainFlak)" %commandLineArgs[0]
		exit()
	#Open first file compile and write to second file
	#Open files
	try:
		infile = open(commandLineArgs[1])
		string = infile.read()
		infile.close()

		#Clean the string
		string = re.sub("[^+-<>\[\]]","",string)
	
		outfile = open(commandLineArgs[2],"w")	
		outfile.write(optimizer.optimize(compile(string)))
		outfile.close()
	except IOError:
		print "File",commandLineArgs[1],"does not exist."
