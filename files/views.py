from django.shortcuts import render, redirect
from files.resources import UploadFileResources
from files.models import UplaodFile
from tablib import Dataset
from django.db.models import Q
from django.core.paginator import Paginator
import numpy as np
import pandas as pd
from collections import Counter


def Index(request):
    drop_dupli = []
    if request.method == 'POST':
        file1 = request.FILES['myfile1']
        try:
            file2 = request.FILES['myfile2']
        except:
            file2 = None

        df1 = pd.read_excel(file1)
        if file2:
            df2 = pd.read_excel(file2)
            df1_counts = pd.DataFrame(df1['phone']).value_counts()
            df2_counts = pd.DataFrame(df2['phone']).value_counts()

            df3 = df1_counts + df2_counts
            df3.to_excel('df3.xlsx')

            # df2_counts.columns = ['phone', 'Count']

            # df_concat = pd.concat([df1, df2_counts], axis=1, sort=False)

            # df_grouped = df_concat.groupby(['phone']).sum()

            # print(df_grouped)
            # df_grouped.to_excel('f2.xlsx')

        else:
            f1 = pd.DataFrame(df1).value_counts()
            f1.to_excel('f1.xlsx')



        # commondf = pd.merge(dropdf1, dropdf2, on=["phone"])
        # commondf1 = pd.merge(df1, df2, on=["name"])
        # commondf2 = pd.merge(df1, df2, on=["email"])
        # commondf3 = pd.merge(df1, df2, on=["address"])
        # commondf4 = pd.merge(df1, df2, on=["adhar"])

        # print(commondf1)
        # print(commondf2)
        # print(commondf3)
        # print(commondf4)

        # drop_dupli = commondf.drop_duplicates()
        # commondf.to_excel('duplicate_phone.xlsx')

        # dups = df1.groupby(df1.columns.tolist()).size().reset_index().rename(columns={0:'count'})

        # drop_dupli1 = commondf1.drop_duplicates()
        # drop_dupli1.to_excel('dupli_phone.xlsx')

        # drop_dupli2 = commondf2.drop_duplicates()
        # drop_dupli2.to_excel('dupli_email.xlsx')

        # drop_dupli3 = commondf3.drop_duplicates()
        # drop_dupli3.to_excel('dupli_address.xlsx')

        # drop_dupli4 = commondf4.drop_duplicates()
        # drop_dupli4.to_excel('dupli_adhar.xlsx')


        # df_all_rows = pd.concat([drop_dupli, drop_dupli1, drop_dupli2, drop_dupli3, drop_dupli4])
        # finaldf = df_all_rows.drop_duplicates()
        # finaldf.to_excel('drop_dupli.xlsx')
        

    context = {'data': drop_dupli}
    return render(request, 'files/index.html', context)


def SearchView(request):
    data = UplaodFile.objects.none()
    arr = []
    name = ""
    phone = ""
    email = ""
    address = ""
    adhar = ""

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        adhar = request.POST.get('adhar')

    print("name: ", name, phone, email, address, adhar)
    if name != None and name != "" and phone != None and phone != "" and email != None and email != "" and adhar != None and adhar != "" and address != None and address != "":
        data = UplaodFile.objects.filter(Q(name=name, phone=phone, email=email, address=address, adhar=adhar))
        arr = np.array(data)

    elif name != None and name != "" and phone != None and phone != "" and email != None and email != "" and adhar != None and adhar != "":
        data = UplaodFile.objects.filter(Q(name=name, phone=phone, email=email, address=address))
        arr = np.array(data)

    elif name != None and name != "" and phone != None and phone != "" and email != None and email != "":
        data = UplaodFile.objects.filter(Q(name=name, phone=phone, email=email))
        arr = np.array(data)

    elif name != None and name != "" and phone != None and phone != "":
        data = UplaodFile.objects.filter(Q(name=name, phone=phone))
        arr = np.array(data)

    elif email != None and email != "" and phone != None and phone != "":
        data = UplaodFile.objects.filter(Q(email=email, phone=phone))
        arr = np.array(data)

    elif name != None and name != "" and address != None and address != "":
        data = UplaodFile.objects.filter(Q(name=name, address=address))
        arr = np.array(data)

    elif name != None and name != "":
        data = UplaodFile.objects.filter(name=name)
        arr = np.array(data)
    
    elif phone != None and phone != "":
        data = UplaodFile.objects.filter(phone=phone)
        arr = np.array(data)

    elif email != None and email != "":
        data = UplaodFile.objects.filter(email=email)
        arr = np.array(data)

    elif address != None and address != "":
        data = UplaodFile.objects.filter(address=address)
        arr = np.array(data)

    elif adhar != None and adhar != "":
        data = UplaodFile.objects.filter(adhar=adhar)
        arr = np.array(data)

    else:
        pass

    context = {'data': data, 'arr': arr}
    return render(request, 'files/search.html', context)


def DeleteRecords(request):
    if request.method == "POST":
        data = request.POST.getlist('id')
        for i in data:
            UplaodFile.objects.get(id=i).delete()
    return redirect('index')