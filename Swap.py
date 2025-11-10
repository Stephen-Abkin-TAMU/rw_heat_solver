def Swap(this_glob, that_glob):
    temp = this_glob.location
    this_glob.location = that_glob.location
    that_glob.location = temp

    temp = this_glob.value
    this_glob.value = that_glob.value
    that_glob.value = temp
