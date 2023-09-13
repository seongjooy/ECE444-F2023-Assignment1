class Utils:
    def reversed(number):
        if isinstance(number, int):
            return str(number)[::-1]
        else:
            raise ValueError("Please input an integer")

    def formatter(number):
        if isinstance(number, int):
            return [bin(number), oct(number)] 
        else:
            raise ValueError("Please input an integer")