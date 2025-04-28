from django.shortcuts import render
def index(request):
    return render(request,"index.html");
def DonorRegistration(request):
    return render(request,"Donor Registration.html");
def Dashboard(request):
    return render(request,"UserZone/Dashboard.html");
def Feedback(request):
    return render(request,"UserZone/Feedback.html");
def ChangePassword(request):
    return render(request,"UserZone/ChangePassword.html");
def LogOut(request):
    return render(request,"UserZone/LogOut.html");