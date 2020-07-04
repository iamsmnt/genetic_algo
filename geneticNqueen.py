#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 15:24:42 2020

@author: smnt
"""
import numpy as np
import pandas as pd
import random


class EightQueensGA():
    

    mutationRate = 0.01
    totalPopulation = 150
    crossOver = 0.5
    
    def __init__(self,target):
        self.target = target
        
        
    def initializePopulation(self,totalPopulation = 150):
        populationData = []
        fitnessData = []
        
        for outloop in range(totalPopulation):
          randomData = []
          fitnessScore = 0
          for inloop in range(len(self.target)):
            selectedData = np.random.randint(0,8)
            if (selectedData == self.target[inloop]):
              fitnessScore = fitnessScore + 1
            randomData.append(selectedData)
          populationData.append(randomData)
          fitnessData.append(fitnessScore)
        probabilityDist = []
        for outloop in range(totalPopulation):
          probabilityDist.append(fitnessData[outloop]/len(self.target))
        probDataFrame = pd.DataFrame({'QueensPosition':populationData,'FitnessScore':fitnessData,'Probability':probabilityDist})
        probDataFrame = probDataFrame.sort_values(['Probability'],ascending=False)
        probDataFrame = probDataFrame.reset_index(drop=True)
        return fitnessData,populationData,probDataFrame

    def getFitnessScore(self,data):
        # data = ''.join([elem for elem in data])
        fitnessScore = 0
        for inloop in range(len(self.target)):
          if (data == self.target[inloop]):
            fitnessScore = fitnessScore + 1
        return fitnessScore
    
    def mutationAndCrossover(self,populationData,fitnessData,dataframe):
        crossOverPoint = int(EightQueensGA.crossOver*len(self.target))
        generationCount = 1000
        for loop in range(generationCount):
            positions=[]
            positions.append(dataframe[0:1]["QueensPosition"].values[0])
            positions.append(dataframe[1:2]["QueensPosition"].values[0])
            print('Fitness Scores of Parents ',self.getFitnessScore(positions[0]),self.getFitnessScore(positions[1]))
            if (self.getFitnessScore(positions[0])==len(self.target) | self.getFitnessScore(positions[1])==len(self.target)):
                print(positions[0],' ',positions[1])
                break
            child1 = positions[0][0:crossOverPoint]+positions[1][crossOverPoint:]
            child2 = positions[1][0:crossOverPoint]+positions[0][crossOverPoint:]
            child1[random.randint(0,len(self.target)-1)] = np.random.randint(0,8)
            child2[random.randint(0,len(self.target)-1)] = np.random.randint(0,8)
            populationData.append(child1)
            populationData.append(child2)
            fitnessData = []
            totalPopulation = len(populationData)
            for outloop in range(totalPopulation):
              fitnessScore = self.getFitnessScore(dataframe.iloc[outloop,0])
              fitnessData.append(fitnessScore)
            probabilityDist = []
            for outloop in range(totalPopulation):
              probabilityDist.append(fitnessData[outloop]/sum(fitnessData))
            probDataFrame = pd.DataFrame({'QueensPosition':populationData,'FitnessScore':fitnessData,'Probability':probabilityDist})
            probDataFrame = probDataFrame.sort_values(['Probability'],ascending=False)
            probDataFrame = probDataFrame.reset_index(drop=True)
            print('Generation ',loop,' ',' Average Fitness Score ',probDataFrame["FitnessScore"].mean(),' ', child1,' ',self.getFitnessScore(child1),child2,self.getFitnessScore(child2))

   
            

    
 
targets = [[4,1,3,5,7,2,0,6],[2,6,1,7,5,3,0,4],[4,2,0,6,1,7,5,3],
    [3,6,4,2,0,5,7,1],[5,2,6,1,3,7,0,4]]
    

test = EightQueensGA(targets[0])

fitnessdata,populationdata,df = test.initializePopulation(150)
        # data = ''.join([elem for elem in data])
fitnessScore = 0
for inloop in range(len(targets[0])):
  if (populationdata[inloop] == targets[0][inloop]):
    fitnessScore = fitnessScore + 1
    
    
test.getFitnessScore(populationdata[0])

