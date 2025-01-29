# -------------------
# PROLOGIN
# 2024
#
# Link:
# https://prologin.org/train/2024/qualification/l-escalade-de-l-yggdrasil
# 
# Program:
#   # Train-2024-Qualification-01
# 
# Program title:
#   "L'escalade de l'Yggdrasil"
#
# DEV:
#   - Celeste VANDAMME
#       GitHub: https://github.com/Celeste-VANDAMME
#       Discord: @slak3r
#
# -------------------


# --- A. LIBRARIES AND DEPENDENCIES

from typing import List



# --- B. GLOBAL PARAMETERS

# Available files: sample_1.txt, sample_2.txt, sample_3.txt
INPUT_FILE_DIR  = str("2024/Qualification/01_Escalade-de-Yggdrasil/data/sample_2.txt")

STARTING_HEIGHT = int(1)



# --- C. FUNCTIONS

def inputReading_ProLogin() -> tuple[int, List[int]]:
    """
    Reads input for the ProLogin problem. This code was given on the website.
    The function expects two lines of input:
    1. An integer `n` representing the number of jumps.
    2. A space-separated list of integers representing the differences.
    Returns:
        tuple[int, List[int]]: A tuple containing the integer `n` and a list of integers `differences`.
    """
    
    n = int(input())
    differences = list(map(int, input().split()))
    
    return n, differences


def inputReading_Personal() -> tuple[int, List[int]]:
    """
    Reads input from a file and returns the data as a tuple.
    The function reads from a file specified by the global variable INPUT_FILE_DIR.
    The first line of the file contains an integer `n`.
    The second line contains a list of integers separated by spaces.
    Returns:
        tuple[int, List[int]]: A tuple containing:
            - n (int): The integer read from the first line of the file.
            - differences (List[int]): A list of integers read from the second line of the file.
    """
    
    with open(INPUT_FILE_DIR, 'r') as file:
        n = int( file.readline().strip() )
        differences = list(map(int, file.readline().strip().split()))
        
        return n, differences


def le_plus_grand_saut(n: int, differences: List[int]) -> int:
    """
    :param n: le nombre de branches de l'arbre moins 1
    :param differences: la liste des différences en hauteur des branches consécutives
    """
    
    # -- 1.1. We get the heights of the individual branches
    branchHeights = differences.copy()
    
    for i in range(1, n+1):
        branchHeights[i] += branchHeights[i-1]
    
    
    # -- 1.2. We get the maximum height
    highestBranchIndex, highestBranchHeight = max(enumerate(branchHeights), key=lambda x: x[1])

    # If the highest branch is the first one, then the maximum jump is 0 (default value demanded by the problem)
    if( highestBranchIndex == 0 ):
        return 0
    
    
    # -- 1.3. Now we find the highest jump done up to the highest branch
    maxJump = max( differences[:highestBranchIndex+1] )
    

    # -- 1.4. We return the maximum jump
    return maxJump


def displayResult(maxJump: int) -> None:
    """
    Displays the result of the program.
    :param maxJump: The maximum jump that can be made.
    """
    
    """
    print("")
    print(" --- RESULT --- ")
    print("The maximum height Höder will have to do is:")
    print(f"{maxJump} jumps high!")
    print("")
    """
    
    # Simplified display:
    print(maxJump)
    
    return None



# --- D. main.py

def main() -> None:
    
    # -- 1. Input read
    n, differences = inputReading_Personal()
    
    # -- 2. Adding the starting height to "differences"
    differences.insert(0, STARTING_HEIGHT)
    
    # -- 3. Analysis
    maxJump = le_plus_grand_saut(n, differences)
    
    # -- 4. Output (displaying the result)
    displayResult( maxJump )
    
    # -- X. Closing "main()"
    return None


# --- E. main() execution

if __name__ == "__main__":
    main()