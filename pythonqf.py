
class QuickFind(object):
    seed_array = range(10)
    array_sizes = {}

    def union(self, p, q):
		pid = self.seed_array[p]
		qid = self.seed_array[q]

		for index, item in enumerate(self.seed_array):
			if self.seed_array[index] == pid:
				self.seed_array[index] = qid



if __name__ == "__main__":
	print QuickFind.seed_array
	qf = QuickFind()
	qf.union(9,3)
	qf.union(0,7)
	qf.union(6,5)
	qf.union(1,7)
	qf.union(4,5)
	qf.union(9,1)
	print qf.seed_array
    # resulted in [7, 7, 2, 7, 5, 5, 5, 7, 8, 7]