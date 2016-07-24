#Temporary Holding place for my code

def divideBrainFuck(brainfuck):
	reducer = lambda x,y: x + [y] if y != x[-1][0] or y in "[]<" else x[:-1] + [x[-1]+y]
	return reduce(reducer,[[brainfuck[0]]]+list(brainfuck[1:]))

def compile(brainfuck):
	key = {"+":"{}(({}))({()<({}[()]<<>({}<>)>)>}{})<>(({}%s)<<>{({}[()]<({}<>)<>>)}{}>)",
	       "-":"{}(({}))({()<({}[()]<<>({}<>)>)>}{})<>(({}[%s])<<>{({}[()]<({}<>)<>>)}{}>)",
	       ">":"{}(({}%s))({()<({}[()]<<>({}<>)>)>}{})<>(({})<><{({}[()]<({}<>)<>>)}{}>)",
	       "<":"(<>)<>{}((({}))){(<{}{}(({}[()]))<>{}<>>)}{}({()<({}[()]<<>({}<>)>)>}{})<>(({})<><{({}[()]<({}<>)<>>)}{}>)",
	       "[":"{",
	       "]":"}"}
	filler = lambda x: key[x] if x in "[]<" else key[x[0]]%("()"*len(x))
	return "(({})(<>))" + "".join(map(filler, divideBrainFuck(brainfuck))) + "{}{}<>"

if __name__ == "__main__":
	snippet = "++>++>++"
	print compile(snippet)
