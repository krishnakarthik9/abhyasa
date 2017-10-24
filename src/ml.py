from data_loader import Data_Loader
import numpy as np

def main():
    data_path = './data'
    test_size_ratio = 0.1

    loader = Data_Loader(data_path)
    [train_img, train_labels, test_img, test_labels] = [np.array(x) for x in loader.load_all_data(test_size_ratio)]
    print train_img, train_labels, len(train_img), len(train_labels)
    print test_img, test_labels, len(test_img), len(test_labels)

if __name__ == '__main__':
    main()
