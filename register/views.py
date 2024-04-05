from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Applicant 
from .models import Formsubmited, Documents
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def index(request):
    return render(request, "register/index.html")

def contact_view(request):
    return render(request, "register/contact.html")

    
def about_us(request):
    return render(request, "register/about.html")

def formBrief(request):
    forms=Formsubmited.objects.all()
    return render(request, "register/forms.html",{
        "forms":forms
    })

def form_detail(request, pk):
    form = get_object_or_404(Formsubmited, pk=pk)
    return render(request, "register/detail.html", {
        "form": form
    })

def UserLogin(request):
    if request.method =='POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return render(request, "register/register.html")
        else:
            return render (request, "register/login.html",
            {"message" : "invalid credentials"})
    return render(request, "register/login.html")

def UserSignUp(request):
    if request.method == 'POST':
        new_user = Applicant(
            username=request.POST.get("username"),
            email=request.POST.get("email"),
            password=request.POST.get("password"),  # Hash the password using set_password
        )

        # Add any additional fields specific to your custom user model
        new_user.phone_number = request.POST.get("phone_number")

        # Save the user instance
        new_user.save()
        return redirect("register:login")  # Redirect to the login page after registration

    return render(request, "register/signup.html")


def UserLogout(request):
    logout(request)
    return render(request, "register/index.html", {
        "message" : "user has been logged out."
    })




def formSubmit(request):
    if request.method == 'POST':
        # Retrieve data from the form
        eligibility = request.POST.get('eligibility')
        surname = request.POST.get('surname')
        given_name = request.POST.get('given_name')
        other_name = request.POST.get('other_name')
        maiden_name = request.POST.get('maiden_name')
        sex = request.POST.get('sex')
        date_of_birth = request.POST.get('date_of_birth')
        educ_level = request.POST.get('educ_level')
        profession = request.POST.get('profession')
        occupation = request.POST.get('occupation')
        religion= request.POST.get('religion')
        disabilities= request.POST.get('disabilities')
        country= request.POST.get('country')
        county= request.POST.get('county')
        district= request.POST.get('district')
        subCounty= request.POST.get('subCounty')
        parish= request.POST.get('parish')
        village= request.POST.get('village')
        street= request.POST.get('street')
        houseNo= request.POST.get('houseNo')
        yearsLivedAtAddress= request.POST.get('yearsLivedAtAddress')
        previousDistrict= request.POST.get('previousDistrict')
        postalAddress= request.POST.get('postalAddress')
        birthCountry= request.POST.get('birthCountry')
        birthCounty= request.POST.get('birthCounty')
        birthdistrict= request.POST.get(' birthdistrict')
        birthsubCounty= request.POST.get('birthsubCounty')
        birthParish= request.POST.get('birthParish')
        birthCity= request.POST.get('birthCity')
        healthFacility= request.POST.get('healthFacility')
        weightatBirth= request.POST.get('weightatBirth')
        parity= request.POST.get('parity')
        originCountry= request.POST.get('originCountry')
        originCounty= request.POST.get('originCounty')
        originParish= request.POST.get('originParish')
        originDistrict= request.POST.get('originDistrict')
        originSubcounty= request.POST.get('originSubcounty')
        originVillage= request.POST.get('originVillage')
        clan= request.POST.get('clan')
        tribe= request.POST.get('tribe')
        citizenshipType= request.POST.get('citizenshipType')
        citizenshipCertNumber= request.POST.get('citizenshipCertNumber')
        passportNo= request.POST.get('passportNo')
        fileNumber= request.POST.get('fileNumber')
        pollingStation= request.POST.get('pollingStation')
        placeOfResidence= request.POST.get('placeOfResidence')
        placeOfOrgin= request.POST.get('placeOfOrgin')
        pollingStationName= request.POST.get('pollingStationName')
        maritalStatus= request.POST.get('maritalStatus')
        spouseSurname= request.POST.get('spouseSurname')
        spouseGivenName= request.POST.get('spouseGivenName')
        spouseOtherName= request.POST.get('spouseOtherName')
        spousePreviousName= request.POST.get('spousePreviousName')
        NIN= request.POST.get('NIN')
        spouseCitizenshipType= request.POST.get('spouseCitizenshipType')
        placeOfMarriage= request.POST.get('placeOfMarriage')
        DateOfMarriage= request.POST.get('DateOfMarriage')
        TypeOfMarriage= request.POST.get('TypeOfMarriage')
        marriageCertNumber= request.POST.get('marriageCertNumber')
        otherSpouses= request.POST.get('otherSpouses')
        fatherSurname= request.POST.get('fatherSurname')
        fatherOtherName= request.POST.get('fatherOtherName')
        fatherGivenName= request.POST.get('fatherGivenName')
        fatherNIN= request.POST.get('fatherNIN')
        fatherCitizenshipType= request.POST.get('fatherCitizenshipType')
        fatherCitizenshipCertNumber= request.POST.get('fatherCitizenshipCertNumber')
        livingStatus= request.POST.get('livingStatus')
        fatherOccupation= request.POST.get('fatherOccupation')
        fatherCountry= request.POST.get('fatherCountry')
        fatherCounty= request.POST.get('fatherCounty')
        fatherParish= request.POST.get('fatherParish')
        fatherStreet= request.POST.get('fatherStreet')
        fatherDistrict= request.POST.get('fatherDistrict')
        fatherSubCounty= request.POST.get('fatherSubCounty')
        fatherVillage= request.POST.get('fatherVillage')
        fatherHouseNo= request.POST.get('fatherHouseNo')
        motherSurname= request.POST.get('motherSurname')
        motherOtherName= request.POST.get('motherOtherName')
        motherGivenName= request.POST.get('motherGivenName')
        motherNIN= request.POST.get('motherNIN')
        motherCitizenshipType= request.POST.get('motherCitizenshipType')
        motherCitizenshipCertNumber= request.POST.get('motherCitizenshipCertNumber')
        motherLivingStatus= request.POST.get('motherLivingStatus')
        motherOccupation= request.POST.get('motherOccupation')
        motherCountry= request.POST.get('motherCountry')
        motherCounty= request.POST.get('motherCounty')
        motherParish= request.POST.get('motherParish')
        motherStreet= request.POST.get('motherStreet')
        motherDistrict= request.POST.get('motherDistrict')
        motherSubCounty= request.POST.get('motherSubCounty')
        motherVillage= request.POST.get('motherVillage')
        motherHouseNo= request.POST.get('motherHouseNo')
        guardianSurname= request.POST.get('guardianSurname')
        guardianOtherName= request.POST.get('guardianOtherName')
        guardianGivenName= request.POST.get('guardianGivenName')
        guardianPassportNo= request.POST.get('guardianPassportNo')
        guardianNIN= request.POST.get('guardianNIN')
        guardianCitizenshipType= request.POST.get('guardianCitizenshipType')
        guardianCitizenshipCertNumber= request.POST.get('guardianCitizenshipCertNumber')
        guardianLivingStatus= request.POST.get('guardianLivingStatus')
        guardianOccupation= request.POST.get('guardianOccupation')
        guardianCountry= request.POST.get('guardianCountry')
        guardianCounty= request.POST.get('guardianCounty')
        guardianParish= request.POST.get('guardianParish')
        guardianStreet= request.POST.get('guardianStreet')
        guardianDistrict= request.POST.get('guardianDistrict')
        guardianSubCounty= request.POST.get('guardianSubCounty')
        guardianVillage= request.POST.get('guardianVillage')
        guardianHouseNo= request.POST.get('guardianVillage')

        # Create a new Person instance and save it to the database
        person = Formsubmited(
            eligibility=eligibility,
            surname=surname,
            given_name=given_name,
            other_name=other_name,
            maiden_name=maiden_name,
            sex=sex,
            date_of_birth=date_of_birth,
            educ_level=educ_level,
            profession=profession,
            occupation=occupation,
            religion=religion,
            disabilities=disabilities,
            country=country,
            county=county,
            district=district,
            subCounty=subCounty,
            parish=parish,
            village=village,
            street=street,
            houseNo=houseNo,
            yearsLivedAtAddress=yearsLivedAtAddress,
            previousDistrict=previousDistrict,
            postalAddress=postalAddress,
            birthCountry = birthCountry,
            birthCounty=birthCounty,
            birthdistrict=birthdistrict,
            birthsubCounty=birthsubCounty,
            birthParish=birthParish,
            birthCity=birthCity,
            healthFacility=healthFacility,
            weightatBirth=weightatBirth,
            parity=parity,
            originCountry=originCountry,
            originCounty=originCounty,
            originParish=originParish,
            originDistrict=originDistrict,
            originSubcounty=originSubcounty,
            originVillage=originVillage,
            clan=clan,
            tribe=tribe,
            citizenshipType=citizenshipType,
            citizenshipCertNumber=citizenshipCertNumber,
            passportNo= passportNo,
            fileNumber= fileNumber,
            pollingStation= pollingStation,
            placeOfResidence= placeOfResidence,
            placeOfOrgin= placeOfOrgin,
            pollingStationName= pollingStationName,
            maritalStatus= maritalStatus,
            spouseSurname= spouseSurname,
            spouseGivenName= spouseGivenName,
            spouseOtherName= spouseOtherName,
            spousePreviousName= spousePreviousName,
            NIN=  NIN,
            spouseCitizenshipType=  spouseCitizenshipType,
            placeOfMarriage=  placeOfMarriage,
            DateOfMarriage=  DateOfMarriage,
            TypeOfMarriage=  TypeOfMarriage,
            marriageCertNumber=  marriageCertNumber,
            otherSpouses=   otherSpouses,
            fatherSurname=   fatherSurname,
            fatherOtherName=   fatherOtherName,
            fatherGivenName=   fatherGivenName,
            fatherNIN=   fatherNIN,
            fatherCitizenshipType=  fatherCitizenshipType,
            fatherCitizenshipCertNumber=  fatherCitizenshipCertNumber,
            livingStatus=  livingStatus,
            fatherOccupation= fatherOccupation,
            fatherCountry=  fatherCountry,
            fatherCounty = fatherCounty,
            fatherParish = fatherParish,
            fatherStreet = fatherStreet,
            fatherDistrict = fatherDistrict,
            fatherSubCounty = fatherSubCounty,
            fatherVillage = fatherVillage,
            fatherHouseNo = fatherHouseNo,
            motherSurname = motherSurname,
            motherOtherName = motherOtherName,
            motherGivenName =  motherGivenName,
            motherNIN =  motherNIN,
            motherCitizenshipType =  motherCitizenshipType,
            motherCitizenshipCertNumber =  motherCitizenshipCertNumber,
            motherLivingStatus =  motherLivingStatus ,
            motherOccupation =  motherOccupation,
            motherCountry =  motherCountry,
            motherCounty =  motherCounty,
            motherParish =  motherParish,
            motherStreet =   motherStreet,
            motherDistrict =   motherDistrict,
            motherSubCounty =   motherSubCounty,
            motherVillage =   motherVillage,
            motherHouseNo =   motherHouseNo,
            guardianSurname =   guardianSurname,
            guardianOtherName =  guardianOtherName,
            guardianGivenName = guardianGivenName,
            guardianPassportNo = guardianPassportNo,
            guardianNIN = guardianNIN,
            guardianCitizenshipType = guardianCitizenshipType,
            guardianCitizenshipCertNumber = guardianCitizenshipCertNumber,
            guardianLivingStatus = guardianLivingStatus,
            guardianOccupation = guardianOccupation ,
            guardianCountry = guardianCountry,
            guardianCounty = guardianCounty,
            guardianParish = guardianParish,
            guardianStreet = guardianStreet,
            guardianDistrict = guardianDistrict,
            guardianSubCounty = guardianSubCounty,
            guardianVillage = guardianVillage ,
            guardianHouseNo = guardianHouseNo,
        )
        person.save()

        
        #return redirect(request, 'register/index.html',{
        #   "message":"your national id application has been sent please wait for confirmation email to set date for taking id photos"
       # })  
    return render(request, 'register/register.html',{
            "message":"your national id application has been sent please wait for confirmation email to set date for taking biometrics"
        })



def send_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        email = request.POST.get('email', '')
        recipient = request.POST.get('recipient', '')

        from_email = 'ochwodavid0311@gmail.com'

        send_mail(subject, message, from_email, [recipient])
        return HttpResponse('Email sent successfully!')
    else:
        return render(request, 'register/email_form.html')

def document_upload(request):
    if request.method =='POST':
        title = request.POST.get("title")
        local_council = request.POST.get("local_council")
        diso = request.POST.get("diso")
        
        doc = Documents(
            title=title,
            local_council=local_council,
            diso =  diso,
            )

        doc.save()
     
    return render(request, "register/documents.html",  {"message" : "failed to upload documents"})
