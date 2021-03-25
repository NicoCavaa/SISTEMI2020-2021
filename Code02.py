def enqueue(queue, element):
    queue.append(element)


def dequeue(queue):
    return queue.pop(0)


def push(stack, element):
    stack.append(element)


def pop(stack):
    return stack.pop()


def main():
    queue = []
    stack = []

    enqueue(queue, int(input('Numero: ')))

    while input('Vuoi continuare(si/no): ') != 'no':
        enqueue(queue, int(input('Numero: ')))
    
    for i in range(len(queue)):
        push(stack, dequeue(queue))
    
    for i in range(len(stack)):
        enqueue(queue,pop(stack))

    for element in queue:
        print(element)


if __name__ == "__main__":
    main()