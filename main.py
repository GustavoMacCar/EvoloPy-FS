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
import sys

# Select optimizers

current_dataset = "isot_2010_sample"
commom_path = '/home/gmcma/tg/tg-botnet'

PSO=False
MVO=False
GWO=False
MFO=False
WOA=False
FFA=False
BAT=False


if sys.argv[1] == 'pso':
    PSO=True

if sys.argv[1] == 'mvo':
    MVO=True

if sys.argv[1] == 'gwo':
    GWO=True

if sys.argv[1] == 'mfo':
    MFO=True

if sys.argv[1] == 'woa':
    WOA=True

if sys.argv[1] == 'ffa':
    FFA=True

if sys.argv[1] == 'bat':
    BAT=True




optimizer=[PSO, MVO, GWO, MFO, WOA, FFA, BAT]
#optimizer=[CS]
#datasets=["ionosphere","BreastCancer","iris", "ctu13"]
datasets=[current_dataset]

#benchmarkfunc=[Fs1,Fs2,Fs3,Fs4,Fs5,Fs6,Fs7,Fs8,Fs9,Fs10] 
        
# Select number of repetitions for each experiment. 
# To obtain meaningful statistical results, usually 30 independent runs 
# are executed for each algorithm.
NumOfRuns=1

# Select general parameters for all optimizers (population size, number of iterations)
PopulationSize = 20
Iterations= 20

#Export results ?
Export=True


#ExportToFile="YourResultsAreHere.csv"
#Automaticly generated file name by date and time
ExportToFile="experiment"+time.strftime("%Y-%m-%d-%H-%M-%S")+".csv" 
ExportToProject=f"{commom_path}/features.csv" #Adjust to match features.csv file path in the models project
with open(ExportToProject, 'w+', newline='\n') as out:
    out.truncate()
out.close()

with open('optimized.csv', 'w') as out:
    out.truncate()
out.close()

FirstOptimizer=f"{commom_path}/first_optimizer.csv"
with open(FirstOptimizer, 'w+') as out:
    out.truncate()
out.close()

SecondOptimizer=f"{commom_path}/second_optimizer.csv"
with open(SecondOptimizer, 'w+') as out:
    out.truncate()
out.close()

ThirdOptimizer=f"{commom_path}/third_optimizer.csv"
with open(ThirdOptimizer, 'w+') as out:
    out.truncate()
out.close()

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

                if len(rows) == 0: #optimized vazio
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
                        if len(sys.argv) >= 3:
                            with open('optimized.csv', 'w',newline='\n') as out:
                                writer = csv.writer(out,delimiter=',')
                                #     pass
                                #     header= numpy.concatenate([["Optimizer","Dataset","objfname","Experiment","startTime","EndTime","ExecutionTime","trainAcc","testAcc"],CnvgHeader1,CnvgHeader1])
                                #     #header= numpy.concatenate(["Optimizer"])
                                #     writer.writerow(header)
                                #a=numpy.concatenate([[x.optimizer,datasets[j],x.objfname,k+1,x.startTime,x.endTime,x.executionTime,x.trainAcc,x.testAcc],x.convergence1,x.convergence2, optimized_cols])
                                a=numpy.concatenate([optimized_cols])
                                writer.writerow(a)
                            out.close()

                        with open(ExportToProject, 'a',newline='\n') as out:
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

                        with open(FirstOptimizer, 'a',newline='\n') as out:
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





















if len(sys.argv) >= 3:

    PSO=False
    MVO=False
    GWO=False
    MFO=False
    WOA=False
    FFA=False
    BAT=False
    
    
    if sys.argv[2] == 'pso':
        PSO=True
    
    if sys.argv[2] == 'mvo':
        MVO=True
    
    if sys.argv[2] == 'gwo':
        GWO=True
    
    if sys.argv[2] == 'mfo':
        MFO=True
    
    if sys.argv[2] == 'woa':
        WOA=True
    
    if sys.argv[2] == 'ffa':
        FFA=True
    
    if sys.argv[2] == 'bat':
        BAT=True
    
    
    
    
    optimizer=[PSO, MVO, GWO, MFO, WOA, FFA, BAT]
    #optimizer=[CS]
    #datasets=["ionosphere","BreastCancer","iris", "ctu13"]
    datasets=[current_dataset]
    
    #benchmarkfunc=[Fs1,Fs2,Fs3,Fs4,Fs5,Fs6,Fs7,Fs8,Fs9,Fs10] 
            
    # Select number of repetitions for each experiment. 
    # To obtain meaningful statistical results, usually 30 independent runs 
    # are executed for each algorithm.
    NumOfRuns=1
    
    # Select general parameters for all optimizers (population size, number of iterations)
    PopulationSize = 20
    Iterations= 20
    
    #Export results ?
    Export=True
    
    
    #ExportToFile="YourResultsAreHere.csv"
    #Automaticly generated file name by date and time
    ExportToFile="experiment"+time.strftime("%Y-%m-%d-%H-%M-%S")+".csv" 
    with open(ExportToProject, 'w+', newline='\n') as out:
        out.truncate()
    out.close()

    
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
    
                    for element in rows: #optimized cheio
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
                            with open(ExportToProject, 'a',newline='\n') as out:
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
                            with open(SecondOptimizer, 'w',newline='\n') as out:
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
        print("2 No Optomizer or Cost function is selected. Check lists of available optimizers and cost functions") 
            
        
#Usar como motivação o aprimoramento de modelos que nem sempre tem escalabilidade linear com relação ao número de features (random forest), 
#como em casos de uso de redes de computadores (botnets)

if len(sys.argv) >= 4:

    PSO=False
    MVO=False
    GWO=False
    MFO=False
    WOA=False
    FFA=False
    BAT=False
    
    
    if sys.argv[3] == 'pso':
        PSO=True
    
    if sys.argv[3] == 'mvo':
        MVO=True
    
    if sys.argv[3] == 'gwo':
        GWO=True
    
    if sys.argv[3] == 'mfo':
        MFO=True
    
    if sys.argv[3] == 'woa':
        WOA=True
    
    if sys.argv[3] == 'ffa':
        FFA=True
    
    if sys.argv[3] == 'bat':
        BAT=True
    
    
    
    
    optimizer=[PSO, MVO, GWO, MFO, WOA, FFA, BAT]
    #optimizer=[CS]
    #datasets=["ionosphere","BreastCancer","iris", "ctu13"]
    datasets=[current_dataset]
    
    #benchmarkfunc=[Fs1,Fs2,Fs3,Fs4,Fs5,Fs6,Fs7,Fs8,Fs9,Fs10] 
            
    # Select number of repetitions for each experiment. 
    # To obtain meaningful statistical results, usually 30 independent runs 
    # are executed for each algorithm.
    NumOfRuns=1
    
    # Select general parameters for all optimizers (population size, number of iterations)
    PopulationSize = 20
    Iterations= 20
    
    #Export results ?
    Export=True
    
    
    #ExportToFile="YourResultsAreHere.csv"
    #Automaticly generated file name by date and time
    ExportToFile="experiment"+time.strftime("%Y-%m-%d-%H-%M-%S")+".csv" 
    with open(ExportToProject, 'w+', newline='\n') as out:
        out.truncate()
    out.close()

    
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
    
                    for element in rows: #optimized cheio
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
                            with open(ExportToProject, 'a',newline='\n') as out:
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
                            with open(ThirdOptimizer, 'w',newline='\n') as out:
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
        print("3 No Optomizer or Cost function is selected. Check lists of available optimizers and cost functions") 
            
        
#Usar como motivação o aprimoramento de modelos que nem sempre tem escalabilidade linear com relação ao número de features (random forest), 
#como em casos de uso de redes de computadores (botnets)

