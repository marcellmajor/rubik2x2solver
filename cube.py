from solution import *
import colorama
import sty
import copy
from collections import defaultdict

colors = [
    "Y", # Yellow
    "R", # Red
    "W", # White
    "O", # Orange
    "G", # Green
    "B"  # Blue
]

color_selector = {
    "Y":"\33[48;5;11m", # Yellow
    "R":colorama.Back.RED, # Red
    "W":"\33[48;5;15m", # White
    "O":"\33[48;5;214m", # Orange
    "G":colorama.Back.GREEN, # Green
    "B":colorama.Back.BLUE  # Blue
}

block_size = 2

class Cube(object):
    def __init__( self, top_face, row_of_faces, bottom_face ):
        self.top_face = top_face
        self.row_of_faces = row_of_faces
        self.bottom_face = bottom_face

    def rotate_right(self, count):
        for i in range(0,count):
            _temp_face_half = self.row_of_faces[3][2:]
            self.row_of_faces[3] = self.row_of_faces[3][:2] + self.row_of_faces[2][2:]
            self.row_of_faces[2] = self.row_of_faces[2][:2] + self.row_of_faces[1][2:]
            self.row_of_faces[1] = self.row_of_faces[1][:2] + self.row_of_faces[0][2:]
            self.row_of_faces[0] = self.row_of_faces[0][:2] + _temp_face_half
            _temp_face = self.bottom_face
            self.bottom_face = _temp_face[2] + _temp_face[0] +_temp_face[3] + _temp_face[1]

    def rotate_up(self, count):
         for i in range(0,count):
            _temp_face = self.row_of_faces[2]
            self.row_of_faces[2] = self.row_of_faces[2][0] + self.bottom_face[1] + self.row_of_faces[2][2] + self.bottom_face[3]
            self.bottom_face = self.bottom_face[0] + self.row_of_faces[0][2] + self.bottom_face[2] + self.row_of_faces[0][0]
            self.row_of_faces[0] = self.top_face[3] + self.row_of_faces[0][1] + self.top_face[1] + self.row_of_faces[0][3]
            self.top_face = self.top_face[0] + _temp_face[1] + self.top_face[2] + _temp_face[3]
            _temp_face = self.row_of_faces[3]
            self.row_of_faces[3] = _temp_face[2] + _temp_face[0] +_temp_face[3] + _temp_face[1]

    def rotate_cloclkwise(self, count):
         for i in range(0,count):
            _temp_face = self.row_of_faces[2]
            self.row_of_faces[2] = _temp_face[2] + _temp_face[0] +_temp_face[3] + _temp_face[1]
            _temp_face_half = self.top_face[2:]
            self.top_face = self.top_face[:2] + self.row_of_faces[1][3] + self.row_of_faces[1][1]
            self.row_of_faces[1] = self.row_of_faces[1][0] + self.bottom_face[0] + self.row_of_faces[1][2] + self.bottom_face[1]
            self.bottom_face = self.row_of_faces[3][2] + self.row_of_faces[3][0] + self.bottom_face[2:]
            self.row_of_faces[3] = _temp_face_half[0] + self.row_of_faces[3][1] + _temp_face_half[1] + self.row_of_faces[3][3]

    def count_solved_faces(self):
        faces = [
            self.top_face,
            self.row_of_faces[0],
            self.row_of_faces[1],
            self.row_of_faces[2],
            self.row_of_faces[3],
            self.bottom_face
            ]
        _counter = 0
        for _face in faces:
            if _face[0] == _face[1] == _face[2] == _face[3]:
                _counter += 1
        return _counter

    def print_colored(self):
        colorama.init()
        print(' ' * block_size * 4,end='')
        print(color_selector[self.top_face[0]] + ' ' * block_size,end='')
        print(colorama.Style.RESET_ALL,end='')
        print(color_selector[self.top_face[1]] + ' ' * block_size,end='')
        print(colorama.Style.RESET_ALL)
        print(' ' * block_size * 4,end='')
        print(color_selector[self.top_face[2]] + ' ' * block_size,end='')
        print(colorama.Style.RESET_ALL,end='')
        print(color_selector[self.top_face[3]] + ' ' * block_size,end='')
        print(colorama.Style.RESET_ALL)

        for _face in self.row_of_faces:
            print(color_selector[_face[0]] + ' ' * block_size,end='')
            print(color_selector[_face[1]] + ' ' * block_size,end='')
        print(colorama.Style.RESET_ALL)
        for _face in self.row_of_faces:
            print(color_selector[_face[2]] + ' ' * block_size,end='')
            print(color_selector[_face[3]] + ' ' * block_size,end='')
        print(colorama.Style.RESET_ALL)

        print(' ' * block_size * 4,end='')
        print(color_selector[self.bottom_face[0]] + ' ' * block_size,end='')
        print(colorama.Style.RESET_ALL,end='')
        print(color_selector[self.bottom_face[1]] + ' ' * block_size,end='')
        print(colorama.Style.RESET_ALL)
        print(' ' * block_size * 4,end='')
        print(color_selector[self.bottom_face[2]] + ' ' * block_size,end='')
        print(colorama.Style.RESET_ALL,end='')
        print(color_selector[self.bottom_face[3]] + ' ' * block_size,end='')
        print(colorama.Style.RESET_ALL)

    def test_cube(self):
        _colorcount = defaultdict(int)
        assert(len(self.top_face) == 4)
        for _color in self.top_face:
            _colorcount[_color] += 1
            assert(_color in colors)
        assert(len(self.row_of_faces) == 4)
        for _face in self.row_of_faces:
            assert(len(_face) == 4)
            for _color in _face:
                _colorcount[_color] += 1
                assert(_color in colors)
        assert(len(self.bottom_face) == 4)
        for _color in self.bottom_face:
            _colorcount[_color] += 1
            assert(_color in colors)
        #print("Cube seems OK")
        for _color in _colorcount.keys():
            if _colorcount[_color] != 4:
                print("{}:{}".format(_color,_colorcount[_color]))
                self.print_colored()
            assert( _colorcount[_color] == 4 )
            assert( _color in colors )
    
    def clone(self):
        return copy.deepcopy(self)