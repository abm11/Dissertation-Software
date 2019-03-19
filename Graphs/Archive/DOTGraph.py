from graphviz import Source

src = ('ENS1.gv')

f = open("SOPgv/ENS1.gv", "r")
print(f.read())


src.render('grid.dot', view=True)  

