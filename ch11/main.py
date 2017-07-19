import gp
from importlib import reload
reload(gp)

exampletree = gp.exampletree()
print(exampletree.evaluate([5,3]))
exampletree.display()

gp.drawgptree(exampletree)
print('GpTree has been drawed!')



