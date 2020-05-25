from solution import *
from cube import *

chromosome_size = 24
mutation_rate = 5
my_solution = Solution(chromosome_size)
my_solution.generate_random_genes()
#_sample = "C1R1C2U1R1U1C3R2C3U2R3C3U1R3U1C3U2U2R2C3U2U1C2C3"
#_sample = "R3C1U3R2U3R1C1R3U3R2U1R1U2C3U1C3R3U1R2C1U1C2U3C1"
#print("Before:", _sample)
#my_solution.set_chromosome(_sample)
#print("After: ", my_solution.get_chromosome())
my_cube = Cube(
    "ORRO",
    ["YGBY","WBRO","WBGW","YGRO"],
    "YGBW"
)
my_cube.test_cube()
my_cube.print_colored()
# solved = my_cube.count_solved_faces()
# print("Solved faces:",str(solved))
# print("Rotate Right")
# _temp_cube = my_cube.clone()
# _temp_cube.rotate_right(2)
# _temp_cube.test_cube()
# _temp_cube.print_colored()
# print("Rotate Up")
# _temp_cube = my_cube.clone()
# _temp_cube.rotate_up(2)
# _temp_cube.test_cube()
# _temp_cube.print_colored()
# print("Rotate Clockwise")
# _temp_cube = my_cube.clone()
# _temp_cube.rotate_cloclkwise(2)
# _temp_cube.test_cube()
# _temp_cube.print_colored()

_index, _fitness = my_solution.calculate_fitness(my_cube.clone(), my_solution.get_chromosome())
print("Fitness:",str(_fitness))

# looping for solution
_counter = 0
_best_index = _index

print("\nSTART\n")
#while _fitness != solved_fitness and _counter < 500000:
while (not ((_fitness > (solved_fitness - chromosome_size)) and (_best_index < 10)) ) and _counter < 500000:
    _temp_cube = my_cube.clone()
    _new_cube = my_cube.clone()
    _genes = my_solution.mutate_genes(mutation_rate)
    _new_solution = None
    if _fitness >= (solved_fitness - chromosome_size):
        _new_solution = Solution((_best_index+1)*2)
    else:
        _new_solution = Solution(chromosome_size)
    _new_solution.generate_random_genes()
    _new_genes = _new_solution.get_chromosome()
    _new_index, _new_fitness = _new_solution.calculate_fitness(_new_cube,_new_genes)
    _max_index, _act_fitness = my_solution.calculate_fitness(_temp_cube, _genes)

    if _new_fitness > _act_fitness:
        _genes = _new_genes
        _max_index = _new_index
        _act_fitness = _new_fitness
        _temp_cube = _new_cube
        
        if _act_fitness > _fitness:
            print("\n{}. RND taken over {}".format(_counter, _act_fitness))
            my_solution = copy.deepcopy(_new_solution)

    if _act_fitness > _fitness:
        my_solution.set_chromosome( _genes )
        _fitness = _act_fitness
        _best_index = _max_index
        print("\n{}. chromosome changed; index:{}, new: {}".format(_counter, _best_index, _genes))
        _temp_cube = my_cube.clone()
        my_solution.calculate_fitness(_temp_cube, _genes, _best_index)
        _temp_cube.print_colored()
    _counter += 1
    if _counter % 100 == 0:
        print("{}. round, fitness: {}; index: {}; chromosome={}".format(_counter, _fitness, _best_index, my_solution.get_chromosome()), end="\r")
print("\n\nCOUNTER = {}".format(_counter))
print()
_temp_cube = my_cube.clone()
_i, _f = my_solution.calculate_fitness( _temp_cube, my_solution.get_chromosome(), _best_index )
print("{}. step, fitness: {}".format(_i, _f))
print("Solution: {}".format(my_solution.get_chromosome()[:(_best_index+1)*2]))