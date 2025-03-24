# -*- coding: utf-8 -*-
"""
@author: Enrico
"""

import numpy
import preprocessing as pre
import DCF
import logisticRegression_classifier as logReg
import scipy.optimize

def vcol(v):
    return v.reshape((v.size, 1))

def vrow(v):
    return v.reshape((1, v.size))

def ML_GAU(D):  #compute mean and covariance matrix, diagonal
    mu = vcol(D.mean(1))
    C = numpy.dot(D-mu, (D-mu).T)/float(D.shape[1])
    return mu, C, C*numpy.eye(C.shape[0])


def logpdf_1sample(x, mu, C):   #x = 1 sample, mu = means vector, C = covariance matrix
    P = numpy.linalg.inv(C) #inverse of C, the precision matrix
    res =  -0.5*x.shape[0] * numpy.log(2*numpy.pi)
    res += -0.5*numpy.linalg.slogdet(C)[1]      #slogdet to compute the determinant
    res += -0.5*numpy.dot((x-mu).T, numpy.dot(P, (x-mu)))
    return res.ravel()  #res is 1x1 matrix with revel() return one dim vector with 1 value

def logpdf_GAU_ND(X, mu, C): #log of density X = samples
    Y = [logpdf_1sample(X[:, i:i+1], mu, C) for i in range(X.shape[1])] #for each samples compute logpdf and put it into Y
    return numpy.array(Y).ravel()

def compute_score (DValid, mu0, mu1, C0, C1):
    logDensities0 = logpdf_GAU_ND(DValid, mu0, C0)
    logDensities1 = logpdf_GAU_ND(DValid, mu1, C1)
    return logDensities1 - logDensities0

def training(DTrain, LTrain, DValid, LValid):
    
    #Traininf part
    D0 = DTrain[:, LTrain==0] #pulsar
    D1 = DTrain[:, LTrain==1] #no pulsar
    mu0, C0, C0_diag = ML_GAU(D0)
    mu1, C1, C1_diag = ML_GAU(D1)
       
    C_tied = (C0*D0.shape[1] + C1*D1.shape[1]) / float(DTrain.shape[1])
    C_tied_diag = (C0_diag*D0.shape[1] + C1_diag*D1.shape[1]) / float(DTrain.shape[1])
    
    return mu0, mu1, C0, C1, C0_diag, C1_diag, C_tied, C_tied_diag



def compute_print_minDCF(scoreMVG, scoreNB, scoreTied, scoreTiedNB, labels, pi, Cfn, Cfp):
    min_DCF_MVG = DCF.compute_min_DCF(scoreMVG, labels, pi, Cfn, Cfp)
    print("MVG min_DCF: ", min_DCF_MVG)
    
    min_DCF_NB = DCF.compute_min_DCF(scoreNB, labels, pi, Cfn, Cfp)
    print("NB min_DCF: ", min_DCF_NB)
    
    min_DCF_Tied = DCF.compute_min_DCF(scoreTied, labels, pi, Cfn, Cfp)
    print("Tied min_DCF: ", min_DCF_Tied)
    
    min_DCF_Tied_NB = DCF.compute_min_DCF(scoreTiedNB, labels, pi, Cfn, Cfp)
    print("Tied NB min_DCF: ", min_DCF_Tied_NB)
    
def kfold(K, D, L, pi, Cfn, Cfp, pca=42, sc=False):
    
    length_fold = int(D.shape[1]/K)
    nTrain = length_fold*(K-1)
    index = 0
    scoreMVG = numpy.array([])
    scoreNB = numpy.array([])
    scoreTied =numpy.array([])
    scoreTiedNB =numpy.array([])
    scoreCal = numpy.array([])
    labels = numpy.array([])
    for x in range(K):
        DTrain = numpy.delete(D, [index, index+length_fold-1], axis = 1)
        DValid = D[:, index:(index+length_fold)]
        if(pca < 42):
            DTrain, P = pre.PCA_reduce(DTrain, pca) 
            DValid = numpy.dot(P.T, DValid)
        LTrain = numpy.delete(L, [index, index+length_fold-1])
        LValid = L[index:(index+length_fold)] 
        index += length_fold
        mu0, mu1, C0, C1, C0_diag, C1_diag, C_tied, C_tied_diag = training(DTrain, LTrain, DValid, LValid)
        scoreMVG = numpy.append(scoreMVG, compute_score(DValid, mu0, mu1, C0, C1))
        scoreNB = numpy.append(scoreNB, compute_score(DValid, mu0, mu1, C0_diag, C1_diag))
        scoreSingleTied = compute_score(DValid, mu0, mu1, C_tied, C_tied)
        
        scoreTied = numpy.append(scoreTied, scoreSingleTied)
        scoreTiedNB = numpy.append(scoreTiedNB, compute_score(DValid, mu0, mu1, C_tied_diag, C_tied_diag))
        labels = numpy.append(labels, LValid)
        if sc:
            scoreTrainSet = vrow(compute_score(DTrain, mu0,mu1, C_tied, C_tied))
            logReg_obj = logReg.logreg_obj_wrap(scoreTrainSet, LTrain, 0, pi)
            _v, _J, _d = scipy.optimize.fmin_l_bfgs_b(logReg_obj,  numpy.zeros(scoreTrainSet.shape[0]+1), approx_grad= True)
            _w = _v[0:scoreTrainSet.shape[0]]
            _b = _v[-1]
            computeLLR = _w*scoreSingleTied + _b - numpy.log(pi/(1-pi))
            scoreCal = numpy.append(scoreCal, computeLLR)
            
            
        
    compute_print_minDCF(scoreMVG, scoreNB, scoreTied, scoreTiedNB, labels, pi, Cfn, Cfp)
    if sc:
        print("Tied actDCF: ", DCF.compute_act_DCF(scoreCal, labels, pi, Cfn, Cfp))
        DCF.bayes_error_plot(scoreTied, labels, "gauss") #not calibrated
        DCF.bayes_error_plot(scoreCal, labels,"gauss_calibrated")   #calibrated
        
        
def test(DTrain, LTrain, DTest, LTest, pi, Cfn, Cfp, pca=42):
    scoreTied =numpy.array([])
    scoreCal = numpy.array([])
   
    if(pca < 42):
        DTrain, P = pre.PCA_reduce(DTrain, pca) 
        DTest = numpy.dot(P.T, DTest)
       
    mu0, mu1, C0, C1, C0_diag, C1_diag, C_tied, C_tied_diag = training(DTrain, LTrain, DTest, LTest)
    scoreTied = compute_score(DTest, mu0, mu1, C_tied, C_tied)
        
    scoreTrainSet = vrow(compute_score(DTrain, mu0,mu1, C_tied, C_tied))
    logReg_obj = logReg.logreg_obj_wrap(scoreTrainSet, LTrain, 0, pi)
    _v, _J, _d = scipy.optimize.fmin_l_bfgs_b(logReg_obj,  numpy.zeros(scoreTrainSet.shape[0]+1), approx_grad= True)
    _w = _v[0:scoreTrainSet.shape[0]]
    _b = _v[-1]
    scoreCal = _w*scoreTied + _b - numpy.log(pi/(1-pi))
            
    print("Tied min DCF: ", DCF.compute_min_DCF(scoreTied, LTest, pi, Cfn, Cfp))
    print("Tied actDCF: ", DCF.compute_act_DCF(scoreCal, LTest, pi, Cfn, Cfp))
        
               
    
def single_split(dimTrain, D, L, pi, Cfn, Cfp, pca=42):        #split dataset in train and test set, dimTrain from 0 to 1 
    nTrain = int(D.shape[1]*dimTrain)
    DTrain = D[:, 0:nTrain]
    DValid = D[:, nTrain:]
    LTrain = L[0:nTrain]
    LValid = L[nTrain:]
    if(pca < 42):
        DTrain, P = pre.PCA_reduce(DTrain, pca) 
        DValid = numpy.dot(P.T, DValid)
    mu0, mu1, C0, C1, C0_diag, C1_diag, C_tied, C_tied_diag = training(DTrain, LTrain, DValid, LValid)
    scoreMVG = compute_score(DValid, mu0, mu1, C0, C1)
    scoreNB = compute_score(DValid, mu0, mu1, C0_diag, C1_diag)
    scoreTied = compute_score(DValid, mu0, mu1, C_tied, C_tied)
    scoreTiedNB = compute_score(DValid, mu0, mu1, C_tied_diag, C_tied_diag)
    compute_print_minDCF(scoreMVG, scoreNB, scoreTied, scoreTiedNB, LValid, pi, Cfn, Cfp)