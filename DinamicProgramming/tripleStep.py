# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time. Implement a method to count how many possible ways the child can run up the
# stairs.

#approccio ricorsivo
def makeStep(steps):
    if steps <= 3:
        return steps        
    return makeStep(steps-1)+makeStep(steps-2)+makeStep(steps-3)


def makeStepDynamic(steps):
    memo = []
    memo.append(0)
    memo.append(1)
    memo.append(2)
    memo.append(3)

    for i in range(4,steps+1):
        memo.append(memo[i-1]+memo[i-2]+memo[i-3])

    return memo[steps]


if __name__ == "__main__":
    n = 6
    print(f'For n={n} we have {makeStep(n)} paths')
    print(f'For n={n} we have {makeStepDynamic(n)} dynamic paths')
