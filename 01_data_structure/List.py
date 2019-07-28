int_data = [1, 2, 3, 4, 5, 6]
str_data = ['1', '2', '3', '4', '5', '6']

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

objec_data = []
init_object_data = [Node(1), Node(2), Node(3), Node(4), Node(5)]
for i in range(0, 5):
    objec_data.append(Node(i))

for node in init_object_data:
    print('list data')
    print(node.data)

node = init_object_data.pop()
print('pop node data')
print(node.data)

init_object_data.insert(0, Node(0))

print('insert object 0 data:')
print(init_object_data[0].data)

print('Index item')
index_list = [1, 2, 3, 4, 5]
print(index_list.index(3))

print('Count item ')
print(index_list.count(3))

print('Sort list')
sort_list = [1,3, 5, 7, 9, 2, 4]
sorted_list = sort_list.sort()

print(sorted_list)


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print('count: apple:', fruits.count('apple'))
print('index: apple:', fruits.index('apple'))
print('index from position: apple:',fruits.index('apple', 4))


''' Reserve '''
fruits.reverse()
print(fruits)

''' Sort '''
fruits.sort()
print(fruits)
