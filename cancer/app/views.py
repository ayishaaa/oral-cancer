from django.shortcuts import render,redirect
from app.models import expert,healthworker,tbl_idgen,tbl_log,patient_dtl
def index(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")    
def adminheader(request):
    return render(request,"adminheader.html")  
def managehealthworker(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.wid
    id = str(id+1)
    wid = "WRK_00" + str(id)
    request.session['wid'] = id
    return render(request,"managehealthworker.html",{'wid':wid})    
def manageexpert(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.eid
    id = str(id+1)
    eid = "EXPERT_00" + str(id)
    request.session['eid'] = id
    return render(request,"manageexpert.html",{'eid':eid})    
def registerworker(request):
    if request.method=='POST':
        data=healthworker()
        data.worker_id=request.POST.get('workerid')
        data.Name=request.POST.get('name')
        data.Email=request.POST.get('email')
        data.Mobile=request.POST.get('mobile')
        data.Address=request.POST.get('address')
        data.District=request.POST.get('dis')
        data.Pincode=request.POST.get('pincode')
        data.Category=request.POST.get('category')
        data.IDcardno=request.POST.get('idcardnumber')
        data.status="not_verified"
        data.save()
        data1 = tbl_idgen.objects.get(id=1)
        data1.wid = request.session['wid']
        data1.save()
        return redirect('/managehealthworker')
def registerexpert(request):
    if request.method=='POST':
        data=expert()
        data.expert_id=request.POST.get('expertid')
        data.Name=request.POST.get('name')
        data.Email=request.POST.get('email')
        data.Mobile=request.POST.get('mobile')
        data.Designation=request.POST.get('designation')
        data.Address=request.POST.get('address')
        data.Qualification=request.POST.get('qualification')
        data.MCIDCIRegno=request.POST.get('mci/dciregno')
        data.MoUsigned=request.POST.get('mousigned')
        data.status="not_verified"
        data.save()
        data1 = tbl_idgen.objects.get(id=1)
        data1.eid = request.session['eid']
        data1.save()
        return redirect('/manageexpert')        

def addworker(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.wid
    id = str(id+1)
    wid = "WRK_00" + str(id)
    request.session['wid'] = id
    return render(request,"addworker.html",{'wid':wid})    
def addexpert(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.eid
    id = str(id+1)
    eid = "EXPERT_00" + str(id)
    request.session['eid'] = id
    return render(request,"addexpert.html",{'eid':eid})    
def addworker1(request):
    if request.method=='POST':
        data=healthworker()
        data.worker_id=request.POST.get('workerid')
        data.Name=request.POST.get('name')
        data.Email=request.POST.get('email')
        data.Mobile=request.POST.get('mobile')
        data.Address=request.POST.get('address')
        data.District=request.POST.get('dis')
        data.Pincode=request.POST.get('pincode')
        data.Category=request.POST.get('category')
        data.IDcardno=request.POST.get('idcardnumber')
        data.status="verified"
        data.save()
        data1 = tbl_idgen.objects.get(id=1)
        data1.wid = request.session['wid']
        data1.save()
        data2=tbl_log()
        data2.Username=request.POST.get('workerid')
        data2.Password=request.POST.get('mobile')
        data2.Category="healthworker"
        data2.save()
        return redirect('/addworker')
def addexpert1(request):
    if request.method=='POST':
        data=expert()
        data.expert_id=request.POST.get('expertid')
        data.Name=request.POST.get('name')
        data.Email=request.POST.get('email')
        data.Mobile=request.POST.get('mobile')
        data.Designation=request.POST.get('designation')
        data.Address=request.POST.get('address')
        data.Qualification=request.POST.get('qualification')
        data.MCIDCIRegno=request.POST.get('mci/dciregno')
        data.MoUsigned=request.POST.get('mousigned')
        data.status="verified"
        data.save()
        data1 = tbl_idgen.objects.get(id=1)
        data1.eid = request.session['eid']
        data1.save()
        data2=tbl_log()
        data2.Username=request.POST.get('expertid')
        data2.Password=request.POST.get('mobile')
        data2.Category="expert"
        data2.save()
        return redirect('/addexpert')        
def removeworker(request):
    data=healthworker.objects.filter(status="verified")
    return render(request,"removeworker.html",{'data':data})    
def verifyworker(request):
    data=healthworker.objects.filter(status="not_verified")
    return render(request,"verifyworker.html",{'data':data})     
def removeexpert(request):
    data=expert.objects.filter(status="verified")
    return render(request,"removeexpert.html",{'data':data})    
def verifyexpert(request):
    data=expert.objects.filter(status="not_verified")
    return render(request,"verifyexpert.html",{'data':data})    
def removeworker1(request,id):
    data=healthworker.objects.get(worker_id=id)
    data.delete()
    return redirect('/removeworker') 
def removeexpert1(request,id):
    data=expert.objects.get(expert_id=id)
    data.delete()
    return redirect('/removeexpert')   
def verifyexpert1(request,id):
    data=expert.objects.get(expert_id=id)
    data.status="verified"
    data.save()
    return redirect('/verifyexpert')          
def verifyexpert2(request,id):
    data=expert.objects.get(expert_id=id)
    data.status="rejected"
    data.save()
    return redirect('/verifyexpert')     
def verifyworker1(request,id):
    data=healthworker.objects.get(worker_id=id)
    data.status="accepted"
    data.save()
    return redirect('/verifyworker')        
def verifyworker2(request,id):
    data=healthworker.objects.get(worker_id=id)
    data.status="rejected"
    data.save()
    return redirect('/verifyworker')
def patientheader(request):
    return render(request,"patientheader.html") 
def patientbasic(request):
    data = tbl_idgen.objects.get(id=1)
    id = data.pid
    id = str(id+1)
    pid = "PT_00" + str(id)
    request.session['pid'] = id
    return render(request,"patientbasic.html",{'pid':pid}) 
def registerpatient(request):
    if request.method=='POST':
        data=patient_dtl()
        data.patient_id=request.POST.get('patientid')
        data.Name=request.POST.get('name')
        data.Age=request.POST.get('age')
        data.Sex=request.POST.get('sex')
        data.Mobile=request.POST.get('mobile')
        data.Place=request.POST.get('place')
        data.District=request.POST.get('dis')
        data.LSGD=request.POST.get('lsgd')
        data.Occupation=request.POST.get('occupation')
        data.Aadharno=request.POST.get('aadharnumber')
        data.save()
        data1 = tbl_idgen.objects.get(id=1)
        data1.pid = request.session['pid']
        data1.save()
        return redirect('/patientbasic')        
# Create your views here.
