from module.decorator import timer


class CustomList:
    def __init__(self, *values):
        self.list = list(values)

    # @timer
    def __add__(self,other):
        if isinstance(other, list):
            return CustomList(*self.list, *other)
        elif isinstance(other, CustomList):
            return CustomList(*self.list, *other.list)
        else:
            return CustomList(*self.list, other)

    # @timer
    def __bool__(self):
        return bool(self.list)

    # @timer
    def __contains__(self, item):
        for val in self.list:
            if item == val:
                return True
        return False

    # @timer
    def __delitem__(self, index):
        del self.list[index]

    # @timer
    def __eq__(self, other):
        if isinstance(other, (list, CustomList)):
            return self.list == other
        else:
            raise TypeError("Cannot compare CustomList instance with type other than list or CustomList.")

    # @timer
    def __getitem__(self, index):
        return self.list[index]

    # @timer
    def __iter__(self):
        return self.generator()

    # @timer
    def __len__(self):
        return len(self.list)

    # @timer
    def __repr__(self):
        return repr(self.list)

    # @timer
    def __setitem__(self, index, value):
        self.list[index] = value

    # @timer
    def __str__(self):
        return "["+",".join([str(char) for char in self.list])+"]"

    # @timer
    def append(self, other):
        if isinstance(other,list):
            raise TypeError("Can't append list")
        else:
            self.list = [*self.list, other]

    # @timer
    def clear(self):
        self.list = []

    # @timer
    def count(self, value):
        count = 0
        for val in self.list:
            if val == value:
                count += 1
        return count

    # @timer
    def extend(self, other):
        if isinstance(other, list):
            self.list.extend(other)
        elif isinstance(other, CustomList):
            self.list.extend(other.list)
        else:
            raise TypeError("Can't extend type other than list or CustomList.")

    # @timer
    def generator(self):
        for val in self.list:
            yield val

    # @timer
    def index(self, value):
        for idx, val in enumerate(self.list):
            if val == value:
                return idx
        return -1

    # @timer
    def insert(self, index, value):
        if 0 <= index < len(self.list):
            self.list[index] = value
        else:
            raise IndexError("Index out of range.")

    # @timer
    def pop(self):
        if len(self.list)==0:
            raise IndexError("Cannot pop from an empty list.")
        temp = self.list[-1]
        del self.list[-1]
        return temp

    # @timer
    def reverse(self):
        self.list = self.list[::-1]

    # @timer
    def remove(self,value):
        for idx,val in enumerate(self.list):
            if val == value:
                del self.list[idx]
                return
        raise ValueError("Value not in CustomList.")


    # @timer
    def sort(self,func=None, reverse=False):
        self.list.sort(key=func, reverse=reverse)


# if __name__=="__main__":
#     new_list = CustomList(1,2,3)
    # print(len(new_list))        #len          1.0     O(1)
    # print(new_list)             #str          2.1     O(N)
    # print(new_list[1])          #getitem      0.0     O(1)
    # print(new_list[0:2])        #getitem      0.0     O(1)
    # del new_list[0]             #delitem      1.2     O(N)
    # new_list[0] = 10            #setitem      0.0     O(1)
    # new_list += new_list        #add          2.1     O(N)
    # new_list.append(33)         #append       1.2     O(1)
    # new_list.extend(new_list)   #extend       1.0     O(N)
    # new_list.reverse()          #reverse      1.2     O(N)
    # new_list.sort(None, True)   #sort         1.0     O(NlogN)
    # print(new_list.count(1))    #count        1.2     O(N)
    # print(new_list.pop())       #pop          1.0     O(1)
    # print(new_list.index(1))    #index        1.0     O(N)
    # new_list.remove(2)          #remove       2.9     O(N)
    # new_list.insert(1,20)       #insert       1.2     O(N)
    # print(not new_list)         #bool         0.7     O(1)
    # print(33 in new_list)       #contains     1.0     O(N)
    # print(new_list == [1,2,3])  #eq           1.2     O(N)
    # print(new_list != [1,2,3])  #eq           1.0     O(N)
    # print(new_list == new_list)
    # new_list.clear()            #clear        0.0     O(1)
    # for val in new_list.generator():    #generator  1.O     O(N)
    #     print(val)
    # for val in new_list:            #generator 0.0      O(N)
    #     print(val)                  #iter       14.8    ?


