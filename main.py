"""
Created on Tue Dec 27 12:46:20 2019

@author: Ibrahim Aljarah, and Ruba Abu Khurma 
"""

import csv
import numpy
import time
import selector as slctr
from sklearn.model_selection import train_test_split
import pandas as pd
import fitnessFUNs

# Select optimizers
PSO=False
MVO=False
GWO=True
MFO=False
WOA=False
FFA=False
BAT=False




optimizer=[PSO, MVO, GWO, MFO, WOA, FFA, BAT]
#optimizer=[CS]
#datasets=["ionosphere","BreastCancer","iris", "ctu13"]
datasets=["ctu13-3"]

#benchmarkfunc=[Fs1,Fs2,Fs3,Fs4,Fs5,Fs6,Fs7,Fs8,Fs9,Fs10] 
        
# Select number of repetitions for each experiment. 
# To obtain meaningful statistical results, usually 30 independent runs 
# are executed for each algorithm.
NumOfRuns=3

# Select general parameters for all optimizers (population size, number of iterations)
PopulationSize = 20
Iterations= 20

#Export results ?
Export=True


#ExportToFile="YourResultsAreHere.csv"
#Automaticly generated file name by date and time
ExportToFile="experiment"+time.strftime("%Y-%m-%d-%H-%M-%S")+".csv" 

# Check if it works at least once
Flag=False

# CSV Header for for the cinvergence 
CnvgHeader1=[]
CnvgHeader2=[]

rows = []
with open('optimized.csv') as csv_file:
    for row in csv.reader(csv_file):
        row = [int(i) for i in row]
        rows.append(row)

for l in range(0,Iterations):
	CnvgHeader1.append("Iter"+str(l+1))

for l in range(0,Iterations):
	CnvgHeader2.append("Iter"+str(l+1))


for j in range (0, len(datasets)):        # specfiy the number of the datasets
    for i in range (0, len(optimizer)):
    
        if((optimizer[i]==True)): # start experiment if an optimizer and an objective function is selected
            for k in range (0,NumOfRuns):
                #func_details=["costNN",-1,1]
                func_details=fitnessFUNs.getFunctionDetails(0)
                completeData=datasets[j]+".csv"

                if len(rows) == 0:
                    x, optimized_cols=slctr.selector(i,func_details,PopulationSize,Iterations,completeData, []) #automatizar o parametro de optimized cols
                    if(Export==True):
                        with open(ExportToFile, 'a',newline='\n') as out:
                            writer = csv.writer(out,delimiter=',')
                            if (Flag==False): # just one time to write the header of the CSV file
                                writer.writerow([x.optimizer])
                            #     pass
                            #     header= numpy.concatenate([["Optimizer","Dataset","objfname","Experiment","startTime","EndTime","ExecutionTime","trainAcc","testAcc"],CnvgHeader1,CnvgHeader1])
                            #     #header= numpy.concatenate(["Optimizer"])
                            #     writer.writerow(header)
                            #a=numpy.concatenate([[x.optimizer,datasets[j],x.objfname,k+1,x.startTime,x.endTime,x.executionTime,x.trainAcc,x.testAcc],x.convergence1,x.convergence2, optimized_cols])
                            a=numpy.concatenate([optimized_cols])
                            writer.writerow(a)
                        out.close()
                    Flag=True # at least one experiment

                for element in rows:
                    x, optimized_cols=slctr.selector(i,func_details,PopulationSize,Iterations,completeData, element) #automatizar o parametro de optimized cols
                    if(Export==True):
                        with open(ExportToFile, 'a',newline='\n') as out:
                            writer = csv.writer(out,delimiter=',')
                            if (Flag==False): # just one time to write the header of the CSV file
                                writer.writerow([x.optimizer])
                            #     pass
                            #     header= numpy.concatenate([["Optimizer","Dataset","objfname","Experiment","startTime","EndTime","ExecutionTime","trainAcc","testAcc"],CnvgHeader1,CnvgHeader1])
                            #     #header= numpy.concatenate(["Optimizer"])
                            #     writer.writerow(header)
                            #a=numpy.concatenate([[x.optimizer,datasets[j],x.objfname,k+1,x.startTime,x.endTime,x.executionTime,x.trainAcc,x.testAcc],x.convergence1,x.convergence2, optimized_cols])
                            a=numpy.concatenate([optimized_cols])
                            writer.writerow(a)
                        out.close()
                    Flag=True # at least one experiment
                
if (Flag==False): # Faild to run at least one experiment
    print("No Optomizer or Cost function is selected. Check lists of available optimizers and cost functions") 
        
        
#Usar como motivação o aprimoramento de modelos que nem sempre tem escalabilidade linear com relação ao número de features (random forest), 
#como em casos de uso de redes de computadores (botnets)