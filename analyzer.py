import pandas as pd
from util import CUR_DIR
import csv
from classifier import classify
review = {}
review['food']=[]
review['health']=[]
review['journey']=[]
review['security']=[]
review['clean']=[]
review['digital']=[]
review['others']=[]


def analyze_csv():
    review = {}
    review['food']=[]
    review['health']=[]
    review['journey']=[]
    review['security']=[]
    review['clean']=[]
    review['digital']=[]
    review['others']=[]
    data = pd.read_csv('./media/TestData.csv')
    cats = []
    for i in range (len(data['complaint'])):
        cat = classify(data['complaint'][i])
        cats.append(cat)
        review[cat].append(data['complaint'][i])

    # Writing Data with Category in a file
    cats_df = pd.DataFrame(cats,columns=["category"])
    data['category'] = cats_df
    data.to_csv('./media/Result.csv', sep=",", index=False)
    return review
# analyze_csv()
