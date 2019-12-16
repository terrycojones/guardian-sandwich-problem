#!/usr/bin/env python


def _solve(currentDigits, availableDigitCounts, solutions):
    """
    Return a list of solutions formed by extending the current solution.
    """

    # This is a bit dumb. Better would be to pre-populate current digits with
    # all the instances of a given digit seeing as we know where they must all
    # fall, instead of doing them one by one.  See solve-faster.py

    # print('_solve:', currentDigits, availableDigitCounts)

    # Check the last digit that was added to currentDigits is ok.
    if currentDigits:
        n = len(currentDigits)
        lastDigit = currentDigits[n - 1]
        index = n - 2
        while index >= 0:
            if currentDigits[index] == lastDigit:
                if n - 2 - index == lastDigit:
                    break
                else:
                    return
            index -= 1

    if sum(availableDigitCounts) == 0:
        solutions.append(currentDigits)
    else:
        for index, count in enumerate(availableDigitCounts):
            if count:
                availableDigitCounts[index] -= 1
                _solve(currentDigits + [index + 1], availableDigitCounts,
                       solutions)
                availableDigitCounts[index] += 1


def solve(availableDigitCounts):
    solutions = []
    _solve([], availableDigitCounts, solutions)

    print('solutions for', availableDigitCounts)
    for solution in solutions:
        print(''.join(map(str, solution)))


solve([2, 2, 2, 2])
solve([3] * 9)


# solutions for [2, 2, 2, 2]
# 23421314
# 41312432

# solutions for [3, 3, 3, 3, 3, 3, 3, 3, 3]
# 181915267285296475384639743
# 191218246279458634753968357
# 191618257269258476354938743
# 347839453674852962752816191
# 347936483574692582762519181
# 753869357436854972642812191
