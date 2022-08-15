def tower(n, sourcePole, destPole, auxPole):
    if n == 0:
        return 1
    # Move first disk from sourcePole to Auxilary pole using destination pole in the middle
    tower(n-1, sourcePole, auxPole, destPole)
    print('Move the disk ', n, ' from ', sourcePole, ' to ', destPole)
    tower(n-1, sourcePole, destPole, auxPole)

if __name__ == '__main__':
    tower(3, 'S', 'D', 'A')