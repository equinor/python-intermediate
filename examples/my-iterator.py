class MyIterator:

    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        if self.idx > 6:
            raise StopIteration
        self.idx += 1
        return (self.idx - 1) ** 2

if __name__ == '__main__':
    m = MyIterator()
    for e in m:
        print(e)
    lst = [e for e in m]
    print(lst)
