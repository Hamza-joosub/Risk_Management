import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm, trange

def find_Coefficients(tickerList, correlation_Values, stock_Frame, ProcessNumber ):
    #tqdm._instances.clear()
    correlation_Values["Co-Efficient234"] = "ayo"
    
    for ticker in tqdm(tickerList, desc=f"Process number {ProcessNumber}"): 
        #OtherTicker = yf.download(tickers=ticker,start="2023-09-30", end ="2023-10-30", interval ="1d",progress=False)["Close"].pct_change()
        
        Compare= yf.download(tickers=ticker,start="2023-09-05", end ="2023-10-15", interval ="1d",progress=False)["Close"].pct_change().dropna()
        if(len(Compare) != len(stock_Frame)):
            correlation_Values.loc[ticker,"Co-Efficient"] = 2
        #tempList.append(stock_Frame.corr().loc[stock1,ticker])
        else:
            coefficent = ((np.corrcoef(stock_Frame.to_numpy(),Compare.to_numpy()))[0][1])
            correlation_Values.loc[ticker,"Co-Efficient"] = coefficent
    return correlation_Values
    