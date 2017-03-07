fibbo = lambda aa, bb: (bb, (aa + bb))


def fibbbos(nos):
    sum = 0, 1
    for i in range(0, nos):
        sum = fibbo(sum[0], sum[1])
        yield(sum[0])

# nums = fibbbos(10)
# print(next(nums))
# print(next(nums))
# print(next(nums))
#
# fiboseries = list(map(fibbbos, [10, 20, 30]))
# print(fiboseries)

def gensqrs(n):
    for nos in range(1, n):
        yield nos ** 2


Sqrgen = gensqrs(100)

try:

    while True:
        print(next(Sqrgen))
except StopIteration:

    pass
