import sys
import threading
import numpy


def compute_height(n, parents):

    
    heights = [-1] * n
    root = None
    for i in range(n):
        if parents[i] == -1:
            root = i
            break

    heights[root] = 1

    def dfs(node):

        if heights[node] != -1:
            return heights[node]

        parent = parents[node]

        if parent == -1:
            return 1

        height = 1 + dfs(parent)
        heights[node] = height
        
        return height
    max_height = max(dfs(i) for i in range(n))
    return max_height


def main():
   
    source = input("Enter 'I' or 'F': ")

    if source.upper() == "I":

        n = int(input())
        parents = list(map(int, input().split()))

    elif source.upper() == "F":

        while True:
            try:
                filename = input("Enter file name: ")
                if "a" in filename:
                    print("Invalid file name")
                else:
                    with open("data/" + filename, "r") as f:
                        n = int(f.readline().strip())
                        parents = list(map(int, f.readline().strip().split()))
                    break
            except FileNotFoundError:
                print("File not found")
            except:
                print("Invalid input")

    else:
        print("Please enter 'I' or 'F'")

    height = compute_height(n, parents)

    print(height)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)  
threading.Thread(target=main).start()
main()