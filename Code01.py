def enqueue(queue, element):
    queue.append(element)


def dequeue(queue):
    return queue.pop(0)


def main():
    queue = []

    enqueue(queue, int(input('numero: ')))

    while input('Vuoi continuare(si/no): ') != 'no':
        enqueue(queue, int(input('numero; ')))

    for i in range(len(queue)):
        print(dequeue(queue))


if __name__ == '__main__':
    main()