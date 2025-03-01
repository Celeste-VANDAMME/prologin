# -------------------
# PROLOGIN
# 2024
#
# Link:
# https://prologin.org/train/2024/qualification/un_peu_d_ordre
# 
# Program:
#   # Train-2024-Qualification-02
# 
# Program title:
#   "Un peu d'ordre"
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

IS_PROLOGIN_ENV = True # Set to "True" if you are working on the Prologin submission environment

INPUT_FILE_DIR  = str("2024/Qualification/02_Un-peu-dordre/data/sample_3.txt")
# Available files: sample_1.txt, sample_2.txt, sample_3.txt

LOOPING_LIMIT = int(1000000) # Limit of loops to prevent infinite loops


# --- C. FUNCTIONS

def dataReading_ProLogin() -> tuple[int, int, List[int]]:
    
    k = int(input())
    n = int(input())
    personHeights = list(map(int, input().split()))
    
    return k, n, personHeights


def dataReading_File(fileDir:str) -> tuple[int, int, List[int]]:
    
    with open(fileDir, "r") as file:
        
        k = int(file.readline().strip())
        n = int(file.readline().strip())
        personHeights = list(map(int, file.readline().strip().split()))
    
    return k, n, personHeights


def sortingAnalysis(k:int, n:int, personHeights:List[int]) -> bool:
    
    # 1.1. Variables
    hasLoopedEntireList = False
    loopCounter = int(0)
    
    # 1.2. Analysis
    """
    The process here is that we're going to keep moving elements
    with the "k" offset value if we detect that x+k is smaller than x.
    
    If we have an ordered list, then it's possible to sort the family members.
    Otherwise, it's not!
    """

    personHeightsBuffer = personHeights.copy()
    personHeightsBufferSorted = sorted(personHeightsBuffer)
    
    while not hasLoopedEntireList and loopCounter < LOOPING_LIMIT:
        
        loopCounter += 1
        
        for i in range(k, n):
            
            # Getting variables the scanned variables
            valueInspected = personHeightsBuffer[i]
            valuePrevious_K = personHeightsBuffer[i-k]
            
            # And swapping them if the condition is met
            if valueInspected < valuePrevious_K:
                personHeightsBuffer[i] = valuePrevious_K
                personHeightsBuffer[i-k] = valueInspected
                
                # We want to cycle through the whole list again after this operation
                break
            
            if i == n-1:
                hasLoopedEntireList = True
    
    if personHeightsBuffer == personHeightsBufferSorted:
        return True
    
    else:
        return False


def displayOutput(isSortingPossible:bool) -> None:
    
    if isSortingPossible:
        print("OUI")
    else:
        print("NON")
    
    return None


# --- D. main.py

def main() -> None:
    
    # -- 1. Data Reading
    
    if IS_PROLOGIN_ENV:
        k, n, personHeights = dataReading_ProLogin()
        
    else:
        fileDir = INPUT_FILE_DIR
        k, n, personHeights = dataReading_File(fileDir)
    
    
    # -- 2. Height Sorting Analysis
    isSortingPossible = sortingAnalysis(k, n, personHeights)
    
    
    # -- 3. Output
    displayOutput(isSortingPossible)
    
    
    # -- 4. Closing "main()"
    return None



# --- E. main() execution

if __name__ == "__main__":
    main()