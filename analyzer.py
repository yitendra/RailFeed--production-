import pandas as pd
from util import CUR_DIR
from classifier import classify
review = {}
review['food']=[]
review['health']=[]
review['journey']=[]
review['security']=[]
review['clean']=[]
review['digital']=[]
review['others']=[]

data = pd.read_csv('./media/TestData.csv')

