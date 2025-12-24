def countfreq(arr,freq=None):
    if freq is None:
        freq = {}
    for item in arr:
        if type(item) == list:
            countfreq(item,freq)
        else:
            freq[item] = freq.get(item,0) + 1
    return freq
