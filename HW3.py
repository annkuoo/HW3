def print_v(v):
    print(" ".join(map(str, v)))
    print()

def quick_sort(v, start, end, count):
    if start < end:
        pivot = v[start]
        i = start
        j = end
        while i < j:
            while i < len(v) and v[i] <= pivot:
                i += 1
            while v[j] > pivot:
                j -= 1
            if i < j:
                v[i], v[j] = v[j], v[i]
                count[0] += 1
                print(f"{count[0]}: ")
                print_v(v)
        v[start], v[j] = v[j], v[start]
        count[0] += 1
        print(f"{count[0]}: ")
        print_v(v)
        quick_sort(v, start, j - 1, count)
        quick_sort(v, j + 1, end, count)

def initialize(v):
    v.extend([33, 67, 8, 13, 54, 119, 3, 84, 25, 41])

def main():
    v = []
    initialize(v)
    count = [0]

    # print out the initial vector
    print_v(v)

    # QS
    quick_sort(v, 0, len(v) - 1, count)

    # print out the final result
    print("Final result:")
    print_v(v)

if __name__ == "__main__":
    main()
