import random
BIN_SIZE = 1


def first_fit(i):
    bins = []
    items = i.copy()
    for i, item in enumerate(items):
        for j, bin in enumerate(bins):
            if item + bin <= BIN_SIZE:
                bins[j] += item
                break
        else:
            bins.append(item)
    # print("first fit bins")
    # print(bins)
    # print(sum(bins))
    return len(bins)

def first_fit_desc(i):
    bins = []
    items = i.copy()
    items.sort(reverse=True)
    for i, item in enumerate(items):
        for j, bin in enumerate(bins):
            if item + bin <= BIN_SIZE:
                bins[j] += item
                break
        else:
            bins.append(item)
   
    # print("first fit desc bins")
    # print(sum(bins))
    # print(bins)
    return len(bins)
        
def best_fit(i):
    items = i.copy()
    bins = []
    for i, item in enumerate(items):
        best_bin_index = None
        best_bin = None
        for j, bin in enumerate(bins):
            if item + bin <= BIN_SIZE and (best_bin is None or bin > best_bin):
                best_bin_index = j
                best_bin = bin
        if best_bin:
            bins[best_bin_index] += item
        else:
            bins.append(item)
    # print("best fit bins")
    # print(sum(bins))
    # print(bins)
    return len(bins)

def best_fit_desc(i):
    items = i.copy()
    items.sort(reverse=True)
    bins = []
    for i, item in enumerate(items):
        best_bin_index = None
        best_bin = None
        for j, bin in enumerate(bins):
            if item + bin <= BIN_SIZE and (best_bin is None or bin > best_bin):
                best_bin_index = j
                best_bin = bin
        if best_bin:
            bins[best_bin_index] += item
        else:
            bins.append(item)
    # print("best fit bins")
    # print(sum(bins))
    # print(bins)
    return len(bins)
    # print("best fit desc bins")
    # print(sum(bins))
    # print(bins)
    return len(bins)

if __name__ == '__main__':
    # items = open('data.csv').readlines()
    num_items = 30000
    # items = [random.random() * 0.5 for i in range(num_items//2)] + [0.5 + random.random() * 0.5 for i in range(num_items//2)]
    # print(sum(items))
    items = [0.2, 0.5, 0.4, 0.7, 0.1, 0.3, 0.8]
    print("First Fit: number of bins used: %d" % first_fit(items))

    print("First Fit Descending: number of bins used: %d" % first_fit_desc(items))

    print("Best Fit: number of bins used: %d" % best_fit(items))

    print("Best Fit Descending: number of bins used: %d" % best_fit_desc(items))
