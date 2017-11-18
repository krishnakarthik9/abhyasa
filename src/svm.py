import sys
import time
import pickle
import numpy as np
from sklearn import svm
from matplotlib import style
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score,confusion_matrix

class SVM(object):
    def __init__(self, train_img, train_labels, test_img, test_labels):
        self.train_img = train_img
        self.train_labels = train_labels
        self.test_img = test_img
        self.test_labels = test_labels

        # SVM classifier
        self.clf = svm.SVC(gamma=0.1, kernel='poly')

        np.set_printoptions(threshold=np.nan)
        style.use('ggplot')
        # Save all the SVM Print Statements in a Log file.
        self.old_stdout = sys.stdout
        self.log_file = open("outputs/logs/" + "summary_svm" + str(int(time.time())) + ".log","w+")
        sys.stdout = self.log_file

    def train(self):
        '''
        self.clf to fit train data
        '''
        print('\nSVM Classifier with gamma = 0.1; Kernel = polynomial')
        print('\nPickling the Classifier for Future Use...')
        self.clf.fit(self.train_img,self.train_labels)

        with open('svm.pickle','wb') as f:
            pickle.dump(self.clf, f)

    def predict(self, img):
        pickle_in = open('svm.pickle','rb')
        trained_clf = pickle.load(pickle_in)
        pickle_in.close()

        pred_label = trained_clf.predict(img)
        print(pred_label)
        sys.stdout = self.old_stdout
        self.log_file.close()


    def test(self):
        '''
        use self.clf to get score/accuracy
        prints accuracy
        draws plot
        '''
        self.train()

        pickle_in = open('svm.pickle','rb')
        trained_clf = pickle.load(pickle_in)
        pickle_in.close()

        print('\nCalculating Accuracy of trained Classifier...')
        acc = trained_clf.score(self.test_img,self.test_labels)

        print('\nMaking Predictions on Validation Data...')
        pred_labels = trained_clf.predict(self.test_img)

        print('\nCalculating Accuracy of Predictions...')
        accuracy = accuracy_score(self.test_labels, pred_labels)

        print('\nCreating Confusion Matrix...')
        conf_mat = confusion_matrix(self.test_labels,pred_labels)

        print('\nSVM Trained Classifier Accuracy: ',acc)
        print('\nPredicted Values: ',pred_labels)
        print('\nAccuracy of Classifier on Validation Images: ',accuracy)
        print('\nConfusion Matrix: \n',conf_mat)

        # close log_file and reset stdout
        sys.stdout = self.old_stdout
        self.log_file.close()

        return acc,pred_labels,accuracy,conf_mat


    def plots(self):
        acc,pred_labels,accuracy,conf_mat = self.test()
        plt.matshow(conf_mat)
        plt.title('Confusion Matrix for Test Data')
        plt.colorbar()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')
        # plt.show()
        plt.savefig('outputs/confusion_matrix.png')

        # Show the Test Images with Original and Predicted Labels
        a = np.random.randint(1,40,15)
        for i in a:
            two_d = (np.reshape(self.test_img[i], (45, 45)) * 255).astype(np.uint8)
            plt.title('Original Label: {0}  Predicted Label: {1}'.format(self.test_labels[i],pred_labels[i]))
            plt.imshow(two_d, interpolation='nearest',cmap='gray')
            # plt.show()
            plt.savefig('outputs/' + str(i) + '.png')