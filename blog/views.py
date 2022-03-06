'''from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Blog Home</h1>")
'''
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from blog.models import Users
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login
from blog.models import CreatedUsersForm
from blog.models import RideRequests, Driver
from django.contrib import messages
from django.contrib.auth.models import User

posts = [
  {
    'author': 'Betty',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'Jan 23, 2022'
  },
  {
    'author': 'Josuke',
    'title': 'Blog Post 1',
    'content': 'Hello First post content',
    'date_posted': 'Jan 23, 2022'
  }
]

def home(request):
  context = {'posts': posts}
  return render(request, 'blog/home.html', context)
  '''
  # 执行model操作

  # 添加操作
  ob = Users() # User实例化新的对象(空对象)
  ob.name = "张三"
  ob.age=20
  ob.phone="576"
  print(ob.name)
  print(ob.age)
  ob.save()  #新对象就是添加数据，已存在对象就是修改

  ob1 = Users() # User实例化新的对象(空对象)
  ob1.name = "王五"
  ob1.age=22
  ob1.phone="1234"
  print(ob1.name)
  print(ob1.age)
  ob1.save()  #新对象就是添加数据，已存在对象就是修改
  

  
  #删除操作
  mod = Users.objects #获取users的model对象
  user = mod.get(id = 4) #获取id值为6的数据信息
  print(user.name)
  user.delete()
  

  #修改操作
  ob = Users.objects.get(id=3)
  print(ob.name)
  ob.name = "bt"
  ob.age = 23
  ob.save()
  
  return HttpResponse("首页")  #显示在网页中
  '''
'''
def indexUsers(request):
  try:
    ulist = Users.objects.all()
    context = {"userslist": ulist}
    return render(request, "blog/index.html", context) #加载模板
  except:
    return HttpResponse("没有找到用户信息！")
'''
#加载添加用户信息表单
def addRideRequest(request):
  return render(request, "blog/add.html")


#执行添加用户操作
def insertRideRequest(request):
  #try:
  owner_id = request.user.id
  ob = RideRequests()
  #从表单中获取要添加的信息并封装到ob对象中
  ob.start = request.POST['start']
  ob.dest = request.POST['dest']
  ob.numPass = request.POST['numPass']
  ob.isShare = request.POST['isShare']
  ob.addDate = request.POST['addDate']
  ob.addTime = request.POST['addTime']
  ob.user_id = owner_id
  ob.status = 0
  #print(ob.start, ob.dest, ob.numPass, ob.isShare, ob.addDate, ob.addTime, ob.user_id, ob.driver_id)
  ob.save() #执行保存
  return redirect("rideinfo")
  # except:
  #   context = {"info":"Sorry, ride request is not successful...Please try again."}
  #   return render(request, "blog/info.html", context)
'''
#删除用户信息
def delUsers(request, uid=0):
  try:
    ob = Users.objects.get(id=uid) #获取要删除的数据
    ob.delete() #执行删除操作
    context = {"info":"删除成功！"}
  except:
    context = {"info":"删除失败！"}
  return render(request, "blog/info.html", context)
'''

def signupUsers(request):
  if request.method == 'POST':
    #form = UserCreationForm(request.POST)
    form = CreatedUsersForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Account created successfully!')
      return redirect("loginusers")
  else:
    form = CreatedUsersForm()
    return render(request, "blog/sign_up.html", {'form':form})

def loginUsers(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      login(request, form.get_user())
      return redirect("blog-home")
  else:
    form = AuthenticationForm()
  return render(request, 'blog/login.html', {'form':form})

def rideInfo(request):
  try:
    #owner_id = request.user.id
    owner_id = request.session.get('_auth_user_id')
    print("************", owner_id)
    ulist = RideRequests.objects.filter(user_id=owner_id)
    context = {"userslist": ulist}
    return render(request, "blog/ride_info.html", context) #加载模板
  except:
    return HttpResponse("Can't find ride information...")

def rideViewEdit(request):
  print("===================", request.user.username)
  ride_id = request.POST['uid']
  ob = RideRequests.objects.get(id=ride_id)
  if ob.status==0:
    context = {'ob_ride': ob}
    return render(request, 'blog/ride_open.html', context)
  else:
    print('^^^^^^^^^^', ob.id)
    drive_id = ob.driver_id
    print("**********", drive_id)
    ob_driver = Driver.objects.get(id=drive_id)
    context = {'ob_ride': ob, 'ob_driver': ob_driver}
    return render(request, 'blog/ride_confirmed.html', context)

def rideOpenDel(request):
  try:
    ride_id = request.POST['uid']
    ob = RideRequests.objects.get(id=ride_id)
    ob.delete()
    messages.success(request, 'Cancel successfully.')
  except:
    messages.error(request, 'Cancel not successfully...')
  return render(request, 'blog/ride_open.html')

def rideOpenEdit(request):
  try:
    ride_id = request.POST['uid']
    ob = RideRequests.objects.get(id=ride_id)
    context = {'ride_ob':ob}
    return render(request,"blog/ride_openedit.html",context)
  except:
    return HttpResponse("Cannot find the ride infomation...")

def rideOpenUpdate(request):
  try:
      ride_id = request.POST['uid']
      ob = RideRequests.objects.get(id=ride_id)
      ob.start = request.POST['start']
      ob.dest = request.POST['dest']
      ob.numPass = request.POST['numPass']
      ob.addDate = request.POST['addDate']
      ob.addTime = request.POST['addTime']
      ob.isShare = request.POST['isShare']
      ob.save()
      context = {'ob_ride':ob}
      messages.success(request, "Information updated successfully!")
      return render(request,"blog/ride_open.html",context)
  except:
      ride_id = request.POST['uid']
      ob = RideRequests.objects.get(id=ride_id)
      context = {'ob_ride':ob}
      messages.error(request, "Try it again...")
      return render(request,"blog/ride_openedit.html",context)

def driveRegister(request):
  user_name = request.user.username
  driver_email = request.user.email
  result= Driver.objects.filter(username=user_name)
  if result.exists():
    messages.error(request, "You have already registered!")
    return redirect('drivehome')
  return render(request, "blog/driver_register.html")

def driveUpdate(request):
  try:
    user_name = request.user.username
    driver_email = request.user.email
    ob = Driver()
    ob.driver_name = request.POST['driver_name']
    ob.vehicle_type = request.POST['vehicle_type']
    ob.max_numPass = request.POST['max_numPass']
    ob.license_num = request.POST['license_num']
    ob.username = user_name
    ob.email = driver_email
    ob.save() #执行保存
    messages.success(request, 'Your registration is successful!')
  except:
    messages.error(request, 'Sorry, please try again to register...')
  return redirect('drivehome')

#执行添加用户操作
def driveProfile(request):
  try:
    user_name = request.user.username
    ob = Driver.objects.get(username=user_name)
    context = {'driver_ob': ob}
    return render(request, 'blog/driver_profile.html', context)
  except:
    messages.error(request, "Please register first...")
    return redirect('drivehome')

def driveHome(request):
  return render(request, 'blog/driver_home.html')

def driveEdit(request):
  try:
    user_name = request.user.username
    driver_email = request.user.email
    ob = Driver.objects.get(username=user_name)
    ob.driver_name = request.POST['driver_name']
    ob.vehicle_type = request.POST['vehicle_type']
    ob.max_numPass = request.POST['max_numPass']
    ob.license_num = request.POST['license_num']
    ob.username = user_name
    ob.email = driver_email
    ob.save()
    context = {'driver_ob':ob}
    messages.success(request, "Information updated successfully!")
  except:
    user_name = request.POST['uname']
    ob = Driver.objects.get(username=user_name)
    context = {'driver_ob':ob}
    messages.error(request, "Try it again...")
  return redirect('drivehome')

def driveEditInfo(request):
  try:
    user_name = request.POST['uname']
    ob = Driver.objects.get(username=user_name)
    context = {'driver_ob':ob}
    return render(request,"blog/driver_editinfo.html",context)
  except:
    return HttpResponse("Cannot find the driver infomation...")

def driveSearch(request):
  try:
    user_name = request.user.username
    ob = Driver.objects.get(username=user_name)
    max_numPass = ob.max_numPass
    olist = RideRequests.objects.filter(numPass__lte=max_numPass, status=0)
    context = {"orderslist": olist}
    return render(request, "blog/driver_search.html", context) #加载模板
  except:
    return HttpResponse("Can't find order search information...")

def driveAccept(request):
  try:
    user_name = request.user.username
    drive_id = Driver.objects.get(username=user_name).id
    order_id = request.POST['oid']
    ob = RideRequests.objects.get(id=order_id)
    ob.status = 1
    ob.driver_id = drive_id
    ob.save()
    messages.success(request,"You accept the order successfully!")
  except:
     messages.error(request,"Sorry, You cannot accept this order...")
  return redirect("drivehome")

def driveAcceptRide(request):
  try:
    #owner_id = request.user.id
    user_name = request.user.username
    drive_id = Driver.objects.get(username=user_name).id
    olist = RideRequests.objects.filter(driver_id=drive_id, status=1)
    context = {"orderslist": olist}
    return render(request, "blog/driver_acceptride.html", context) #加载模板
  except:
    return HttpResponse("Can't find accepted ride information...")
  
def driveView(request):
  order_id = request.POST['oid']
  user_name = request.user.username
  drive_id = Driver.objects.get(username=user_name).id
  order_ob = RideRequests.objects.filter(driver_id=drive_id, status=1).first()
  context = {'order_ob': order_ob}
  return render(request, 'blog/driver_view.html', context)

def driveComplete(request):
  user_name = request.user.username
  drive_id = Driver.objects.get(username=user_name).id
  order_id = request.POST['oid']
  ob = RideRequests.objects.get(id=order_id)
  ob.status = 2
  ob.driver_id = drive_id
  ob.save()
  messages.success(request,"The order is completed")
  return redirect('drivehome')

def shareHome(request):
  return render(request, 'blog/sharer_home.html')

def shareSearch(request):
  return render(request, 'blog/sharer_search.html')