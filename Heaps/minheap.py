import heapq as heapq
A=[2,3,8,-1,29,0,1]
#Minheap is a binary tree where the value of the parent is less than or equal to its childre.
heapq.heapify(A)
print(A)

#To add an element to the heap, use heappush
heapq.heappush(A, -5)
print(A)

#To remove the smallest element from the heap, use heapq.heappop()
smallest = heapq.heappop(A)
print(smallest)

#To print the smallest element without removing it, use A[0]
print(A[0])

def heapsort(A):
    sorted_list=[]
    n=len(A)
    for i in range(n):
        smallest = heapq.heappop(A)
        sorted_list.append(smallest)
    return sorted_list
sorted_A = heapsort(A)
print(sorted_A)
