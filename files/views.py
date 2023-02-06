from django.shortcuts import render
import numpy as np
import pandas as pd
import os
# from sklearn.ensemble import RandomForestClassifier
# import multiprocessing
# import time
# from sklearn.model_selection import train_test_split
import vaex



# Index File
def Index(request):
    drop_dupli = []
    if request.method == 'POST':
        file1 = request.FILES.getlist('myfile1')
        df3 = 0

        for i in file1:
            print("i: ", i)
            ext = os.path.splitext(i.name)[1]
            print(ext)
            if ext == '.xlsx':
                df1 = vaex.from_csv(i,convert=True, chunk_size=5000000)
                df1.to_csv("Hello.csv", index=False)
                type("DF1: ", df1)
                # df1 = pd.read_excel(i, header=None)
                # df1 = pd.DataFrame(df1).value_counts()
                # df3 =  df3 + df1

            elif ext == '.csv':
                df1 = pd.read_csv(i, header=None)
                df1 = pd.DataFrame(df1).value_counts()
                df3 =  df3 + df1

            elif ext == ".txt":
                df1 = pd.read_csv(i, sep=" ", on_bad_lines='skip', header=None)
                df1 = pd.DataFrame(df1).value_counts()
                df3 =  df3 + df1

            else:
                df1 = pd.read_excel(i, header=None)
                df1 = pd.DataFrame(df1).value_counts()
                df3 =  df3 + df1


        # results = []
        # def processData(data,outcome_filter):
        #     print(outcome_filter)
        #     df_filter = data[data['df4']==outcome_filter]
        #     df_filter.drop(['df4'],axis = 1, inplace = True)
        #     data_new=df_filter 
        #     clf=RandomForestClassifier(n_estimators=15000)
        #     X=data_new.drop('y',axis=1)       # Features
        #     y=data_new['y']                   # Labels


        #     # Split the dataset into Training set and Testing set
        #     X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1)
        #     clf.fit(X_train,y_train)
        #     y_out = clf.predict(X_test)
        #     X_test['df4']=outcome_filter
        #     cols = list(X_test.columns)+['Actual']
        #     out = pd.concat([X_test,y_test],axis=1,ignore_index=True)
        #     out.columns = cols
        #     out.reset_index(drop=True,inplace=True)
        #     final_out = pd.concat([out,pd.DataFrame(y_out)], axis = 1, ignore_index=True)
        #     final_out.columns=list(out.columns)+['Prediction']
        #     print(final_out.shape)
        #     return final_out 

        # def collect_results(result):
        #     results.extend(result.values.tolist())

        # multiprocessing.cpu_count()
        # start_time=time.time()

        # pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        # pool.close()
        # pool.join()   

        # print("Dimensions in final test data {}".format(df3.shape))
        # print("--- %s seconds ---" % (time.time()-start_time))  

        # df3.to_excel('df3.xlsx')

        # try:
        #     file2 = request.FILES['myfile2']
        # except:
        #     file2 = None
        
        # try:
        #     file3 = request.FILES['myfile3']
        # except:
        #     file3 = None


        # df1 = pd.read_excel(file1)
        # if file3 and file2 and file1:


        #     df2 = pd.read_excel(file2)
        #     df3 = pd.read_excel(file3)

        #     df1_counts = pd.DataFrame(df1.iloc[:, 0].value_counts())
        #     df2_counts = pd.DataFrame(df2.iloc[:, 0]).value_counts()
        #     df3_counts = pd.DataFrame(df3.iloc[:, 0]).value_counts()

        #     df3 = df1_counts + df2_counts + df3_counts
        #     d4 = df3.dropna()

        #     d4.to_excel('df3.xlsx')

        # elif file1 and file2:
        #     df2 = pd.read_excel(file2)
        #     df1_counts = pd.DataFrame(df1.iloc[:, 0]).value_counts()

        #     df2_counts = pd.DataFrame(df2.iloc[:, 0]).value_counts()

        #     df3 = df1_counts + df2_counts
        #     d4 = df3.dropna()

        #     d4.to_excel('df3.xlsx')

        # else:
        #     f1 = pd.DataFrame(df1).value_counts()
        #     f1.to_excel('df3.xlsx')

        #     print(file1)

    context = {'data': drop_dupli}
    return render(request, 'files/index.html', context)


# def SearchView(request):
#     data = UplaodFile.objects.none()
#     arr = []
#     name = ""
#     phone = ""
#     email = ""
#     address = ""
#     adhar = ""

#     if request.method == "POST":
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         address = request.POST.get('address')
#         adhar = request.POST.get('adhar')

#     print("name: ", name, phone, email, address, adhar)
#     if name != None and name != "" and phone != None and phone != "" and email != None and email != "" and adhar != None and adhar != "" and address != None and address != "":
#         data = UplaodFile.objects.filter(Q(name=name, phone=phone, email=email, address=address, adhar=adhar))
#         arr = np.array(data)

#     elif name != None and name != "" and phone != None and phone != "" and email != None and email != "" and adhar != None and adhar != "":
#         data = UplaodFile.objects.filter(Q(name=name, phone=phone, email=email, address=address))
#         arr = np.array(data)

#     elif name != None and name != "" and phone != None and phone != "" and email != None and email != "":
#         data = UplaodFile.objects.filter(Q(name=name, phone=phone, email=email))
#         arr = np.array(data)

#     elif name != None and name != "" and phone != None and phone != "":
#         data = UplaodFile.objects.filter(Q(name=name, phone=phone))
#         arr = np.array(data)

#     elif email != None and email != "" and phone != None and phone != "":
#         data = UplaodFile.objects.filter(Q(email=email, phone=phone))
#         arr = np.array(data)

#     elif name != None and name != "" and address != None and address != "":
#         data = UplaodFile.objects.filter(Q(name=name, address=address))
#         arr = np.array(data)

#     elif name != None and name != "":
#         data = UplaodFile.objects.filter(name=name)
#         arr = np.array(data)
    
#     elif phone != None and phone != "":
#         data = UplaodFile.objects.filter(phone=phone)
#         arr = np.array(data)

#     elif email != None and email != "":
#         data = UplaodFile.objects.filter(email=email)
#         arr = np.array(data)

#     elif address != None and address != "":
#         data = UplaodFile.objects.filter(address=address)
#         arr = np.array(data)

#     elif adhar != None and adhar != "":
#         data = UplaodFile.objects.filter(adhar=adhar)
#         arr = np.array(data)

#     else:
#         pass

#     context = {'data': data, 'arr': arr}
#     return render(request, 'files/search.html', context)


# def DeleteRecords(request):
#     if request.method == "POST":
#         data = request.POST.getlist('id')
#         for i in data:
#             UplaodFile.objects.get(id=i).delete()
#     return redirect('index')
