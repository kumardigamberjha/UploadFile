from django.shortcuts import render
import numpy as np
import pandas as pd
import os
import vaex
import time

def Index(request):
    drop_dupli = []
    if request.method == 'POST':
        file1 = request.FILES.getlist('myfile1')
        try:
            file2 = request.FILES.getlist('myfile2')
        except:
            file2 = None
        
        try:
            file3 = request.FILES.getlist('myfile3')
        except:
            file3 = None

        df3 = 0
        dupli_df = []
        ########################## Reading File  ###########################
        for i in file1:
            ext = os.path.splitext(i.name)[1]
            count = 0
            if ext == '.xlsx':
                start = time.time()
                df1 = pd.read_excel(i, header=None)
                end = time.time()
                print("Excel: ", end - start)
                
            elif ext == '.csv':
                start = time.time()
                df1 = pd.read_csv(i, header=None)
                df1 = pd.DataFrame(df1.iloc[:, 0]).value_counts()

                df3 = df1 + df3
                end = time.time()
                print("CSV: ", end - start)

            elif ext == ".txt":
                start = time.time()
                df1 = pd.read_csv(i, sep=" ", on_bad_lines='skip', header=None)
                df1 = pd.DataFrame(df1.iloc[:,0]).value_counts()

                df3 =  df3 + df1
                end = time.time()
                print("Writing: ", end - start)

            else:
                df1 = pd.read_excel(i, header=None)
                df1 = pd.DataFrame(df1).value_counts()
                df3 =  df3 + df1


        ########################## Reading File 2 ###########################
        for i in file2:
            ext = os.path.splitext(i.name)[1]
            if ext == '.xlsx':
                start = time.time()
                df1 = pd.read_excel(i, header=None)
                end = time.time()
                print("Excel: ", end - start)
                
            elif ext == '.csv':
                start = time.time()
                df1 = pd.read_csv(i, header=None)

                df1 = pd.DataFrame(df1.iloc[:, 0]).value_counts()
                df3 = df1 + df3
                end = time.time()
                print("CSV: ", end - start)

            elif ext == ".txt":
                start = time.time()
                df1 = pd.read_csv(i, sep=" ", on_bad_lines='skip', header=None)
                df1 = pd.DataFrame(df1.iloc[:,0]).value_counts()
                df3 =  df3 + df1
                end = time.time()
                print("Writing: ", end - start)

            else:
                df1 = pd.read_excel(i, header=None)
                df1 = pd.DataFrame(df1).value_counts()
                df3 =  df3 + df1

        ########################## Reading File 3 ###########################
        for i in file3:
            ext = os.path.splitext(i.name)[1]
            if ext == '.xlsx':
                start = time.time()
                df1 = pd.read_excel(i, header=None)
                end = time.time()
                print("Excel: ", end - start)
                
            elif ext == '.csv':
                start = time.time()
                df1 = pd.read_csv(i, header=None)
                df1 = pd.DataFrame(df1.iloc[:, 0]).value_counts()
                df3 = df1 + df3
                end = time.time()
                print("CSV: ", end - start)

            elif ext == ".txt":
                start = time.time()
                df1 = pd.read_csv(i, sep=" ", on_bad_lines='skip', header=None)
                df1 = pd.DataFrame(df1.iloc[:,0]).value_counts()
                df3 =  df3 + df1
                end = time.time()
                print("Txt: ", end - start)

            else:
                df1 = pd.read_excel(i, header=None)
                df1 = pd.DataFrame(df1).value_counts()
                df3 =  df3 + df1


        ########################## Writting Data ###########################
        print("Writing Data: ")
        start = time.time()
        df4 = df3.dropna()
        df4.to_csv('df3.csv')
        end = time.time()
        print("write: ", end - start)


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
