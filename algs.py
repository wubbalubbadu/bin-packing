BIN_SIZE = 1


def first_fit(items):
    bins = []
    for item in items:
        for bin in bins:
            if item + bin <= BIN_SIZE:
                bin += item
                break
        else:
            bins.append(item)
    return len(bins)

def first_fit_desc(items):
    bins = []
    items.sort(reverse=True)
    for item in items:
        for bin in bins:
            if item + bin <= BIN_SIZE:
                bin += item
                break
        else:
            bins.append(item)
    return len(bins)
        
def best_fit(items):
    bins = []
    for item in items:
        best_bin = None
        for bin in bins:
            if item + bin <= BIN_SIZE and (best_bin is None or bin < best_bin):
                best_bin = bin
        if best_bin:
            best_bin += item
        else:
            bins.append(item)
    return len(bins)

def best_fit_desc(items):
    bins = []
    items.sort(reverse=True)
    for item in items:
        best_bin = None
        for bin in bins:
            if item + bin <= BIN_SIZE and (best_bin is None or bin < best_bin):
                best_bin = bin
        if best_bin:
            best_bin += item
        else:
            bins.append(item)
    return len(bins)

if __name__ == '__main__':
    # items = open('data.csv').readlines()
    items = [0.3, 0.2, 0.5, 0.3, 0.8, 0.4, 0.2, 0.9, 0.1, 0.01, 0.135]
    print("First Fit: number of bins used: %d" % first_fit(items))
    print("First Fit Descending: number of bins used: %d" % first_fit_desc(items))
    print("Best Fit: number of bins used: %d" % best_fit(items))
    print("Best Fit Descending: number of bins used: %d" % best_fit_desc(items))