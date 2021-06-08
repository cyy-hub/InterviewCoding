# coding:utf-8

import torch as th
from torch.autograd import Variable
import torch.nn as nn
import pandas as pd

def preNormalize(data):
    xstd=data.std(0)
    #xstd =(xstd > 0.001).float().mul(xstd)+(xstd<=0.001).float()*0.001
    data=(data-data.mean(0))/xstd
    return data

th.manual_seed(1)
data=pd.read_excel('./feature_beijing_.xlsx')
data=data[data['ObjBlood']>0].reset_index(drop=True)
#data=data[data['Player']=='human'].reset_index(drop=True)
data =data[data['ObjType']==2].reset_index(drop=True) #  man:ObjType==1   tank:ObjType==2&A1==1    car:ObjType==2&A1==0
data=data[data['A1']==0].reset_index(drop=True)


x=data.iloc[:,[4,5,6,8,10,17,36]]
y=data.iloc[:,[39,40]]
x=th.from_numpy(x.values).float()

x=preNormalize(x)

y=th.from_numpy(y.values).float()
y=y.view(y.size(0),2)
randidx = th.randperm(len(data))
trainnum=len(data)*2/3
testnum=len(data)-trainnum
trainx=x[randidx[:trainnum],:]
trainy=y[randidx[:trainnum],:]
testx=Variable(x[randidx[trainnum:],:])
testy=Variable(y[randidx[trainnum:],:])

mynet=nn.Sequential(
    nn.Linear(x.size(1),32),
    nn.LeakyReLU(0.1,inplace=True),
    nn.Linear(32,256),
    nn.Tanh(),
    nn.Linear(256, 2),
    nn.Sigmoid(),
    )
print mynet
criterion=nn.BCELoss()
optimizer=th.optim.SGD(mynet.parameters(),lr=0.48,momentum=0.97)

batchsize=128
maxloop=1001
for i in range(maxloop):
    randidx = th.randperm(trainnum)
    inputs=Variable(trainx[randidx[:batchsize],:])
    labels=Variable(trainy[randidx[:batchsize],:])


    optimizer.zero_grad()
    outputs=mynet(inputs)
    loss=criterion(outputs,labels)
    loss.backward()
    optimizer.step()



outputs = mynet(testx)

outputs_move=(outputs[:,0]>0.5).float()
outputs_attack=(outputs[:,1]>0.5).float()
testy_move=(testy[:,0]>0.5).float()
testy_attack=(testy[:,1]>0.5).float()

print 'length of trainy:',len(trainy)
print 'length of testy:',len(testy)

print 'move: '
testy_move_total1=testy_move.sum().data[0] #all outputs are the same?
testy_move_total0=len(testy)-testy_move_total1
testy_move_outputt1=outputs_move.sum().data[0]
testy_move_outputt0=len(outputs_move)-testy_move_outputt1

move_same1=0
move_same0=0
for i in range(len(testy)):
    if ((outputs_move[i].data[0]==1) and (testy_move[i].data[0]==1)):
        move_same1+=1
    if ((outputs_move[i].data[0]==0) and (testy_move[i].data[0]==0)):
        move_same0+=1
print 'move_same0:', move_same0, '    testy total0:', testy_move_total0,'    output total0:',testy_move_outputt0
print 'move_same1:',move_same1,'      testy total1:',testy_move_total1,'    output total1:',testy_move_outputt1
print 'the accuracy of move is 1:',(move_same1/(testy_move>0.5).float().sum().data[0])
print 'the accuracy of move is 0:',(move_same0/(testy_move_total0))
move_total_same=move_same0+move_same1
print 'the accuracy of move :',((move_total_same/float(len(testy))))



print '\n\nattack: '

testy_attack_total1=testy_attack.sum().data[0] #all outputs are the same?
testy_attack_total0=len(testy)-testy_attack_total1
testy_attack_outputt1=outputs_attack.sum().data[0]
testy_attack_outputt0=len(outputs_attack)-testy_attack_outputt1

attack_same1=0
attack_same0=0
for i in range(len(testy)):
    if ((outputs_attack[i].data[0]==1) and (testy_attack[i].data[0]==1)):
        attack_same1+=1
    if ((outputs_attack[i].data[0]==0) and (testy_attack[i].data[0]==0)):
        attack_same0+=1
print 'attack_same0:',attack_same0,'    testy total0:',testy_attack_total0,'    output total0:',testy_attack_outputt0
print 'attack_same1:',attack_same1,'    testy total1:',testy_attack_total1,'    output total1:',testy_attack_outputt1
print 'the accuracy of attack is 1:',(attack_same1/testy_attack_total1)
print 'the accuracy of attack is 0:',(attack_same0/(testy_attack_total0))
print 'the accuracy of attack :',((attack_same0+attack_same1)/float(len(testy)))


mystop=1