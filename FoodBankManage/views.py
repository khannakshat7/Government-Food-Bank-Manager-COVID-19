from django.shortcuts import render
from FoodBankManage.models import FoodBankBeneficiary,GramPanchayat,Block,FoodBankInventrycook,FoodBankInventrymid,FoodBankInventryDry

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request,'login.html')

@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))


def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'login.html', {})


@login_required
def foodBankBeneficiary(request):
    if request.method == "POST":
        blocke = request.POST.get('block_name')
        pancha = [g.gramname for g in GramPanchayat.objects.filter(blockna__blockname=blocke)]
        return render(request,'foodbeneficiary.html',{"pancha" : pancha, "blocke" : blocke})

@login_required
def foodBankInventory(request):
    if request.method == "POST":
        blocke = request.POST.get('block_name')
        inventry = request.POST.get('inventry')
        if(inventry == "dryfoodpacket"):
            return foodBankInventorydryfoodpacket(request,blocke=blocke)
        elif(inventry == "middaymeal"):
            return foodBankInventorymiddaymeal(request,blocke=blocke)
        elif(inventry == "cookedmeal"):
            return foodBankInventorycookedmeal(request,blocke=blocke)

@login_required
def Blockname(request):
    blocks = [e.blockname for e in Block.objects.all()]
    return render(request,'block.html',{"blocks" : blocks})

@login_required
def Blockname2(request):
    blocks = [e.blockname for e in Block.objects.all()]
    return render(request,'block2.html',{"blocks" : blocks})

@login_required
def foodBankAdd(request):
    if request.method == "POST":
        blocke = str(request.POST.get('block_name'))
        gram = str(request.POST.get('gram'))
        head = str(request.POST.get('head'))
        members = int(request.POST.get('members'))
        mobile = request.POST.get('mobile')
        NFSA = int(request.POST.get('NFSA'))
        foodpacket = int(request.POST.get('foodpacket'))
        wheat = int(request.POST.get('wheat'))
        rice = int(request.POST.get('rice'))
        
        beneficiary = FoodBankBeneficiary()
        beneficiary.block = blocke
        beneficiary.gram = gram
        beneficiary.head_of_family = head
        beneficiary.total_members_in_family = members
        beneficiary.mobile = mobile
        beneficiary.NFSA = NFSA
        beneficiary.food_packet_Count = foodpacket
        beneficiary.wheat_kg = wheat
        beneficiary.rice_kg = rice
        beneficiary.save()
    return render(request,"submit.html") 

def foodBankInventorydryfoodpacket(request,blocke):
    pancha = [g.gramname for g in GramPanchayat.objects.filter(blockna__blockname=blocke)]
    return render(request,'foodinventrydry.html',{"pancha" : pancha, "blocke" : blocke})

def foodBankInventorymiddaymeal(request,blocke):
    pancha = [g.gramname for g in GramPanchayat.objects.filter(blockna__blockname=blocke)]
    return render(request,'foodinventrymid.html',{"pancha" : pancha, "blocke" : blocke})

def foodBankInventorycookedmeal(request,blocke):
    pancha = [g.gramname for g in GramPanchayat.objects.filter(blockna__blockname=blocke)]
    return render(request,'foodinventrycook.html',{"pancha" : pancha, "blocke" : blocke})


def foodBankInventrydryAdd(request):
    if request.method == 'POST':
        blocke = str(request.POST.get('block_name'))
        gram = str(request.POST.get('gram'))
        available = int(request.POST.get('available'))
        receivedbhama = int(request.POST.get('receivedbhama'))
        receivedgovt = int(request.POST.get('receivedgovt'))
        receivedngo = int(request.POST.get('receivedngo'))
        distributed = int(request.POST.get('distributed'))
        Required = int(request.POST.get('Required'))


        inventrydry = FoodBankInventryDry()
        inventrydry.block = blocke
        inventrydry.gram = gram
        inventrydry.Available = available
        inventrydry.Recieved_Bhamashah = receivedbhama
        inventrydry.Recieved_Government = receivedgovt
        inventrydry.Recieved_NGO = receivedngo
        inventrydry.Distributed = distributed
        inventrydry.Required = Required
        inventrydry.save()
    return render(request,"submit.html")

def foodBankInventrymidAdd(request):
    if request.method == 'POST':
        blocke = str(request.POST.get('block_name'))
        gram = str(request.POST.get('gram'))
        Available_Wheat_Kgs = int(request.POST.get('Available_Wheat_Kgs'))
        Recieved_Wheat_Kgs = int(request.POST.get('Recieved_Wheat_Kgs'))
        Distributed_Wheat_Kgs = int(request.POST.get('Distributed_Wheat_Kgs'))
        Required_Wheat_Kgs = int(request.POST.get('Required_Wheat_Kgs'))
        Available_Rice_Kgs = int(request.POST.get('Available_Rice_Kgs'))
        Recieved_Rice_Kgs = int(request.POST.get('Recieved_Rice_Kgs'))
        Distributed_Rice_Kgs = int(request.POST.get('Distributed_Rice_Kgs'))
        Required_Rice_Kgs = int(request.POST.get('Required_Rice_Kgs'))


        inventrymid = FoodBankInventrymid()
        inventrymid.block = blocke
        inventrymid.gram = gram
        inventrymid.Available_Wheat_Kgs = Available_Wheat_Kgs
        inventrymid.Recieved_Wheat_Kgs = Recieved_Wheat_Kgs
        inventrymid.Distributed_Wheat_Kgs = Distributed_Wheat_Kgs
        inventrymid.Required_Wheat_Kgs = Required_Wheat_Kgs
        inventrymid.Available_Rice_Kgs = Available_Rice_Kgs
        inventrymid.Recieved_Rice_Kgs = Recieved_Rice_Kgs
        inventrymid.Distributed_Rice_Kgs = Distributed_Rice_Kgs
        inventrymid.Required_Rice_Kgs = Required_Rice_Kgs
        inventrymid.save()
    return render(request,"submit.html")

def foodBankInventrycookAdd(request):
    if request.method == 'POST':
        blocke = str(request.POST.get('block_name'))
        gram = str(request.POST.get('gram'))
        Cooked_Meal_Government = int(request.POST.get('Cooked_Meal_Government'))
        Cooked_Meal_Bhamashah = int(request.POST.get('Cooked_Meal_Bhamashah'))
        Cooked_Meal_NGO = int(request.POST.get('Cooked_Meal_NGO'))
        Distributed_Overall_Cooked_Meal = int(request.POST.get('Distributed_Overall_Cooked_Meal'))


        inventrycook = FoodBankInventrycook()
        inventrycook.block = blocke
        inventrycook.gram = gram
        inventrycook.Received_Cooked_Meal_Government = Cooked_Meal_Government
        inventrycook.Received_Cooked_Meal_Bhamashah = Cooked_Meal_Bhamashah
        inventrycook.Recieved_Cooked_Meal_NGO = Cooked_Meal_NGO
        inventrycook.Distributed_Overall_Cooked_Meal = Distributed_Overall_Cooked_Meal
        inventrycook.save()
    return render(request,"submit.html")