def create_accumulator():
    local1 = 0
    def summator(local2):
        nonlocal local1
        local1+=local2
        return local1
    return summator