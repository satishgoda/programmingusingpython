__author__ = 'satish goda'

# (1, 3, 8, 2, 5, 7, 9) => ('1:3', '5', '7:9')

numbers = (1, 3, 8, 2, 5, 7, 9)

frames = sorted(set(numbers))


def collapse(sequence):
    def compact(s, e):
        fmt, args = ('{0}', (s,)) if s == e else ('{0}:{1}', (s, e))
        return fmt.format(*args)

    start, rest = sequence[0], iter(sequence[1:])
    end = start

    while True:
        try:
            current = rest.next()
        except StopIteration:
            yield compact(start, end)
            break
        else:
            if current == (end + 1):
                end = current
            else:
                yield compact(start, end)
                end = start = current

print list(collapse(frames))