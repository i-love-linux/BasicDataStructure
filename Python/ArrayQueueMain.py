from BasicDS.ArrayQueue import ArrayQueue

if __name__ == "__main__":
    queue = ArrayQueue()

    for i in range(10):
        queue.enqueue(i)
        print(queue)
        if i % 3 == 2:
            queue.dequeue()
            print(queue)
