import heapq as heapq
#Maxheap is a binary tree where the value of the parent is greater than or equal to its children.
A=[2,3,8,-1,29,0,1]
n=len(A)
print("Original List:", A)
# To create a max heap, we can negate the values in the list and then use heapq to create a min heap.
for i in range(n):
    A[i] = -A[i]
heapq.heapify(A)
for i in range(n):
    A[i] = -A[i]
print("Max Heap:", A)
largest=heapq.heappop(A)
print("Largest element removed from Max Heap:", largest)
print("Wrong Max Heap after removing largest element:", A)
for i in range(n-1):
    A[i] = -A[i]
heapq.heapify(A)
for i in range(n-1):
    A[i] = -A[i]
print("Correct Max Heap after removing largest element:", A)