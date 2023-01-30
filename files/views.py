from django.shortcuts import render, redirect
from files.resources import UploadFileResources
from files.models import UplaodFile
from tablib import Dataset
from django.db.models import Q
from django.core.paginator import Paginator

def Index(request):
    if request.method == 'POST':
        call_resource = UploadFileResources()
        dataset = Dataset()
        new_call_details = request.FILES['myfile']

        imported_data = dataset.load(new_call_details.read(),format='xlsx')
        for i in imported_data:
            value = UplaodFile(
                i[0],
                i[1],
                i[2],
                i[3],
                i[4],
                i[5],
                # i[6],
            )
            value.save()
            print("Value Saved")
        else:
            print("Some Error")
    context = {}
    return render(request, 'files/index.html', context)


def SearchView(request):
    data = UplaodFile.objects.none()
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

    elif name != None and name != "" and phone != None and phone != "" and email != None and email != "" and adhar != None and adhar != "":
        data = UplaodFile.objects.filter(Q(name=name, phone=phone, email=email, address=address))

    elif name != None and name != "" and phone != None and phone != "" and email != None and email != "":
        data = UplaodFile.objects.filter(Q(name=name, phone=phone, email=email))

    elif name != None and name != "" and phone != None and phone != "":
        data = UplaodFile.objects.filter(Q(name=name, phone=phone))

    elif email != None and email != "" and phone != None and phone != "":
        data = UplaodFile.objects.filter(Q(email=email, phone=phone))

    elif name != None and name != "" and address != None and address != "":
        data = UplaodFile.objects.filter(Q(name=name, address=address))

    elif name != None and name != "":
        data = UplaodFile.objects.filter(name=name)
    
    elif phone != None and phone != "":
        data = UplaodFile.objects.filter(phone=phone)

    elif email != None and email != "":
            data = UplaodFile.objects.filter(email=email)

    elif address != None and address != "":
            data = UplaodFile.objects.filter(address=address)

    elif adhar != None and adhar != "":
            data = UplaodFile.objects.filter(adhar=adhar)

    else:
        pass

    context = {'data': data}
    return render(request, 'files/search.html', context)


def DeleteRecords(request):
    if request.method == "POST":
        data = request.POST.getlist('id')
        for i in data:
            UplaodFile.objects.get(id=i).delete()
    return redirect('index')