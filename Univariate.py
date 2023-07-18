class Univariate():
    def QualQuan (dataset):
        quan=[]
        qual=[]
        for columnsName in dataset.columns:
            if(dataset[columnsName].dtype=='O'):
                #print("qual")
                qual.append(columnsName)
            else:
                #print("quan")
                quan.append(columnsName)
        return qual,quan
    
    def freqTable(columnsName,dataset):
        freqTable=pd.DataFrame(columns=["Unique_Value","Frequency","Relative Frequency","cumsum"])
        freqTable["Unique_Value"]=dataset["ssc_p"].value_counts().index
        freqTable["Frequency"]=dataset["ssc_p"].value_counts().values
        freqTable["Relative Frequency"]=(freqTable["Frequency"]/103)
        freqTable["cumsum"]=freqTable["Relative Frequency"].cumsum()
        return freqTable
    
    def Univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%",
                                        "Q2:50%","Q3:75%","Q4:100%","IQR","1.5rule","lesser","greater","min","max"],
                                         columns=quan)
        for columnsName in quan :
            descriptive[columnsName]["Mean"]=dataset[columnsName].mean()
            descriptive[columnsName]["Median"]=dataset[columnsName].median()
            descriptive[columnsName]["Mode"]=dataset[columnsName].mode()[0]
            descriptive[columnsName]["Q1:25%"]=dataset.describe()[columnsName]["25%"]
            descriptive[columnsName]["Q2:50%"]=dataset.describe()[columnsName]["50%"]
            descriptive[columnsName]["Q3:75%"]=dataset.describe()[columnsName]["75%"]
            descriptive[columnsName]["Q4:100%"]=dataset.describe()[columnsName]["max"]
            descriptive[columnsName]["IQR"]=descriptive[columnsName]["Q3:75%"]-descriptive[columnsName]["Q1:25%"]
            descriptive[columnsName]["1.5rule"]=1.5*descriptive[columnsName]["IQR"]
            descriptive[columnsName]["lesser"]=descriptive[columnsName]["Q1:25%"]-descriptive[columnsName]["1.5rule"]
            descriptive[columnsName]["greater"]=descriptive[columnsName]["Q3:75%"]+descriptive[columnsName]["1.5rule"]
            descriptive[columnsName]["max"]=dataset[columnsName].max()
            descriptive[columnsName]["min"]=dataset[columnsName].min()
        return descriptive
  
    def outlier(dataset,quan):
        for columnsName in quan:
            if descriptive[columnsName]["min"]<descriptive[columnsName]["lesser"]:
                lesser.append(columnsName)
            if descriptive[columnsName]["max"]>descriptive[columnsName]["greater"]:
                greater.append(columnsName)
        return descriptive
    def replace(dataset,quan):
        for columnsName in lesser:
            dataset[column][dataset[column]<descriptive[column]["lesser"]]=descriptive[column]["lesser"]
        for columnsName in greater:
            dataset[column][dataset[column]>descriptive[column]["greater"]]=descriptive[column]["greater"] 
        return descriptive