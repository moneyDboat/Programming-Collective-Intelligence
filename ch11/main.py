import gp

# exampletree = gp.exampletree()
# print(exampletree.evaluate([5,3]))
# exampletree.display()
#
# gp.drawgptree(exampletree)
# print('GpTree has been drawed!')


# print('<----Evolue Tree!---->')
# hiddenset = gp.buildhiddenset()
# rf = gp.getrankfunction(hiddenset)
# evolve_tree = gp.evolve(2, 500, rf, mutationrate=0.2, breedingrate=0.1, pexp=0.7, pnew=0.1)
# gp.drawgptree(evolve_tree, jpeg='output/evtree.jpg')


print('<----A game!---->')
winner = gp.evolve(5, 100, gp.tournament, maxgen=50)
gp.drawgptree(winner, jpeg='output/gametree.jpg')

print('<----Play a game with computer!---->')
gp.gridgame([winner, gp.humanplayer])
