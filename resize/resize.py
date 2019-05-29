from load_data import LoadData

class Resize:

    def __init__(self):
        data = LoadData()
        print(data.getInputValues())

    pass

if __name__ == '__main__':
    Resize()