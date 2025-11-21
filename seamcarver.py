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
        width = self.width()
        height = self.height()
        
        # Property of the energy function in which we check the pixels surrounding it.
        # Modulo measure of height and width to ensure that border pixels will have wrapped pixels to compare to
        up = (j - 1) % height
        down = (j + 1) % height
        left = (i - 1) % width
        right = (i + 1) % width

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
        
        # Get width and height from picture
        width = self.width()
        height = self.height()

        # Initialize dynamic programming
        dp = [[0] * width for _ in range(height)]
        parent = [[0] * width for _ in range(height)]

        # Approach is to compute for the energies from top to bottom, then find the collumn with the smallest culmative energy.
        # Go back up to recover the seam with the minimal energy
        
        # Base case: first row
        for col in range(width):
            dp[0][col] = self.energy(col, 0)

        # Putting energy values into dp table (by rows)
        for row in range(1, height):
            for col in range(width):

                # Default store top first
                prev_energy = dp[row - 1][col]
                prev_col = col

                # Check if top left energy value is lesser than middle
                if col > 0 and dp[row - 1][col - 1] < prev_energy:
                    prev_energy = dp[row - 1][col - 1]
                    prev_col = col - 1

                # Check if top right energy value is lesser than top left
                if col > 0 and dp[row - 1][col + 1] < prev_energy:
                    prev_energy = dp[row - 1][col + 1]
                    prev_col = col + 1

                # Update dp and parent
                dp[row][col] = self.energy(col, row) + prev_energy
                parent[row][col] = prev_col

        # Find the column with minimum cumulative energy in the bottom row
        min_col = 0
        min_energy = dp[height - 1][0]
        for col in range(1, width):
            if dp[height - 1][col] < min_energy:
                min_energy = dp[height - 1][col]
                min_col = col

        # Backtrack to recover the seam path
        seam = [0] * height
        seam[height - 1] = min_col
        for row in range(height - 1, 0, -1): # -> -1 because we go backwards (bottom to top)
            seam[row - 1] = parent[row][seam[row]]

        # Return list seam
        return seam


    def find_horizontal_seam(self) -> list[int]:
        '''
        Return a sequence of indices representing the lowest-energy
        horizontal seam
        '''
        
        # Get width and height from picture
        width = self.width()
        height = self.height()

        # Initialize dynamic programming
        dp = [[0] * width for _ in range(height)]
        parent = [[0] * width for _ in range(height)]

        # Kind of same approach but this time we go left to right and vice versa

        # Base case: first column
        for row in range(height):
            dp[0][row] = self.energy(0, row)

        # Putting energy values into dp table (by collumn)
        for col in range(1, width):
            for row in range(height):

                # Default store left first
                prev_energy = dp[col - 1][row]
                prev_row = row

                # Check if top left energy value is lesser than left
                if row > 0 and dp[col - 1][row - 1] < prev_energy:
                    prev_energy = dp[col - 1][row - 1]
                    prev_row = row - 1

                # Check if bottom left energy value is lesser than top left
                if row < height - 1 and dp[col - 1][row + 1] < prev_energy:
                    prev_energy = dp[col - 1][row + 1]
                    prev_row = row + 1

                # Update dp and parent
                dp[col][row] = self.energy(col, row) + prev_energy
                parent[col][row] = prev_row
        
        # Find the row with minimum cumulative energy in the last collumn
        min_row = 0
        min_energy = dp[width - 1][0]
        for row in range(1, height):
            if dp[width - 1][row] < min_energy:
                min_energy = dp[width - 1][row]
                min_row = row

        # Backtrack to recover seam
        seam = [0] * width
        seam[width - 1] = min_row
        for col in range(width - 1, 0, -1):
            seam[col - 1] = parent[col][seam[col]]

        # Return list seam
        return seam


    def remove_vertical_seam(self, seam: list[int]):
        '''
        Remove a vertical seam from the picture
        '''
        pass

    def remove_horizontal_seam(self, seam: list[int]):
        '''
        Remove a horizontal seam from the picture
        '''
        pass
class SeamError(Exception):
    pass
