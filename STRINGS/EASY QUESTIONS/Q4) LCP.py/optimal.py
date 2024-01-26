# METHOD- (TRIE)-

# 1) Insert all the words one by one in the trie. After inserting we perform a walk on the trie.

# 2) In this walk, go deeper until we find a node having more than 1 children(branching occurs) or 0 children (one of the string gets exhausted). This is because the characters (nodes in trie) which are present in the longest common prefix must be the single child of its parent, i.e- there should not be branching in any of these nodes.

# CODE--

# Python 3 program to find the longest common prefix
ALPHABET_SIZE = 26
indexs = 0
class TrieNode:
    # constructor
    def __init__(self):
        self.isLeaf = False
        self.children = [None]*ALPHABET_SIZE
 
# Function to facilitate insertion in Trie
# If not present, insert the node in the Trie
def insert(key, root):
    pCrawl = root
    for level in range(len(key)):
        index = ord(key[level]) - ord('a')
        if pCrawl.children[index] == None:
            pCrawl.children[index] = TrieNode()
        pCrawl = pCrawl.children[index]
    pCrawl.isLeaf = True
 
# Function to construct Trie
def constructTrie(arr, n, root):
    for i in range(n):
        insert(arr[i], root)
 
# Counts and returns number of children of the node
def countChildren(node):
    count = 0
    for i in range(ALPHABET_SIZE):
        if node.children[i] != None:
            count +=1
            # Keeping track of diversion in the trie
            global indexs
            indexs = i
    return count
     
# Perform walk on trie and return longest common prefix 
def walkTrie(root):
    pCrawl = root
    prefix = ""
    while(countChildren(pCrawl) == 1 and pCrawl.isLeaf == False):
        pCrawl = pCrawl.children[indexs]
        prefix += chr(97 + indexs)
    return prefix or -1
 
# Function that returns longest common prefix 
def commonPrefix(arr, n, root):
    constructTrie(arr, n, root)
    return walkTrie(root)
 
# Driver code to test the code
n = 4
arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
root = TrieNode()
print(commonPrefix(arr,n, root))



# OUTPUT-
# The longest common prefix is gee

# Time Complexity : Inserting all the words in the trie takes O(MN) time and performing a walk on the trie takes O(M) time, where-

# N = Number of strings
# M = Length of the largest string

# Auxiliary Space: To store all the strings we need to allocate O(26*M*N) ~ O(MN) space for the Trie.  