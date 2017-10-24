class SVM(object):
    def __init__(self, train_img, train_labels, test_img, test_labels):
        self.train_img = train_img
        self.train_labels = train_labels
        self.test_img = test_img
        self.test_labels = test_labels

        # SVM classifier
        self.clf = None

    def train(self):
        '''
        self.clf to fit train data
        '''
        pass

    def test(self):
        '''
        use self.clf to get score/accuracy
        prints accuracy
        draws plot
        '''
        pass
