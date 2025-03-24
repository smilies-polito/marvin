# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 18:21:10 2022

@author: Enrico
"""

import numpy
import matplotlib.pyplot as plt

def vcol(v):
    return v.reshape((v.size, 1))

def vrow(v):
    return v.reshape((1, v.size))

def assign_labels(scores, pi, Cfn, Cfp, th=None):
    if th is None:
        th = -numpy.log(pi * Cfn) + numpy.log((1 - pi) * Cfp)   #th for optimal bayes decision
    P = scores > th
    return numpy.int32(P)
                    
def compute_conf_matrix_binary(Pred, Labels):
    C = numpy.zeros((2,2))
    C[0,0] = ((Pred == 0) * (Labels == 0)).sum()
    C[0,1] = ((Pred == 0) * (Labels == 1)).sum()
    C[1,0] = ((Pred == 1) * (Labels == 0)).sum()
    C[1,1] = ((Pred == 1) * (Labels == 1)).sum()
    return C

def compute_emp_Bayes_binary(CM, pi, Cfn, Cfp):     #assuming that the  correct predict cost is 0   
    fnr = CM[0,1] / (CM[0,1] + CM[1,1])
    fpr = CM[1,0] / (CM[0,0] + CM[1,0])
    return pi * Cfn * fnr + (1-pi) * Cfp * fpr

def compute_normalized_emp_Bayes(CM, pi, Cfn, Cfp): #DCF normalized
    empBayes = compute_emp_Bayes_binary(CM, pi, Cfn, Cfp)
    return empBayes / min(pi *Cfn, (1-pi)*Cfp)  #devide for the best dummy system

def compute_act_DCF(scores, labels, pi, Cfn, Cfp, th=None):  #score = llr, with th=None we compute theorical optimal bayes decision th
    Pred = assign_labels(scores, pi, Cfn, Cfp, th = th)
    CM = compute_conf_matrix_binary(Pred, labels)
    return compute_normalized_emp_Bayes(CM, pi, Cfn, Cfp)


def compute_min_DCF(scores, labels, pi, Cfn, Cfp):
    thresholds = numpy.array(scores)
    thresholds.sort()
    numpy.concatenate([numpy.array([-numpy.inf]), thresholds, numpy.array([-numpy.inf])])
    dcfList = []
    for t in thresholds:
        dcfList.append(compute_act_DCF(scores, labels, pi, Cfn, Cfp, t))
    return numpy.array(dcfList).min()

def bayes_error(pArray, scores, labels, minCost=False): #pArray is a array of prior value for target class
    y = []
    for p in pArray:
        pi = 1.0 / (1.0 + numpy.exp(-p))
        if minCost:
            y.append(compute_min_DCF(scores, labels, pi, 1, 1))
        else:
            y.append(compute_act_DCF(scores, labels, pi, 1, 1))
    return numpy.array(y)    

def bayes_error_plot(scores, Labels, title=""):
    p = numpy.linspace(-3, 3, 21)
    plt.figure()
    plt.plot(p, bayes_error(p, scores, Labels, minCost=False), label="act DCF", color='r')
    plt.plot(p, bayes_error(p, scores, Labels, minCost=True), label="min DCF", color='b')
    plt.legend()
    plt.xlabel("log(π)/(1-π)")
    plt.ylabel("DCF")
    plt.savefig("img/sc_%s.jpg" % (title))
    