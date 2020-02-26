# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 20:42:24 2019

@author: RAVI
"""

from flask import Flask, render_template , url_for, request
import test
from werkzeug.exceptions import HTTPException,NotFound,abort




app = Flask(__name__)





@app.route('/',methods=['GET','POST'])
def home():
    
    return render_template('home.html')

@app.route('/Tmodel',methods=['GET','POST'])
def Tmodel():
    #if request.method == 'POST':
    value1=request.form['selectdf1']
    value2=request.form['selectdf2']
    if value1=='LR':
        if value2=='LR':
            result=test.LR()+test.LR()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='DF':
            result=test.LR()+test.DF()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='KNN':
            result=test.LR()+test.KNN()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='RF':
            result=test.LR()+test.RF()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='NB':
            result=test.LR()+test.NB()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='DT':
            result=test.LR()+test.DT()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
    elif value1=='DF':
        if value1=='LR':
            result=test.DF()+test.LR()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='DF':
            result=test.DF()+test.DF()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='KNN':
            result=test.DF()+test.KNN()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='RF':
            result=test.DF()+test.RF()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='NB':
            result=test.DF()+test.NB()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='DT':
            result=test.DF()+test.DT()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
    if value1=='LR':
        if value1=='LR':
            result=test.LR()+test.LR()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='DF':
            result=test.LR()+test.DF()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='KNN':
            result=test.LR()+test.KNN()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='RF':
            result=test.LR()+test.RF()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='NB':
            result=test.LR()+test.NB()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='DT':
            result=test.DF()+test.DT()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
    elif value1=='KNN':
        if value1=='LR':
            result=test.KNN()+test.LR()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='DF':
            result=test.KNN()+test.DF()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='KNN':
            result=test.KNN()+test.KNN()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='RF':
            result=test.KNN()+test.RF()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='NB':
            result=test.KNN()+test.NB()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='DT':
            result=test.KNN()+test.DT()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
    elif value1=='RF':
        if value1=='LR':
            result=test.RF()+test.LR()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='DF':
            result=test.RF()+test.DF()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='KNN':
            result=test.RF()+test.KNN()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='RF':
            result=test.RF()+test.RF()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='NB':
            result=test.RF()+test.NB()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='DT':
            result=test.RF()+test.DT()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
    elif value1=='NB':
        if value1=='LR':
            result=test.NB()+test.LR()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='DF':
            result=test.NB()+test.DF()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='KNN':
            result=test.NB()+test.KNN()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='RF':
            result=test.NB()+test.RF()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='NB':
            result=test.NB()+test.NB()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='DT':
            result=test.NB()+test.DT()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
    elif value1=='DT':
        if value1=='LR':
            result=test.DT()+test.LR()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='DF':
            result=test.DT()+test.DF()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='KNN':
            result=test.DT()+test.KNN()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='RF':
            result=test.DT()+test.RF()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='NB':
            result=test.DT()+test.NB()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        elif value2=='DT':
            result=test.DT()+test.DT()
            return render_template('Tmodel.html',
                                   accuracy=result[0],
                                   precision=result[1],
                                   recall=result[2],
                                   fl=result[3],
                                   name=result[4],
                                   accuracy1=result[5],
                                   precision1=result[6],
                                   recall1=result[7],
                                   fl1=result[8],
                                   name1=result[9])
        
    
if __name__ == '__main__':
    app.run(debug=True)