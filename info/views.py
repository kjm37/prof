from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime

# Create your views here.

@login_required(login_url="/")
def index(request):
    user=request.user
    data=profilee.objects.get(connection=user.id)
    ser=services.objects.filter(connection=user.id)
    gallary=portfollio.objects.filter(connection=user.id)
    skills=technical_skills.objects.filter(connection=user.id)
    comment=com.objects.filter(connection=user.id)
    context={'data':data,'services':ser,'gallary':gallary,'technical_skills':skills,'comment':comment}
    return render(request,'index.html',context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')

        else:
            print("wrong credential")#logs
            return redirect('login')
    else:
        return render(request,'login.html')



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password1 = request.POST['password2']


        if password == password1:
            if User.objects.filter(username=username).exists():
                print("Username already used")
                return redirect("register")

            elif User.objects.filter(email=email).exists():
                print("Email already used")
                return redirect("register")

            else:
                var = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                var.save()

                var1 = profilee(connection=var, name = first_name+' '+last_name,email=email)
                var1.save()
                return render(request,"login.html")
        else:
            print("password doesnt match")
            return redirect("register")

    else:
        return render(request, "register.html")

@login_required(login_url="/")
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url="/")
def update(request):
    user=request.user
    data=profilee.objects.get(connection=user.id)
    date=str(data.Dob)
    if request.method == 'POST':
        try:
            pro_pic= request.FILES['pic']
        except:
            pro_pic=data.profile_pic
        profesion= request.POST['profesion']
        intro= request.POST['intro']
        description = request.POST['description']
        dob= request.POST['dob']
        city= request.POST['city']
        university= request.POST['university']
        website= request.POST['website']
        age= request.POST['age']
        degree= request.POST['degree']
        phone= request.POST['phone']

        # date=datetime.strptime(dob,'%m/%d/%Y')

        # print(date)

        #print(dob.year)

        var=profilee(id=data.id,connection=user,profile_pic=pro_pic,
            profesion=profesion,intro=intro,description=description,
            Dob=dob,city=city,university=university,website=website,
            age=age,degree=degree,name=data.name,email=data.email,phone=phone)
        var.save()
        data=profilee.objects.get(connection=user.id)
        date=str(data.Dob)
    return render(request,"form.html",{'data':data,'user':user,'date':date})


@login_required(login_url="/")
def send_message(request):
    if request.method == "POST":
        name= request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        message = request.POST['message']
        data=contact(name=name,email=email,phone=mobile,message=message)
        data.save()
        return redirect('index')
    else:
        return redirect('index')

@login_required(login_url="/")
def gallary(request):
    user=request.user
    image=portfollio.objects.filter(connection=user.id)[::-1]
    context={'image':image,'user':user}
    return render(request,"gallary.html",context)

@login_required(login_url="/")
def del_galary(request,id):
    img=portfollio.objects.get(id=id)
    img.delete()
    return redirect('gallary')

@login_required(login_url="/")
def add_image(request):
    user=request.user
    if request.method == 'POST':
        img=request.FILES['pic']
        image=portfollio(connection=user,gallary=img)
        image.save()
        return redirect('gallary')
    else:
        return render(request,'add-gallary.html')

@login_required(login_url="/")
def ser(request):
    user=request.user
    data=services.objects.filter(connection=user.id)
    return render(request,'service.html',{'data':data})

@login_required(login_url="/")
def del_ser(request,id):
    ser=services.objects.get(id=id)
    ser.delete()
    return redirect('ser')

@login_required(login_url="/")
def add_ser(request):
    user=request.user
    if request.method == 'POST':
        title= request.POST['title']
        description= request.POST['description']

        data=services(connection=user,title=title,services_description=description)
        data.save()
        return redirect('ser')
    else:
        return render(request,'add_ser.html')

@login_required(login_url="/")
def add_skill(request):
    user=request.user
    if request.method == 'POST':
        tech_name = request.POST['tech_name']
        progress = request.POST['progress']

        data=technical_skills(connection=user,tech_name=tech_name,progress=progress)
        data.save()
        return redirect('skills')
    else:
        return render(request,'add_skill.html')

@login_required(login_url="/")
def del_skill(request,id):
    data=technical_skills.objects.get(id=id)
    data.delete()
    return redirect('skills')


@login_required(login_url="/")
def skills(request):
    user=request.user
    data=technical_skills.objects.filter(connection=user.id)
    return render(request,'skill.html',{'data':data})

def add_comment(request):
    user=request.user
    if request.method == 'POST':
        name = request.POST['name']
        profession= request.POST['profession']
        message= request.POST['message']

        data=com(connection=user,name=name,profession=profession,message=message)
        data.save()
        return redirect('comment')
    else:
        return render(request,'add_comment.html')

def del_comment(request,id):
    data=comment.objects.get(id=id)
    data.delete()
    return redirect('comment')

def commentx(request):
    user=request.user
    data=com.objects.filter(connection=user.id)
    return render(request,'comment.html',{'data':data})
