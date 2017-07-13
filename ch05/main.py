import optimization
import dorm
import socialnetwork

# # Group Travel
# print('<----Group Travel---->')
# s = [1, 4, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3]
# optimization.printschedule(s)
#
# cost = optimization.schedulecost(s)
# print('Present cost:%f' % cost)
#
# print('\n<----Random Searching---->')
# domain = [(0, 9)] * (len(optimization.people) * 2)
# print(s)
# s = optimization.randomoptimize(domain, optimization.schedulecost)
# cost = optimization.schedulecost(s)
# print('Present cost:%f' % cost)
# optimization.printschedule(s)
#
# print('\n<----Hill Climbing---->')
# s = optimization.hillclimb(domain, optimization.schedulecost)
# print(s)
# cost = optimization.schedulecost(s)
# print('Present cost:%f' % cost)
# optimization.printschedule(s)
#
# print('\n<----Simulated Annealing---->')
# s = optimization.annealingoptimize(domain, optimization.schedulecost)
# print(s)
# cost = optimization.schedulecost(s)
# print('Present cost:%f' % cost)
# optimization.printschedule(s)
#
# print('\n<----Genetic Algorithms---->')
# s = optimization.geneticoptimize(domain, optimization.schedulecost)
# print(s)
# cost = optimization.schedulecost(s)
# print('Present cost:%f' % cost)
# optimization.printschedule(s)

# print('\n\n<----Student Dorm Optimization---->')
# print('\n<----Random---->')
# s = optimization.randomoptimize(dorm.domain, dorm.dormcost)
# print('Present Cost:%d' % dorm.dormcost(s))
#
# print('\n<----Genetic---->')
# s = optimization.geneticoptimize(dorm.domain, dorm.dormcost)
# print('Present Cost:%d' % dorm.dormcost(s))
# dorm.printsolution(s)


print('\n\n<----Network Visualization---->')
# sol = optimization.annealingoptimize(socialnetwork.domain,
#       socialnetwork.crosscount, step=50, cool=0.99)
sol = optimization.geneticoptimize(socialnetwork.domain, socialnetwork.crosscount)
print('Present Cost:%d' % socialnetwork.crosscount(sol))
print(sol)
socialnetwork.drawnetwork(sol)
