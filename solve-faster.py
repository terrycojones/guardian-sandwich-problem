#!/usr/bin/env python


def findAvailableIndices(digit, count, template):
    length = len(template)
    for start in range(length):
        offsets = list(range(start, length, digit + 1))[:count]
        if len(offsets) != count:
            return
        if all(template[i] is None for i in offsets):
            yield offsets


def _solve(availableDigitCounts, template, solutions):
    freeSlotCount = sum(slot is None for slot in template)
    if freeSlotCount:
        assert sum(availableDigitCounts) == freeSlotCount
        for i in range(len(availableDigitCounts) - 1, -1, -1):
            if availableDigitCounts[i]:
                firstFreeIndex = i
                digit = firstFreeIndex + 1
                break
        assert digit > 0

        for availableIndices in findAvailableIndices(
                digit, availableDigitCounts[firstFreeIndex], template):
            for availableIndex in availableIndices:
                template[availableIndex] = digit
            originalCount = availableDigitCounts[firstFreeIndex]
            availableDigitCounts[firstFreeIndex] = 0
            _solve(availableDigitCounts, template, solutions)
            for availableIndex in availableIndices:
                template[availableIndex] = None
            availableDigitCounts[firstFreeIndex] = originalCount
    else:
        assert sum(availableDigitCounts) == 0
        solutions.append(''.join(map(str, template)))


def solve(availableDigitCounts):
    template = [None] * sum(availableDigitCounts)
    solutions = []
    _solve(availableDigitCounts, template, solutions)

    print('solutions for', availableDigitCounts)
    for solution in solutions:
        print(solution)


solve([2] * 4)
solve([3] * 9)


# $ time solve-faster.py

# solutions for [2, 2, 2, 2]
# 41312432
# 23421314

# solutions for [3, 3, 3, 3, 3, 3, 3, 3, 3]
# 191618257269258476354938743
# 191218246279458634753968357
# 181915267285296475384639743
# 347936483574692582762519181
# 753869357436854972642812191
# 347839453674852962752816191

# 0.17user 0.00system 0:00.17elapsed 98%CPU (0avgtext+0avgdata 8180maxresident)k
# 0inputs+0outputs (0major+1121minor)pagefaults 0swaps
