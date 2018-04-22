import multiprocessing as mp

def job(q):
	res = 0
	for i in range(3):
		res += i+i**2+i**3
	q.put(res)

# 共享内存,共享值,共享数组,只能进行这个进行内存间的数据交流
value = mp.Value('d',1)
array = mp.Array('i',[1,2,3])

# 进程锁


if __name__ == '__main__':
	q = mp.Queue()
	p1 = mp.Process(target=job,args=(q,))
	p1.start()
	p1.join()
	print(q)
	print(q.get())