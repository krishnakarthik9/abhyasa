import os
import PIL
import numpy as np
from PIL import Image

class Data_Loader(object):
    def __init__(self, path='./data'):
        '''
        The folder that path points is expected to have all the data folders i.e,
        A, B,...
        '''
        self.path = path
        self.features_train = []
        self.labels_train = []
        self.features_test = []
        self.labels_test = []

    def get_all_folder_names(self):
        '''
        returns the folder names i.e, ["A", "B", ...]
        '''
        folder_names = [name for name in os.listdir(self.path) if os.path.isdir(os.path.join(self.path, name))]
        return folder_names

    def load_data_from_folder(self, folder_name):
        '''
        returns {features, labels} for a given folder(Ex: A)
        '''
        folder_path = self.path + "/" + folder_name
        features = []
        labels = []
        for file in os.listdir(folder_path):
            try:
                file_path = folder_path + "/" + file
                img = np.asarray(Image.open(file_path).convert('L').resize((45,45), Image.ANTIALIAS)).flatten()
                features.append(img)
                labels.append(folder_name)
            except Exception as e:
                print(e)
        return features, labels

    def load_all_data(self, test_size_ratio):
        '''
        test_size_ratio:
            ratio of total data that we want to test on,
            remaining will be used for training
        returns [features_train, labels_train, features_test, labels_test]
        '''

        folders_list = self.get_all_folder_names()
        for folder in folders_list:
            features, labels = self.load_data_from_folder(folder)
            data_size = len(features)
            train_set_size = int((1.0 - test_size_ratio) * data_size)
            self.features_train += features[:train_set_size]
            self.labels_train += labels[:train_set_size]
            self.features_test += features[train_set_size:]
            self.labels_test += labels[train_set_size:]

        return [self.features_train,
                self.labels_train,
                self.features_test,
                self.labels_test]
