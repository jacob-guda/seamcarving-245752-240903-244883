#!/usr/bin/env python3

from picture import Picture
import math

class SeamCarver(Picture):
    ## TO-DO: fill in the methods below
    def energy(self, i: int, j: int) -> float:
        '''
        Return the energy of pixel at column i and row j
        '''

        # Get width and hegiht from picture
        w = self.width()
        h = self.height()
        
        # Property of the energy function in which we check the pixels surrounding it.
        # Modulo measure of height and width to ensure that border pixels will have wrapped pixels to compare to
        up = (j - 1) % h
        down = (j + 1) % h
        left = (i - 1) % w
        right = (i + 1) % w

        # Implementation of x-gradient
        r1, g1, b1 = self[right, j]
        r2, g2, b2 = self[left, j]
        dx2 = (r1 - r2)**2 + (g1 - g2)**2 + (b1 - b2)**2

        # Implementation of y-gradient
        r3, g3, b3 = self[i, down]
        r4, g4, b4 = self[i, up]
        dy2 = (r3 - r4)**2 + (g3 - g4)**2 + (b3 - b4)**2

        # Return energy of main pixel
        return math.sqrt(dx2 + dy2)
        

    def find_vertical_seam(self) -> list[int]:
        '''
        Return a sequence of indices representing the lowest-energy
        vertical seam
        '''
        raise NotImplementedError

    def find_horizontal_seam(self) -> list[int]:
        '''
        Return a sequence of indices representing the lowest-energy
        horizontal seam
        '''
        raise NotImplementedError

    def remove_vertical_seam(self, seam: list[int]):
        '''
        Remove a vertical seam from the picture
        '''
        raise NotImplementedError

    def remove_horizontal_seam(self, seam: list[int]):
        '''
        Remove a horizontal seam from the picture
        '''
        raise NotImplementedError

class SeamError(Exception):
    pass
