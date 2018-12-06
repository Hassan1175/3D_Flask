from flask import Flask
from flask import render_template, request, redirect
import os
import sys
import click

import  pandas as pd



app = Flask(__name__)

global  complete_file_path

#print fkjndskjfdshsfklj;dsfk;lsdhfkd
App_Root = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def profile_main():
    return render_template('index.html')



@app.route("/upload" , methods = ['POST'])
def upload():
    target = os.path.join(App_Root,'Images/')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        filename= file.filename
        destination = "/".join([target,filename])
        file.save(destination)

        complete_file_path = target+filename

        print(complete_file_path)

        print(type(complete_file_path))

    return  render_template("done.html")


@app.route("/table_display")
def show_tables():
    # DF = pd.read_excel(complete_file_path)
    DF = pd.read_excel("Images/file.xlsx")

    DF_to_html_table =  DF.to_html()

    return DF_to_html_table
    # render_template("done.html")
if __name__ == '__main__':

    app.run(debug=True , threaded= True)

