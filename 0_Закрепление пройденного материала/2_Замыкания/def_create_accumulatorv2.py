def create_accumulator(start:int=0):
    def summator(num):
        nonlocal start
        start+=num
        return start
    return summator