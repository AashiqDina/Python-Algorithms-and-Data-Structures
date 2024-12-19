#----------------------------------------------------------------------------------------------
#Linear Search
#----------------------------------------------------------------------------------------------
def LinearSearch(A, v):
    ArrayIndex = -1
    for i in range(len(A)):
        if (A[i] == v):
            ArrayIndex = i
            return ArrayIndex
    return ArrayIndex
#----------------------------------------------------------------------------------------------
#Test Linear Search
#----------------------------------------------------------------------------------------------
# ArrayToSearch = [3,7,2,98,32,15,75,21,5365,723,1,7,0]
# Value = input('What number do you want to look for? ')
# print('Location of 3 is the array index: ' , LinearSearch(ArrayToSearch, int(Value)))
#----------------------------------------------------------------------------------------------
#Binary Search
#----------------------------------------------------------------------------------------------
def BinarySearch(SA,v):
    Low = 0
    High = len(SA) - 1
    while (Low <= High):
        MidPoint = (Low+High)//2
        if (SA[MidPoint] == v):
            return MidPoint
        elif (SA[MidPoint] < v):
            Low = MidPoint + 1
        else:
            High = MidPoint-1
    return -1
#----------------------------------------------------------------------------------------------
#Binary Search Test
#----------------------------------------------------------------------------------------------
# A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# print(BinarySearch(A,-1))
# print(BinarySearch(A,16))
# print(BinarySearch(A,1))
# print(BinarySearch(A,15))
# print(BinarySearch(A,-1000))
# print(BinarySearch(A,10000))
# print(BinarySearch(A,3))
# print(BinarySearch(A,12))
#----------------------------------------------------------------------------------------------
#Selection Sort
#----------------------------------------------------------------------------------------------
def SelectionSort(A):
    for i in range(len(A)):
        CurrentMin = i
        for j in range(i+1,len(A)):
            if A[j] < A[CurrentMin]:
                CurrentMin = j
        temp = A[i]
        A[i] = A[CurrentMin]
        A[CurrentMin] = temp
    return A
#----------------------------------------------------------------------------------------------
# Selection Sort Test
#----------------------------------------------------------------------------------------------
# A = [5,75,23,86,32,7993,25,768,235,8732,6,3,4454,4354,76,8,2,89,43,3,46]
# print(SelectionSort(A))
#----------------------------------------------------------------------------------------------
# Insertion Sort
#----------------------------------------------------------------------------------------------
def InsertionSort(A):
    for i in range(1,len(A)):
        Insert(A,i,A[i])
    return A

def Insert(A, High, Value):
    for j in range(High-1,-1,-1):
        if Value >= A[j]:
            A[j+1] = Value
            return
        A[j+1] = A[j]
    A[0] = Value
#----------------------------------------------------------------------------------------------
# Insertion Sort Test
#----------------------------------------------------------------------------------------------
# A = [98,543,865,32,6,6,2,76,3,7686,34,87,0,34,7,7,56,34,76,867]
# print(InsertionSort(A))
#----------------------------------------------------------------------------------------------
# Merge Sort
#----------------------------------------------------------------------------------------------
def MergeSort(A):
    if (len(A) <=1):
        return
    MidPoint = len(A)//2
    FirstHalf = A[:MidPoint]
    SecondHalf = A[MidPoint:]
    MergeSort(FirstHalf)
    MergeSort(SecondHalf)
    Merge(FirstHalf,SecondHalf,A)
    return A

def Merge(FirstHalf, SecondHalf, A):
    i=0
    j=0
    k=0
    while j<len(FirstHalf) and k<len(SecondHalf):
        if FirstHalf[j] < SecondHalf[k]:
            A[i] = FirstHalf[j]
            j +=1
            i +=1
        else:
            A[i] = SecondHalf[k]
            k +=1
            i +=1
    while j < len(FirstHalf):
        A[i] = FirstHalf[j]
        j +=1
        i +=1
    while k < len(SecondHalf):
        A[i] = SecondHalf[k]
        k +=1
        i +=1
#----------------------------------------------------------------------------------------------
# Test Merge Sort
#----------------------------------------------------------------------------------------------
# A = [5,345,3,8,23,8,4,3,86,2,65,34,4,85,38,93,54,3,7,34,6767,2457,65,93,5786,5,465,96,23,7,5,4,25]
# print(MergeSort(A))
#----------------------------------------------------------------------------------------------
# Quick Sort
#----------------------------------------------------------------------------------------------
def QuickSort(A):
    RecQuickSort(A,0,len(A))
    return A

def RecQuickSort(A,Low,High):
    if (High-Low) <= 1:
        return
    Pivot = Partition(A,Low,High)
    RecQuickSort(A,Low,Pivot)
    RecQuickSort(A,Pivot+1,High)
    return A

def Partition(A,Low,High):
    Pivot = A[Low]
    B = [0 for i in range(Low,High)]
    LowB = 0
    HighB = len(B)-1
    for i in range(Low+1,High):
        if A[i] < Pivot:
            B[LowB] = A[i]
            LowB += 1
        else:
            B[HighB] = A[i]
            HighB -= 1
    B[LowB] = Pivot
    for i in range(len(B)):
        A[Low+i] = B[i]
    return Low+LowB
#----------------------------------------------------------------------------------------------
# Quick Sort Test
#----------------------------------------------------------------------------------------------
# A = [5,2,6,4,76,23,7,2,89,2,0,9,3,1,5,432,765,32,87,3,57,324,6586,87,23,4,56,45]
# print(QuickSort(A))
#----------------------------------------------------------------------------------------------
# Array Lists
#----------------------------------------------------------------------------------------------
class ArrayList:
    def __init__(self):
        self.TheArray = [0 for i in range(10)]
        self.count = 0

    def Get(self, i):
        return self.TheArray[i]

    def Set(self, i, j):
        self.TheArray[i] = j

    def Length(self):
        return len(self.TheArray)

    def Append(self, i):
        self.TheArray[self.count] = i
        self.count += 1
        if len(self.TheArray) == self.count:
            NewArray = [0 for i in range(2*len(self.TheArray))]
            for j in range(len(self.TheArray)):
                NewArray[j] = self.TheArray[j]
            self.TheArray = NewArray

    def AppendArray(self, A):
        for k in range(len(A)):
            self.TheArray[self.count] = A[k]
            self.count += 1
            if len(self.TheArray) == self.count:
                NewArray = [0 for i in range(2*len(self.TheArray))]
                for j in range(len(self.TheArray)):
                    NewArray[j] = self.TheArray[j]
                self.TheArray = NewArray
    
    def Insert(self, i, j):
        for k in range(self.count,i,-1):
            self.TheArray[k] = self.TheArray[k-1]
        self.TheArray[i] = j
        self.count += 1 
        if len(self.TheArray) == self.count:
            NewArray = [0 for i in range(2*len(self.TheArray))]
            for j in range(len(self.TheArray)):
                NewArray[j] = self.TheArray[j]
            self.TheArray = NewArray

    def Remove(self, i):
        self.count -= 1
        Removed = self.TheArray[i]
        for j in range(i,self.count):
            self.TheArray[j] = self.TheArray[j+1]
        return Removed
#----------------------------------------------------------------------------------------------
# Array List Test
#----------------------------------------------------------------------------------------------
# AnArray = ArrayList()
# print(AnArray.TheArray)
# AnArray.AppendArray([1,3,4,6,82,7,3,42,5])
# print(AnArray.TheArray)
# AnArray.Append(101)
# print(AnArray.TheArray)
# AnArray.Insert(0,0)
# print(AnArray.TheArray)
# print(AnArray.Length())
# print(AnArray.Get(2))
# AnArray.Set(0,10)
# print(AnArray.TheArray)
# AnArray.Remove(0)
# print(AnArray.TheArray)
#----------------------------------------------------------------------------------------------
# Stack
#----------------------------------------------------------------------------------------------
class Stack:
    def __init__(self):
        self.List = ArrayList()

    def Length(self):
        return self.List.count

    def push(self, i):
        self.List.Insert(0,i)

    def pop(self):
        return self.List.Remove(0)
#----------------------------------------------------------------------------------------------
# Stack Test
#----------------------------------------------------------------------------------------------
# aList = Stack()
# print(aList.Length())
# aList.push(1)
# print(aList.Length())
# print(aList.List.TheArray)
# aList.push(2)
# print(aList.Length())
# print(aList.List.TheArray)
# aList.pop()
# print(aList.Length())
# print(aList.List.TheArray)
#----------------------------------------------------------------------------------------------
# Queue
#----------------------------------------------------------------------------------------------
class Queue:

    def __init__(self):
        self.TheQueue = ArrayList()

    def Size(self):
        return self.TheQueue.count

    def enq(self,e):
        self.TheQueue.Append(e)

    def deq(self):
        return self.TheQueue.Remove(0)
#----------------------------------------------------------------------------------------------
# Queue Test
#----------------------------------------------------------------------------------------------
# Q = Queue()
# print(Q.TheQueue.TheArray)
# Q.enq(1)
# print(Q.TheQueue.TheArray)
# Q.enq(2)
# Q.enq(3)
# print(Q.TheQueue.TheArray)
# Q.deq()
# print(Q.TheQueue.TheArray)
# Q.deq()
# print(Q.TheQueue.TheArray)
#----------------------------------------------------------------------------------------------
# Linked Lists
#----------------------------------------------------------------------------------------------
class Node:
    def __init__(self,d,n):
        self.data = d
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def printList(self):
        if self.head == None:
            print("None")
            return
        else:
            ptr = self.head
            while ptr.next != None:
                print(ptr.data , " --> " , end="" , flush=True)
                ptr = ptr.next
            print(ptr.data, "--> None")

    def search(self, i):
        j = 0
        ptr = self.head
        while ptr != None:
            if ptr.data == i:
                return j
            ptr = ptr.next
            i += 1
        return -1

    def append(self,data):
        if self.head == None:
            self.head = Node(data,None)
        else:
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = Node(data,None)
        self.length += 1

    def insert(self, i, data):
        if self.head == None or i == 0:
            self.head = Node(data, self.head)
        else:
            ptr = self.head
            while i>1 and ptr.next != None:
                ptr = ptr.next
                i -= 1
            ptr.next = Node(data,ptr.next)
        self.length += 1

    def remove(self, i):
        if self.head == None:
            return None
        if i == 0:
            ToRemove = self.head.data
            self.head = self.head.data
            self.length -= 1
            return ToRemove
        ptr = self.head
        while ptr.next != None:
            if i == 1:
                ToRemove = ptr.next.data
                ptr.next = ptr.next.next
                self.length -= 1
                return ToRemove
            ptr = ptr.next
            i -= 1
#----------------------------------------------------------------------------------------------
# Linked Lists Test
#----------------------------------------------------------------------------------------------
# List = LinkedList()
# List.printList()
# List.append(1)
# List.printList()
# List.append(2)
# List.printList()
# List.append(3)
# List.insert(2,0)
# List.printList()
# print(List.search(1))
# List.remove(2)
# List.printList()
#----------------------------------------------------------------------------------------------
# Binary Tree Node
#----------------------------------------------------------------------------------------------
class btNode:
    def __init__(self, d, l=None, r=None):
        self.data = d
        self.left = l
        self.right = r

    def printTree(self):
        print(self.data)
        self.printTreeRec(self.left)
        self.printTreeRec(self.right)

    def printTreeRec(self,t):
        if t == None:
            return
        print(t.data)
        self.printTreeRec(t.left)
        self.printTreeRec(t.right)

        
#----------------------------------------------------------------------------------------------
# Depth-First Search
#----------------------------------------------------------------------------------------------
def dfSearch(t,d):
    if (t == None):
        return False
    if (t.data == d):
        return True
    if (dfSearch(t.left,d)):
        return True
    if (dfSearch(t.right,d)):
        return True
#----------------------------------------------------------------------------------------------
# Breadth-First Search
#----------------------------------------------------------------------------------------------
def bfSearch(t,d):
    Q = Queue()
    Q.enq(t)
    while (Q.Size() > 0):
        ptr = Q.deq()
        if (ptr == None):
            continue
        if (ptr.data == d):
            return True
        Q.enq(ptr.left)
        Q.enq(ptr.right)
    return False
#----------------------------------------------------------------------------------------------
# Binary Tree and Searches Test
#----------------------------------------------------------------------------------------------
# Tree = btNode(1,btNode(2,btNode(4,None,None),None),btNode(3,None,btNode(5,None,None)))
# Tree.printTree()
# print(dfSearch(Tree,1))
# print(dfSearch(Tree,2))
# print(dfSearch(Tree,3))
# print(dfSearch(Tree,4))
# print(dfSearch(Tree,5))
# print(dfSearch(Tree,0))
# print(dfSearch(Tree,6))
# print(bfSearch(Tree,1))
# print(bfSearch(Tree,2))
# print(bfSearch(Tree,3))
# print(bfSearch(Tree,4))
# print(bfSearch(Tree,5))
# print(bfSearch(Tree,0))
# print(bfSearch(Tree,6))
#----------------------------------------------------------------------------------------------
# Binary Tree
#----------------------------------------------------------------------------------------------
class BT:
    def __init__(self):
        self.root = None
        self.size = 0

    def search(self,d):
        ptr = self.root
        while ptr != None:
            if d == ptr.data:
                return True
            if d < ptr.data:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return False

    def add(self, d):
        self.size += 1
        if self.root == None:
            self.root = btNode(d,None,None)
            return
        ptr = self.root
        while True:
            if d < ptr.data:
                if ptr.left == None:
                    ptr.left = btNode(d,None,None)
                    return
                ptr = ptr.left
            else:
                if ptr.right == None:
                    ptr.right = btNode(d,None,None)
                    return
                ptr = ptr.right

    def remove(self,d):
        if self.root == None: return
        parentPtr = None
        ptr = self.root
        while ptr != None:
            if ptr.data == d:
                self.size -= 1
                return self.removeNode(ptr,parentPtr)
            parentPtr = ptr
            if d < ptr.data:
                ptr = ptr.left
            else:
                ptr = ptr.right

    def removeNode(self, ptr, parentPtr):
        def updateChild(ptr, oldChild, newChild): 
            if ptr == None:
                self.root = newChild
            elif ptr.left == oldChild:
                ptr.left = newChild
            elif ptr.right == oldChild:
                ptr.right = newChild
            else:
                print("error")
            if ptr.left == ptr.right == None:
                updateChild(parentPtr,ptr,None) 
            elif ptr.left == None:
                updateChild(parentPtr,ptr,ptr.right) 
            elif ptr.right == None:
                updateChild(parentPtr,ptr,ptr.left) 
            else:
                parentMinRNode = ptr
                minRNode = ptr.right
                while minRNode.left != None:
                    parentMinRNode = minRNode
                minRNode = minRNode.left
                ptr.data = minRNode.data 
                updateChild(parentMinRNode,minRNode,minRNode.right)
#----------------------------------------------------------------------------------------------
# Binary Tree Test
#----------------------------------------------------------------------------------------------
BTest = BT()
print(BTest.size)
BTest.add(5)
print(BTest.size)
print(BTest.search(5))
print(BTest.search(4))
print(BTest.remove(5))
print(BTest.search(5))
print(BTest.size)
print(BTest.add(5))
print(BTest.add(4))
print(BTest.add(8))
print(BTest.add(1))
print(BTest.add(16))
print(BTest.size)
print(BTest.search(5))
print(BTest.search(4))
print(BTest.search(8))
print(BTest.search(1))
print(BTest.search(16))
print(BTest.search(6))
#----------------------------------------------------------------------------------------------
# Heaps - TODO
#----------------------------------------------------------------------------------------------
