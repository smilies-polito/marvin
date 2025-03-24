# -*- coding: utf-8 -*-
"""
@author: Enrico
"""

import numpy
import matplotlib
import matplotlib.pyplot as plt
import scipy.optimize
import preprocessing as pre
import DCF

def mcol(v):
    return v.reshape((v.size, 1))

def vrow(v):
    return v.reshape((1, v.size))

def logreg_obj_wrap(DTR, LTR, l, piT):   # l = lambda
    
    Z = LTR * 2.0 - 1.0
    M = DTR.shape[0]
    def logreg_obj(v): #v packs w b
        w = mcol(v[0:M])
        b = v[-1]
        S0 = numpy.dot(w.T, DTR[:, LTR==0]) + b
        S1 = numpy.dot(w.T, DTR[:, LTR==1]) + b #score for all training set, [w^t*x1 + b, w^t*x2 + b, ...]
        cxe =  piT * numpy.logaddexp(0, -S1).mean() + (1-piT) * numpy.logaddexp(0, S0).mean()   #cross avareage entropy, compute 1/n* sum ( log(e^0 + e^-ZS) )
        return cxe + 0.5*l * numpy.linalg.norm(w)**2 #**2 = norm^2
    return logreg_obj

def kfold(K, D, L, pi, piT, Cfn, Cfp, lamb, pca=42, sc = False):
    
    length_fold = int(D.shape[1]/K)
    nTrain = length_fold*(K-1)
    index = 0
    scores = numpy.array([])
    scoresCal = numpy.array([])
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

        logreg_obj = logreg_obj_wrap(DTrain, LTrain, lamb, piT)    
        _v, _J, _d = scipy.optimize.fmin_l_bfgs_b(logreg_obj,  numpy.zeros(DTrain.shape[0]+1), approx_grad= True)
        _w = _v[0:DTrain.shape[0]]
        _b = _v[-1]
        #STE = numpy.dot(_w.T, DValid) + _b #compute the predicted score
        STE = numpy.dot(_w.T, DValid) + _b - numpy.log(DTrain[:, LTrain==0].shape[1]/DTrain[:, LTrain==1].shape[1])
        scores = numpy.append(scores, STE)
        labels = numpy.append(labels, LValid)
        if sc:
            scoreTrainSet = vrow(numpy.dot(_w.T, DTrain) + _b - numpy.log(DTrain[:, LTrain==0].shape[1]/DTrain[:, LTrain==1].shape[1]))
            logReg_objs = logreg_obj_wrap(scoreTrainSet, LTrain, 0, pi)
            _vs, _Js, _ds = scipy.optimize.fmin_l_bfgs_b(logReg_objs,  numpy.zeros(scoreTrainSet.shape[0]+1), approx_grad= True)
            _ws = _vs[0:scoreTrainSet.shape[0]]
            _bs = _vs[-1]
            computeLLR = _ws*STE + _bs - numpy.log(pi/(1-pi))
            scoresCal = numpy.append(scoresCal, computeLLR)
            
    min_DCF = DCF.compute_min_DCF(scores, labels, pi, Cfn, Cfp)
    if sc:
        print("min: ", min_DCF)
        print("cal: ", DCF.compute_act_DCF(scoresCal, labels, pi, Cfn, Cfp))
        DCF.bayes_error_plot(scores, labels, "logReg")  #not calibrated
        DCF.bayes_error_plot(scoresCal, labels, "logReg_calibrated") #calibrated
    return min_DCF

def test(DTrain, LTrain, DTest, LTest, pi, piT, Cfn, Cfp, lamb, pca=42):
    score =numpy.array([])
    scoreCal = numpy.array([])
   
    if(pca < 42):
        DTrain, P = pre.PCA_reduce(DTrain, pca) 
        DTest = numpy.dot(P.T, DTest)
           
    logreg_obj = logreg_obj_wrap(DTrain, LTrain, lamb, piT)    
    _v, _J, _d = scipy.optimize.fmin_l_bfgs_b(logreg_obj,  numpy.zeros(DTrain.shape[0]+1), approx_grad= True)
    _w = _v[0:DTrain.shape[0]]
    _b = _v[-1]
    score = numpy.dot(_w.T, DTest) + _b - numpy.log(DTrain[:, LTrain==0].shape[1]/DTrain[:, LTrain==1].shape[1])
        
    scoreTrainSet = vrow(numpy.dot(_w.T, DTrain) + _b - numpy.log(DTrain[:, LTrain==0].shape[1]/DTrain[:, LTrain==1].shape[1]))
    logReg_obj = logreg_obj_wrap(scoreTrainSet, LTrain, 0, pi)
    _v, _J, _d = scipy.optimize.fmin_l_bfgs_b(logReg_obj,  numpy.zeros(scoreTrainSet.shape[0]+1), approx_grad= True)
    _w = _v[0:scoreTrainSet.shape[0]]
    _b = _v[-1]
    scoreCal = _w*score + _b - numpy.log(pi/(1-pi))
            
    print("LogReg min DCF: ", DCF.compute_min_DCF(score, LTest, pi, Cfn, Cfp))
    print("LogReg actDCF: ", DCF.compute_act_DCF(scoreCal, LTest, pi, Cfn, Cfp))
     

def plot_lambda(K, D, L, pis, title, pca=42):
    lambs = [0, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1e1, 1e2]
    min_DCF_values_S = []   #pi = 0.1
    min_DCF_values_M = []   #pi = 0.5
    min_DCF_values_L = []   #pi = 0.9
    for lamb in lambs: #lambda values      
        min_DCF_S = kfold(K, D, L, 0.1, 0.5, 1, 1, lamb, pca)      
        min_DCF_values_S.append(min_DCF_S)
        min_DCF_M = kfold(K, D, L, 0.5, 0.5, 1, 1, lamb, pca)      
        min_DCF_values_M.append(min_DCF_M)
        min_DCF_L = kfold(K, D, L, 0.9, 0.5, 1, 1, lamb, pca)      
        min_DCF_values_L.append(min_DCF_L)
    
    plt.figure()
    plt.plot(lambs, min_DCF_values_S, label='prior='+str(0.1))
    plt.plot(lambs, min_DCF_values_M, label='prior='+str(0.5))
    plt.plot(lambs, min_DCF_values_L, label='prior='+str(0.9))
    plt.legend()
    plt.semilogx()
    plt.xlabel("λ")
    plt.ylabel("minDCF")    
    plt.savefig("img/lambda_minDCF_%s_PCA%d.jpg" % (title,pca))
