from cube import *
import random

gene_directions = ['R', 'U', 'C']
max_rotation = 3
solved_fitness = 65536

class Solution(object):
    def __init__(self, number_of_genes = 16):
        self.max_genes = number_of_genes
        self.genes = ""

    def calculate_fitness(self, actual_cube, test_chromosome, stop_at = -1 ):
        _fitness = 0
        _max_index = -1
        _print = False
        if stop_at == -1:
            stop_at = self.max_genes
        else:
            stop_at += 1
            _print = True
        for i in range(0,stop_at):
            _act_gene = test_chromosome[i*2:(i+1)*2]
            #print(_act_gene)
            assert(_act_gene[0] in gene_directions)
            if _act_gene[0] == 'R':
                actual_cube.rotate_right(int(_act_gene[1]))
            elif _act_gene[0] == 'U':
                actual_cube.rotate_up(int(_act_gene[1]))
            else:
                actual_cube.rotate_cloclkwise(int(_act_gene[1]))
            
            actual_cube.test_cube()

            _solved_faces = actual_cube.count_solved_faces()

            if _solved_faces == 6:
                #print("\n\nSolved!!! {}. : {}".format(str(i+1), test_chromosome[:((i+1)*2)]), end="\n\n")
                # print solution
                #actual_cube.print_colored()
                _fitness = solved_fitness - i
                _max_index = i
                return _max_index, _fitness

            _new_fitness = _solved_faces * self.max_genes - i
            if _fitness < _new_fitness:
                _fitness = _new_fitness
                _max_index = i
        # if _print:
        #     print("Stopped at:", i)
        #     actual_cube.print_colored()
        return _max_index, _fitness

    def generate_random_genes(self):
        _genes = []
        for i in range(0,self.max_genes):
            _genes.append(
                "{}{}".format(
                    random.sample( gene_directions, 1 )[0],
                    random.randint( 1, max_rotation )
                    )
                )
        self.set_chromosome( ''.join(_genes) )
        #print("Random generated genes:", self.genes)

    def mutate_genes(self, rate = 1):
        _index = random.randint( 0, self.max_genes - 1 )
        _new_genes = ""
        _mutation = "{}{}".format(
            random.sample( gene_directions, 1 )[0],
            random.randint( 1, max_rotation )
        )
        if _index > 0:
            _new_genes += self.genes[:(_index * 2)]
        _new_genes += _mutation
        _len = len(_new_genes) / 2
        if _len < self.max_genes:
            _new_genes += self.genes[( (_index + 1) * 2):]

        _len = len(_new_genes) / 2
        if _len != self.max_genes:
            print("{}. > {} > {}".format(_index, _new_genes, len(_new_genes) / 2))
        assert( (len(_new_genes) / 2) == self.max_genes )

        if rate > 1:
            for i in range(1,rate):
                _index = random.randint( 0, self.max_genes - 1 )
                _newer_genes = ""
                _mutation = "{}{}".format(
                    random.sample( gene_directions, 1 )[0],
                    random.randint( 1, max_rotation )
                )
                if _index > 0:
                    _newer_genes += _new_genes[:(_index * 2)]
                _newer_genes += _mutation
                _len = len(_newer_genes) / 2
                if _len < self.max_genes:
                    _newer_genes += _new_genes[( (_index + 1) * 2):]

                _len = len(_newer_genes) / 2
                if _len != self.max_genes:
                    print("{}. > {} > {}".format(_index, _newer_genes, len(_newer_genes) / 2))
                assert( (len(_newer_genes) / 2) == self.max_genes )
                _new_genes = _newer_genes

        return _new_genes

    def get_chromosome(self):
        return self.genes
    
    def set_chromosome(self, new_chromosome):
        self.genes = new_chromosome
        for i in range(1,self.max_genes):
            _prev_gene = self.genes[(i-1)*2:i*2]
            _act_gene = self.genes[i*2:(i+1)*2]
            if _prev_gene[0] == _act_gene[0]:
                _count = ( int(_prev_gene[1]) + int(_act_gene[1]) ) % ( max_rotation + 1)
                if _count == 0:
                    self.genes = self.genes[:(i-1)*2] + self.genes[(i+1)*2:]
                else:
                    self.genes = self.genes[:(i-1)*2] + "{}{}".format( _prev_gene[0], _count ) + self.genes[(i+1)*2:]
                while (len(self.genes) / 2) < self.max_genes:
                    self.genes += "{}{}".format(
                            random.sample( gene_directions, 1 )[0],
                            random.randint( 1, max_rotation )
                        )
        assert( (len(self.genes) / 2) == self.max_genes )