class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Listaligada:
    def __init__(self):
        self.head = None
        self.size = 0

    def inserir(self, element):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(element)
        else:
            self.head = Node(element)
        self.size += 1

    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("out of range")
        if pointer:
            return pointer.data
        raise IndexError("out of range")

    def __setitem__(self, index, element):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("out of range")
        if pointer:
            pointer.data = element
        else:
            raise IndexError("out of range")

    def sortedMerge(self, a, b):
        result = None

        if a == None:
            return b
        if b == None:
            return a

        # pick either a or b and recur..
        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result

    def mergeSort(self, h):

        if h == None or h.next == None:
            return h

        middle = self.getMiddle(h)
        nexttomiddle = middle.next

        middle.next = None

        left = self.mergeSort(h)

        right = self.mergeSort(nexttomiddle)

        sortedlist = self.sortedMerge(left, right)
        return sortedlist

    def getMiddle(self, head):
        if (head == None):
            return head

        slow = head
        fast = head

        while (fast.next != None and
               fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        return slow

    def testaCiclo(self):
        self.head = self.mergeSort(self.head)
        pointer = self.head
        for d in range(0, self.size -1):
            pointer1 = pointer.next
            if pointer.data == pointer1.data:
                return 1
            else:
                if pointer:

                    pointer = pointer.next
        return 0



if __name__ == '__main__':
    lista = Listaligada()
    n = int(input())
    for c in range(n):
        lista.inserir(int(input()))

    if lista.testaCiclo() == 1:
        print("1")
    else:
        print("0")
