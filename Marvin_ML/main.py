# -*- coding: utf-8 -*-
"""
@author: Enrico
"""
import numpy
import pandas as pd
import matplotlib.pyplot as plt
import preprocessing as pre
import gaussian_classifier as gauss
import logisticRegression_classifier as logReg
#import svm
#import gmm
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from operator import attrgetter
from collections import namedtuple

K = 5
split_ratio = 2.0/3.0

def preprocecing_plot(D, L, DG):
    # Change default font size - comment to use default values
    plt.rc('font', size=16)
    plt.rc('xtick', labelsize=16)
    plt.rc('ytick', labelsize=16)
    
    pre.plot_hist(DG, L, "gaussianized")
    pre.plot_hist(D, L, "row")
    pre.plot_pearson_correlation_heatmap(D, "Whole dataset row", "Greys")
    pre.plot_pearson_correlation_heatmap(D[:, L==0], "Benign row", "Blues")
    pre.plot_pearson_correlation_heatmap(D[:, L==1], "SDC row", "Reds")
    pre.plot_pearson_correlation_heatmap(DG, "Whole dataset gauss", "Greys")
    pre.plot_pearson_correlation_heatmap(DG[:, L==0], "Benign gauss", "Blues")
    pre.plot_pearson_correlation_heatmap(DG[:, L==1], "SDC gauss", "Reds")




def gaussian_classifier(D, L, DG):
    print("\n\nGaussian Classifier\n")
    
    print("\n5-folds - Raw data")
    
    print("\nNo PCA")
    print("pi = 0.5 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, D, L, 0.5, 1, 1, 42)
    print("pi = 0.1 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, D, L, 0.1, 1, 1, 42)
    print("pi = 0.9 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, D, L, 0.9, 1, 1, 42)
   
    '''
    print("\nPCA = 7")
    print("pi = 0.5 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, D, L, 0.5, 1, 1, 7)
    print("pi = 0.1 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, D, L, 0.1, 1, 1, 7)
    print("pi = 0.9 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, D, L, 0.9, 1, 1, 7)
    
    print("\nPCA = 6")
    print("pi = 0.5 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, D, L, 0.5, 1, 1, 6)
    print("pi = 0.1 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, D, L, 0.1, 1, 1, 6)
    print("pi = 0.9 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, D, L, 0.9, 1, 1, 6)
    
    print("\nPCA = 5")
    print("pi = 0.5 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, D, L, 0.5, 1, 1, 5)
    print("pi = 0.1 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, D, L, 0.1, 1, 1, 5)
    print("pi = 0.9 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, D, L, 0.9, 1, 1, 5)
    
    print("\nPCA = 4")
    print("pi = 0.5 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, D, L, 0.5, 1, 1, 4)
    print("pi = 0.1 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, D, L, 0.1, 1, 1, 4)
    print("pi = 0.9 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, D, L, 0.9, 1, 1, 4)
    
    print("\n\n5-folds - Gaussianized data")
    
    print("\nNo PCA")
    print("pi = 0.5 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, DG, L, 0.5, 1, 1, 8)
    print("pi = 0.1 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, DG, L, 0.1, 1, 1, 8)
    print("pi = 0.9 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, DG, L, 0.9, 1, 1, 8)
   
    print("\nPCA = 7")
    print("pi = 0.5 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, DG, L, 0.5, 1, 1, 7)
    print("pi = 0.1 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, DG, L, 0.1, 1, 1, 7)
    print("pi = 0.9 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, DG, L, 0.9, 1, 1, 7)
    
    print("\nPCA = 6")
    print("pi = 0.5 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, DG, L, 0.5, 1, 1, 6)
    print("pi = 0.1 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, DG, L, 0.1, 1, 1, 6)
    print("pi = 0.9 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, DG, L, 0.9, 1, 1, 6)
    
    print("\nPCA = 5")
    print("pi = 0.5 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, DG, L, 0.5, 1, 1, 5)
    print("pi = 0.1 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, DG, L, 0.1, 1, 1, 5)
    print("pi = 0.9 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, DG, L, 0.9, 1, 1, 5)
    
    print("\nPCA = 4")
    print("pi = 0.5 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, DG, L, 0.5, 1, 1, 4)
    print("pi = 0.5 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, DG, L, 0.1, 1, 1, 4)
    print("pi = 0.5 - Cfn = 1 - Cfp = 1")
    gauss.kfold(K, DG, L, 0.9, 1, 1, 4)
    '''

def logisticRegrassion_classifier(D,L, DG):
    print("\n\nLogistic Regression Classifier\n")
    
    # print("\nRaw data")
    # logReg.plot_lambda(K, D, L, [0.5, 0.1, 0.9], "raw") #Lambda minDCF plot - No PCA piT = 0.5
    # logReg.plot_lambda(K, D, L, [0.5, 0.1, 0.9], "raw", 7) #Lambda minDCF plot - PCA = 7 piT = 0.5
    # print("\nGaussinized data")
    # logReg.plot_lambda(K, DG, L, [0.5, 0.1, 0.9], "gauss")   #
    # logReg.plot_lambda(K, DG, L, [0.5, 0.1, 0.9], "gauss", 7) #Lambda minDCF plot - PCA = 7 piT = 0.5    
    
    print("\nLambda 0 minDCF - No PCA")
    
    minDCF = logReg.kfold(K, D, L, 0.5, 0.5, 1, 1, 0)
    print("\npiT = 0.5 pi = 0.5    ", minDCF )
    '''
    minDCF = logReg.kfold(K, D, L, 0.5, 0.1, 1, 1, 0)
    print("\npiT = 0.1 pi = 0.5    ", minDCF )
   
    minDCF = logReg.kfold(K, D, L, 0.5, 0.9, 1, 1, 0)
    print("\npiT = 0.9 pi = 0.5    ", minDCF )
    
    minDCF = logReg.kfold(K, D, L, 0.1, 0.5, 1, 1, 0)
    print("\npiT = 0.5 pi = 0.1    ", minDCF )
   
    minDCF = logReg.kfold(K, D, L, 0.1, 0.1, 1, 1, 0)
    print("\npiT = 0.1 pi = 0.1    ", minDCF )
   
    minDCF = logReg.kfold(K, D, L, 0.1, 0.9, 1, 1, 0)
    print("\npiT = 0.9 pi = 0.1    ", minDCF )
    
    minDCF = logReg.kfold(K, D, L, 0.9, 0.5, 1, 1, 0)
    print("\npiT = 0.5 pi = 0.9    ", minDCF )
    
    minDCF = logReg.kfold(K, D, L, 0.9, 0.1, 1, 1, 0)
    print("\npiT = 0.1 pi = 0.9    ", minDCF )
    
    minDCF = logReg.kfold(K, D, L, 0.9, 0.9, 1, 1, 0)
    print("\npiT = 0.9 pi = 0.9    ", minDCF )
    
    
    print("\nLambda 0 minDCF - PCA = 7")
    
    minDCF = logReg.kfold(K, D, L, 0.5, 0.5, 1, 1, 0, 7)
    print("\npiT = 0.5 pi = 0.5    ", minDCF )
    
    minDCF = logReg.kfold(K, D, L, 0.5, 0.1, 1, 1, 0, 7)
    print("\npiT = 0.1 pi = 0.5    ", minDCF )
   
    minDCF = logReg.kfold(K, D, L, 0.5, 0.9, 1, 1, 0, 7)
    print("\npiT = 0.9 pi = 0.5    ", minDCF )
    
    minDCF = logReg.kfold(K, D, L, 0.1, 0.5, 1, 1, 0, 7)
    print("\npiT = 0.5 pi = 0.1    ", minDCF )
   
    minDCF = logReg.kfold(K, D, L, 0.1, 0.1, 1, 1, 0, 7)
    print("\npiT = 0.1 pi = 0.1    ", minDCF )
   
    minDCF = logReg.kfold(K, D, L, 0.1, 0.9, 1, 1, 0, 7)
    print("\npiT = 0.9 pi = 0.1    ", minDCF )
    
    minDCF = logReg.kfold(K, D, L, 0.9, 0.5, 1, 1, 0, 7)
    print("\npiT = 0.5 pi = 0.9    ", minDCF )
    
    minDCF = logReg.kfold(K, D, L, 0.9, 0.1, 1, 1, 0, 7)
    print("\npiT = 0.1 pi = 0.9    ", minDCF )
    
    minDCF = logReg.kfold(K, D, L, 0.9, 0.9, 1, 1, 0, 7)
    print("\npiT = 0.9 pi = 0.9    ", minDCF )    
    '''


def bayes_err_plot(D,L):
    print("Bayes Error plots")
    print("Gaussian Tied - raw - PCA = 7 - pi = 0.5")
    gauss.kfold(K, D, L, 0.5, 1, 1, 42, True)
    
    '''
    print("Logistic Regression - raw - PCA = 7 - pit = 0.5 - not regularized")
    logReg.kfold(K, D, L, 0.5, 0.5, 1, 1, 0, 7, True)
    
    print("Logistic Regression - raw - PCA = 7 - pi = 0.1 - not regularized")
    logReg.kfold(K, D, L, 0.1, 0.1, 1, 1, 0, 7, True)
    
    print("linear SVM unbalanced - raw - PCA = 7 - C = 0.1")
    svm.kfold(K, D, L, "linear", False, 0.5, 0.5, 1, 1, 1, 0.1, 7, True)
    
    print("gmm full 32 comp - raw - PCA = 7")
    gmm.kfold(K, D, L, "full", 0.5, 0.5, 1, 1, 32, 7, True)
    '''
    
def evaluetion_test(DTrain, LTrain, DTest, LTest):
    #gauss.test(DTrain, LTrain, DTest, LTest, 0.5, 1, 1, 42)
    logReg.test(DTrain, LTrain, DTest, LTest, 0.5, 0.5, 1, 1, 0) #K, D, L, 0.5, 0.5, 1, 1, 0 
    #svm.test(DTrain, LTrain, DTest, LTest, "linear", False, 0.9, 0.5, 1, 1, 1, 0.1, 7)
    #gmm.test(DTrain, LTrain, DTest, LTest, "full", 0.9, 0.9, 1, 1, 32, 7)
  
def recall_precision(L, LPred): #0 = negative 1 = positive
    TP = 0 
    FP = 0 
    FN = 0
    TN = 0
    for index in range(L.shape[0]):
        
        if L[index] == 0 and LPred[index] == 0:
            TN +=1
        if L[index] == 1 and LPred[index] == 1:
            TP +=1
        if L[index] == 0 and LPred[index] == 1:
            FP +=1
        if L[index] == 1 and LPred[index] == 0:
            FN +=1
            
    recall = TP/(TP+FN)
    precision = TP/(TP+FP)
    return recall, precision
  
bench = "sha"
events = ["Level 1 instruction cache refill", 
          "Level 1 data cache refill", 
          "Level 1 data cache access", 
          "Level 1 data TLB refill", 
          "Instruction architecturally executed, Condition code check pass, load", 
          "Instruction architecturally executed, Condition code check pass, store",
          "Instruction architecturally executed, Condition code check pass, exception return",
          "Instruction architecturally executed, Condition code check pass, Software change of the PC", 
          "Branch Instruction architecturally executed, immediate",
          "Instruction architecturally executed, Condition code check pass, unaligned load or store",
          "Branch instruction Speculatively executed, mispredicted or not predicted",
          "Cycle",
          "Predictable branch instruction Speculatively executed",
          "Level 2 data cache refill",
          "Level 2 data cache access, read",
          "Bus access, read",
          "Bus access, write",
          "Bus access, Normal, Cacheable, Shareable",
          "Bus access, peripheral",
          "Data memory access, read",
          "Data memory access, write",
          "Unaligned access, read",
          "Exclusive operation Speculatively executed, Load-Exclusive",
          "Exclusive operation Speculatively executed, Store-Exclusive pass",
          "Exclusive operation Speculatively executed, Store-Exclusive fail",
          "Operation speculatively executed, load",
          "Operation speculatively executed, store",
          "Operation speculatively executed, load or store",
          "Operation speculatively executed, integer data processing",
          "Operation speculatively executed, Software change of the PC",
          "Operation speculatively executed, Cryptographic instruction",
          "Branch Speculatively executed, immediate branch",
          "Exception taken, other synchronous",
          "Exception taken, Instruction Abort",
          "85", # missing 85
          "Exception taken, Hypervisor Call",
          "Exception taken, Instruction Abort not Taken locally",
          "Exception taken, Data Abort or SError not Taken locally",
          "Exception taken, IRQ not Taken locally",
          "Release consistency operation Speculatively executed, Load-Acquire",
          "Release consistency operation Speculatively executed, Store-Release",
          "92"] #missing 92

if __name__ == '__main__':
    
    '''
    Loading and filtering dataset
    '''
    D, L = pre.load("data/" + bench + "/Train.csv")
    D = D.transpose()
    D, L = pre.filter_similar_proportion(D, L)
    D = D.transpose()
    D, L = pre.shuffle_dataset(D,L)
   
    DTest, LTest = pre.load("data/" + bench + "/Test.csv")
    DTest = DTest.transpose()
    DTest, LTest = pre.filter_similar_proportion(DTest, LTest)
    DTest = DTest.transpose()
    DTest, LTest = pre.shuffle_dataset(DTest, LTest)
    
    
    '''
    Preprocess dataset
    '''
    D, DTest = pre.Z_normalize(D, DTest)
    DG = pre.gaussianize(D)
    DGTest = pre.gaussianize(DTest)
    
    
    '''
    DataSet analysis
    '''
    corrs = pre.compute_corr(D, L)
    
    print("Z-norm corrs")
    for el in sorted(corrs, key=lambda x: x[1][0]):
        print(el)
        print(events[el[0]])

    
    corrs_Gauss = pre.compute_corr(DG, L)
    print("Gaussinized corrs")
    for el in sorted(corrs_Gauss, key=lambda x: x[1][0]):
        print(el)
        print(events[el[0]])
  
    #preprocecing_plot(D, L, DG)
    
    
    D = D.transpose()
    DTest = DTest.transpose()
    DG = DG.transpose()
    DGTest = DGTest.transpose()
    
    TOT = numpy.vstack((D.transpose(), L))
    DP, P = pre.PCA_reduce(D.transpose(), 2)
    #pre.plot_scatter(DP, L, "norm")
    TOT_G = numpy.vstack((DG.transpose(), L))
    DP_G, P_G = pre.PCA_reduce(DG.transpose(), 2)
    #pre.plot_scatter(DP_G, L, "gauss")
   
    
    '''
    Filtering column
    '''
    column_to_remove = []

    if bench == "dijkstra":
        column_to_remove = []
    elif bench == "qsort":
        column_to_remove = [  7, 9,  12, 24, 39, 40]
    elif bench == "sha":
        column_to_remove = [7, 9, 12, 24]
    DG_bk = DG
    D_bk = D
    DTest_bk = DTest
    DGTest_bk = DGTest
    for i in range(42):
        print(i)
        DG = DG_bk[:, [i]]
        D = D_bk[:, [i]]     
        #DG = DG[:, [13, 14, 21, 25, 26]] #sha
        #DG = DG[:, [2, 4, 5, 8, 13, 14, 21, 25, 26]] #sha
        #DG = DG[:, [2, 4, 11, 16, 21, 25, 26, 27, 35, 36, 37]] #qsort
        #DG = DG[:, [2, 4, 11, 16, 21, 25, 26, 27, 35, 36, 37]] #dijkstra
        #D = numpy.delete(D, column_to_remove, axis = 1) 
        #DG = numpy.delete(DG, column_to_remove, axis=1)
        DGTest = DGTest_bk[:, [i]] 
        DTest = DTest_bk[:, [i]]     
        #DGTest = DGTest[:, [2, 4, 5, 8, 13, 14, 21, 25, 26]] #sha
        #DGTest = DGTest[:, [2, 4, 11, 16, 21, 25, 26, 27, 35, 36, 37]] #qsort
        #DGTest = DGTest[:, [2, 4, 11, 16, 21, 25, 26, 27, 35, 36, 37]] #dijkstra
        #DTest = numpy.delete(DTest, column_to_remove, axis=1)
        #DGTest = numpy.delete(DGTest, column_to_remove, axis=1)

        if i not in [13, 22, 23, 29, 30, 39, 40]:
            '''
            Gaussian Classifier
            '''
            print("balanced DS")
            gaussian_clf = GaussianNB()
            gaussian_clf.fit(D, L)
            
            L_pred = gaussian_clf.predict(DTest)
            
            accuracy = accuracy_score(L_pred, LTest)
            print(f"Gaussian Classifier z-norm data - Accuracy: {accuracy: .2f}")
            print(f"Recall-Precision {recall_precision(LTest,L_pred)}")
            
            gaussian_clf_G = GaussianNB()
            gaussian_clf_G.fit(DG, L)
            
            L_pred_G = gaussian_clf_G.predict(DGTest)
            
            accuracy_G = accuracy_score(L_pred_G, LTest)
            print(f"Gaussian Classifier Gaussianized data - Accuracy: {accuracy_G: .2f}")
            print(f"Recall-Precision {recall_precision(LTest,L_pred_G)}")


    '''
    D, L = pre.load("data/" + bench + "/Train.csv")
    D, L = pre.shuffle_dataset(D,L)
    DTest, LTest = pre.load("data/" + bench + "/Test.csv")
    DTest, LTest = pre.shuffle_dataset(DTest, LTest)
    print(DTest.shape)
    D, DTest = pre.Z_normalize(D, DTest)
    DGTest = pre.gaussianize(DTest)
    
    DGTest = DGTest.transpose()
    DTest = DTest.transpose()
    DTest = numpy.delete(DTest, column_to_remove, axis=1)
    DGTest = numpy.delete(DGTest, column_to_remove, axis=1)
    
    
    print("unbalanced DS") 
    L_pred = gaussian_clf.predict(DTest)
    
    accuracy = accuracy_score(L_pred, LTest)
    print(f"Gaussian Classifier z-norm data - Accuracy: {accuracy: .2f}")
    
    
    L_pred_G = gaussian_clf_G.predict(DGTest)
    
    accuracy_G = accuracy_score(L_pred_G, LTest)

    print(f"Gaussian Classifier Gaussianized data - Accuracy: {accuracy_G: .2f}")
    '''