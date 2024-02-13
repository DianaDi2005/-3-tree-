class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#в res мы сохраняем сумму всех ветвей дерева
def sum_value(node, res=[]):
    # если у узла дерева node нет потомков (правого и левого), то это конечная ветка данной ветви => сохраняем в res сумму
    if node.right is None and node.left is None:
        res.append(node.value)

    # проверяем, есть ли у узла правый потомок
    if node.right is not None:
        node.right.value += node.value #значение правого потомка увеличивается на значение узла
        sum_value(node.right) #для правого потомка

    # проверяем, если ли у узла левый потомок
    if node.left is not None:
        node.left.value += node.value #значение левого потомка увеличиваем на значение узла
        sum_value(node.left) #применяем еще раз для левого потомка

    return res

print("Введите массив дерева: ")
s = str(input()).split(',')
arr = []
for i in s:
    if i != '':
        arr.append(int(i))
    else:
        arr.append(None)

print("Введите, какую сумму вы хотите проверить: ")
summa = int(input())

# меняем массив так, что если есть узел None, то из него исходит еще две ветки None and None
for i in range(0,len(arr)):
    if arr[i] is None:
        n = 0  #номер строки
        index = i  #индекс элемента в строке
        while index - 2 ** n >= 0:
            index -= 2 ** n
            n += 1

        arr_2 = set(arr[i - index + 2**n: ])#создаем множество из элементов, после n
        if len(arr_2) == 1 and None is arr_2: #если есть None данная строка последняя
            arr = arr[:-2] #под последней строкой появятся два None, их следует удалить
            break

        else:
            new_ind = 2 **(n+1) - 1 + index*2  #индекс первого пустого элемента в строке
            arr.insert(new_ind, None) #добавляем в следующую строку два элемента None
            arr.insert(new_ind + 1, None)

def create_tree(arr):
    def build_tree(index):
        if index < len(arr) and arr[index] is not None:
            root = Node(arr[index]) #создаем узел дерева с начальным значением
            root.left = build_tree(2 * index + 1) #строим левую ветвь дерева
            root.right = build_tree(2 * index + 2) #строим правую ветвь дерева
            return root
        else:
            return None
    return build_tree(0)


def find_summa(root, summa, road=[]):
    if not root:
        return
    # добавляем текущее значение узла
    road.append(root.value)
    # если у узла нет потомков, то мы возвращаем ветку дерева
    if not root.left and not root.right and sum(road) == summa:
        return road

    left = find_summa(root.left, summa, road[:])
    if left:
        return left

    right = find_summa(root.right, summa, road[:])
    if right:
        return right


summa_tree = sum_value(create_tree(arr))
if summa in summa_tree:
    print(find_summa(create_tree(arr), summa))
else:
    print("Данной суммы нет")



