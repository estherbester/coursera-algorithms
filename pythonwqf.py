class WQuickFind(object):
    seed = range(10)
    sizes = [1 for i in seed]
    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def root(self, i):
        while i != self.seed[i]:
            i = self.seed[i]
        return i



    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)

        self.seed[i] = j

    def quickunion(self, p, q):
        i = self.root(p)
        j = self.root(q)
        print i
        if self.sizes[i] < self.sizes[j]:
                self.seed[i] = j
                self.sizes[j] += self.sizes[i]
        else:
                self.seed[j] = self.seed[i]
                self.sizes[i] += self.sizes[j]

if __name__== "__main__":
    wqf = WQuickFind()
    print wqf.seed
    print wqf.sizes

    wqf.quickunion(7,6)
    wqf.quickunion(8,4)
    wqf.quickunion(0,3)
    wqf.quickunion(9,5)
    wqf.quickunion(3,7)
    wqf.quickunion(7,1)
    wqf.quickunion(9,8)
    wqf.quickunion(6,2)
    wqf.quickunion(5,7)


    print wqf.seed
    # results :[0, 0, 0, 0, 8, 9, 7, 0, 9, 0]
