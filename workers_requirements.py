


def workers_requirements(requirements: list[int], 
                         k: int) -> int:
    n = len(requirements)
    total_shifts = 0
    active = [0]*n
    for h in range(n):
        if requirements[h] > active[h]:
            added = requirements[h] - active[h]
            total_shifts += added
            for i in range(h, min(h+k, n)):
                active[i] += added
    return total_shifts


def workers_requirements_sw(requirements: list[int], 
                            k: int) -> int:
    n = len(requirements)
    total_shifts = 0
    active = 0
    end_at = [0]*n
    for h in range(n):
        active -= end_at[h]
        if requirements[h] > active:
            added = requirements[h] - active
            total_shifts += added
            active += added
            if h+k < n:
                end_at[h+k] = added
    return total_shifts



if __name__ == "__main__":

    requirements = [0, 0, 2, 3, 1, 4, 6, 2, 0, 3, 1, 4, 2, 3, 5, 1, 0]
    k = 4
    print(workers_requirements_sw(requirements, k))
