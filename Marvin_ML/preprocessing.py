# -*- coding: utf-8 -*-
"""
@author: Enrico
"""

import numpy
import matplotlib
import matplotlib.pyplot as plt
import pylab
from scipy.stats import norm
from main import *
from scipy.stats.stats import pearsonr

def mcol(v):
    return v.reshape((v.size, 1))

def load(fname):
    DList = []
    labelsList = []
    
    
    with open(fname) as f:
        for line in f:
            try:
                #print(line)
                attrs = line.split(',')[1:43]
                attrs = numpy.array([float(i) for i in attrs])
                attrs = mcol(attrs)      #trasformation in column vector
                DList.append(attrs)
                labelsList.append(line.split(',')[0])
            except:
                pass
            
    return numpy.hstack(DList), numpy.array(labelsList, dtype=numpy.int32)      #hstack impilla vettori colonna per fare matrice, numpy.array ritorna un semplice array d'interi

def compute_corr(x,y):
   
    y_array = y.reshape(-1)
    correlations = list()
    i = 0
    for col in x:
        
        correlation = pearsonr(y_array, col)
        correlations.append((i,correlation))
        i = i +1

    return correlations 

def plot_hist(D,L,title):
    D0 = D[:, L==0] #sub matrix for all row but only the collon with right label
    D1 = D[:, L==1]
    
    for dIdx in range(42):
        plt.figure()
        plt.xlabel(events[dIdx])
        plt.hist(D0[dIdx, :], bins = 50, density = True, alpha = 0.4, label = 'Benign', facecolor='blue', edgecolor='darkred')
        plt.hist(D1[dIdx, :], bins = 50, density = True, alpha = 0.4, label = 'SDC', facecolor='red', edgecolor='darkblue')
        
        
        plt.legend()
        plt.tight_layout() # Use with non-default font size to keep axis label inside the figure
        plt.savefig('img/' + bench + '/hist_%s_%d.jpg' % (title,dIdx))  #for saving the hist
    plt.show()

def center(D):          
    mu = D.mean(1) #with 0 we compute the mean over rows, while with 1 the mean is over columns
    #print(mu.reshape((D.shape[0], 1)))
    DC = D - mu.reshape((D.shape[0], 1))  #reshape per passare da vettore riga a vettore colonna
    return DC

def Z_normalize(D, DTest):
    
    mu = numpy.mean(D, axis=1)
    std_dev = numpy.std(D, axis=1)
    # Handle zero standard deviations by replacing them with a small non-zero value
    std_dev = numpy.where(std_dev == 0, 1e-6, std_dev)
    #print(mu)
    #print(std_dev)
    DZ = D
    DZ = DZ - mcol(mu)
    DZ = DZ / mcol(std_dev)
    DTest = (DTest - mcol(mu)) / mcol(std_dev)
    return DZ, DTest

def gaussianize(D):
    rank = numpy.zeros(D.shape)
    for i in range(D.shape[0]):
        for j in range(D.shape[1]):
           rank[i][j] = (D[i] < D[i][j]).sum()
    rank = (rank + 1) / (D.shape[1] + 2)
    
    return norm.ppf(rank)

def PCA_reduce(D, m):
    
    mu = mcol(D.mean(1))    #mean of the columns, parameter is the axis
    # C = 0                   #Covariance matrix
    # for i in range(D.shape[1]):
    #     xc = D[:, i:i+1]- mu
    #     xcxc = numpy.dot(xc, xc.T)
    #     C = C + xcxc
    # C = C/D.shape[1]    # shape of 1 return the dimension of axis 1
    
    DC = D - mu
    C = numpy.dot(DC, DC.T)/D.shape[1]   #faster way
    #print(mu)
    #print(C)
    
    #extract of the pricipal component
    s, U = numpy.linalg.eigh(C) # .eigh for symmetric matrix .eig for the other
    #columns of U are eigenvectors while s are eigenvalues sorted from the smallest to largest
    P = U[:, ::-1][:, 0:m] #the first reverse the colomns the second take m colomns
    #print(P)
    
    DP = numpy.dot(P.T, D)
    return DP, P


def plot_pearson_correlation_heatmap(D, title, color):
    
    plt.figure()
    pearson_correlations = numpy.corrcoef(D)
    #plt.title(title)
    plt.imshow(pearson_correlations, cmap=color, interpolation='nearest')
    plt.savefig("img/" + bench + "/correlation_%s.jpg" % title)
    
 
def shuffle_dataset(D, L):
    numpy.random.seed(5000)
    idx = numpy.random.permutation(D.shape[1])
    return D[:, idx], L[idx]
    
def filter_similar_proportion(X, y):
    # Convert y to a 1-dimensional array and count the occurrences of '0' and '1'
    y_flat = y.flatten()
    count_0 = numpy.count_nonzero(y_flat == 0)
    count_1 = numpy.count_nonzero(y_flat == 1)
    print(count_0)
    print(count_1)
    # Calculate the proportion of '0' and '1' values in y
    proportion_0 = count_0 / len(y_flat)
    proportion_1 = count_1 / len(y_flat)

    # Determine the minimum count to maintain similar proportions
    min_count = min(count_0, count_1)

    # Filter rows for '0' and '1' separately to keep the desired proportion
    indices_0 = numpy.where(y_flat == 0)[0][:min_count]
    indices_1 = numpy.where(y_flat == 1)[0][:min_count]

    # Select the filtered rows from X and y
    X_filtered = X[numpy.concatenate((indices_0, indices_1))]
    y_filtered = y_flat[numpy.concatenate((indices_0, indices_1))]

    # Reshape y_filtered to be a 2-dimensional array (column vector)
    #y_filtered = y_filtered.reshape(-1, 1)

    # Convert X and y back to PyTorch tensors
    #X_filtered = torch.tensor(X_filtered, dtype=torch.float32)
    #y_filtered = torch.tensor(y_filtered, dtype=torch.float32)

    return X_filtered, y_filtered  

def plot_scatter(D,L, title):
    D0 = D[:, L==0] #sub matrix for all row but only the collon with right label
    D1 = D[:, L==1]
       
    plt.figure()
    plt.xlabel("com1")
    plt.ylabel("com2")
    plt.scatter(D0[0, :], D0[1, :], label = 'Bening', facecolor="blue")
    plt.scatter(D1[0, :], D1[1, :], label = 'SDC', facecolor="red")

    plt.legend()
    plt.tight_layout() # Use with non-default font size to keep axis label inside the figure
    plt.savefig('img/' + bench + '/scatter_%d_%d_%s.png' % (0, 1, title))
    plt.show()