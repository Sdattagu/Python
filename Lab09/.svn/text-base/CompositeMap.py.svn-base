class Entry:

    #key - an (int, int) tuple representing the lookup key.
    #value - A string representing the corresponding value of the key.

    def __init__(self, k1, k2, v):
        #Init an entry instance with the given params
        #Sets equivalent member vars
            #k1 and k2 are int elements of the tuple key
            #v is the string value

        blah = []

        if(type(k1) == int and type(k2) == int and type(v) == str):
            blah.append(k1)
            blah.append(k2)
            self.key = tuple(blah)
            self.value = v
        else:
            raise TypeError("k1 and k2 are not ints, or v is not a str.")

        
    def __str__(self):
        #Return a string representation of the entry in the following format:
        #(k1, k2): "value"

        result = ""
        result += str(self.key) + ": "
        result += '"'
        result += self.value
        result += '"'

        #print(result)
        return result


    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        #Return true iff (Entry1 == Entry2)
        result = False
        if(self.key[0] == other.key[0]):
            if(self.key[1] == other.key[1]):
                result = True

        return result

class Lookup:

    def __init__(self, name):
        #Init an instance of the lookup class
        #Pass and set the name
            #Name is NOT allowed to be empty
                #raise ValueError with appropo message
        #Init the backing store

        self._container = set()
        if(not name or len(name) == 0):
            raise ValueError("name is not allowed to be empty.")
        else:
            self._name = name

    def __str__(self):
        result = ""

        result += "["
        result += '"'
        result += self._name
        result += '"'
        result += ": "
        result += format(len(self._container), '2.0f')
        result += " Entries]"

        #print(result)
        return result
        pass

    def add(self, entry):

        for item1 in self._container:
            if(entry.key == item1.key):
                raise KeyError("Cannot add entry with matching key.")

        self._container.add(entry)

        pass

    def update(self, entry):

        flag = False
        for item1 in self._container:
            if(entry.key == item1.key):
                item1.value = entry.value
                flag = True

        if(flag == False):
            raise KeyError("Entry does not exist.")

        pass

    def addOrUpdate(self, entry):
        return self.add(entry) or self.update(entry)

    def remove(self, entry):
        flag = False
        for item1 in self._container:
            if(entry.key == item1.key):
                item1.value = entry.value
                flag = True

        if(flag == False):
            raise KeyError("Entry does not exist.")
        else:
            self._container.remove(entry)

    def count(self):

        return len(self._container)

if __name__ == '__main__':

    A = Entry(11, 9, "The apocalypse begins")
    #print(str(A))
    B = Entry(11, 8, "blah")
    D = Entry(10, 9, "hah")
    #print(A == B)
    C = Lookup("blah")
    C.add(A)
    print(C)
    #C.update(B)
    C.add(B)
    #print(C)
    #C.update(A)
    C.addOrUpdate(D)
    print(C.count())

    pass
