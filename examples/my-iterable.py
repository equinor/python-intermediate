class MyIterable:

    def __getitem__(self, idx):
        if idx > 6:
            raise IndexError()
        return idx ** 2

if __name__ == '__main__':
    m = MyIterable()
    for e in m:
        print(e)
    lst = [e for e in m]
    print(lst)
