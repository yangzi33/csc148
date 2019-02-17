def f(x):
        q = Queue()
        for e in x:
            q.enqueue(e)

        while not q.is_empty():
            i = q.dequeue()
            if not isinstance(i, list):
                print(i)
            else:
                for e in i:
                     q.enqueue(e)
