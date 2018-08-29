import pandas as pd
import numpy as np
import io
import decimal as de
import sys

# import from system
windoww=sys.argv[1]
acttual=sys.argv[2]
predictedd =sys.argv[3]
outtput=sys.argv[4]

# import data
# actual_path=system_path+'/insight_testsuite/tests/my_own_test_1/input/actual.txt'
# predicted_path=system_path+'/insight_testsuite/tests/my_own_test_1/input/predicted.txt'
# system_path= os.getcwd()[:-4]

actual=pd.read_table(acttual, sep='|',header=None)
predicted=pd.read_table(predictedd, sep='|',header=None)

# pick up the right moving time window
# window_path=system_path+'/insight_testsuite/tests/my_own_test_1/input/window.txt'
f = io.open(windoww,'r')
message = f.read()
f.close()
sliding_window=int(message)

# add a header for easier manipulation
actual.columns=['hour','stock_code', 'stock_price']
predicted.columns=['hour','stock_code', 'stock_price']

# construct a moving window of elements to take average
predicted_time=predicted['hour'].tolist()
predicted_time=list(set(predicted_time))
q=len(predicted_time)-sliding_window
begin=[]
end=[]
i=0
while i<=q:
    begin.append(predicted_time[i])
    end.append(predicted_time[i+sliding_window-1])
    i=i+1
begin=np.array(begin).T
end=np.array(end).T
    
# construct a join pandas dataframe
mergedStuff = pd.merge(actual, predicted, on=['hour','stock_code'], how='outer')
mergedStuff['diff'] = mergedStuff.apply(lambda x: abs(x['stock_price_x'] - x['stock_price_y']) if not np.isnan(x['stock_price_y']) or np.isnan(x['stock_price_x']) else np.nan, axis=1)
mergedStuff.sort_values(by=['hour'])

# extract the difference and the time

desired=mergedStuff[['hour','diff']]
desire=desired.dropna(subset=['diff'])
desire.sort_values(by=['hour'])

# extract the sum of differences in each hour
L=[]
for time in predicted_time:
    net=desire.loc[desired['hour']==time]['diff'].sum()
    weight=desire[desire['hour']==time].shape[0]
    L.append([net,weight])

# extract the moving averages

output=[]
i=0
while i<=q:
    diff=0
    temp=L[i:i+sliding_window]
    weight=0
    for item in temp:
        diff=diff+item[0]
        weight=weight+item[1]
    a=de.Decimal(diff)
    if weight!=0:
        c=a/de.Decimal(weight)
        d=c.quantize(de.Decimal('.00'))
        output.append(d)
    else:
        output.append('NA')
    i=i+1
output=np.array(output)
    
# create the output dataframe
df_begin=pd.DataFrame(begin)
df_end=pd.DataFrame(end)
value=pd.DataFrame(output.T)
frames=[df_begin, df_end,value]
result=pd.concat(frames,axis=1)


# write the output_file
# output_path=system_path+'/output/comparison.txt'
result.to_csv(outtput, header=None, sep="|", index=False)