from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from .models import Teacher,Subject,Literature,Takyryp,Zert_jumys,Keste,Lit
from .forms import SignupForm
from django.contrib import auth
from django.http import HttpResponse
from django.views.generic import View
from catalog.utils import render_to_pdf
from django.template.loader import get_template
from django.conf import settings
from django.http import HttpResponse
#from django.template.loader import render_to_string
#import weasyprint


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
            'today': datetime.date.today(),
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('syll.html', data)
        return HttpResponse(pdf, content_type='application/pdf')



class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('syll.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('syll.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Syll_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


def index(request):

    Keste.objects.all().delete()
    Lit.objects.all().delete()
    next = request.GET.get('next','/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Правильный пароль и пользователь "активен"
            auth.login(request, user)
            # Перенаправление на "правильную" страницу
            return HttpResponseRedirect("/catalog/zapol/")
        else:
            # Отображение страницы с ошибкой
            return HttpResponseRedirect("/")
    return render(request,"log.html",{'redirect_to':next})



def syllabus(request):
    kestes = Keste.objects.all()
    techers = Teacher.objects.all()
    if request.method == 'POST':
        postrek = request.POST.getlist('postt')
        pre = request.POST.getlist('pre')
        teacher = request.POST.get('teacher')
        lab = request.POST.get('lab')
        prak = request.POST.get('prak')
        print(teacher)
        subject = request.POST.get('subject')
        literature = request.POST.getlist('literature')
        ll = Lit.objects.all()
        postre = request.POST.get('post')
        kkm = request.POST.get('kkm')
        pokab = request.POST.get('pokab')
        #subjectname = Subject.objects.only("credit").filter(subject_name=subject)
        subject_credit = Subject.objects.get(subject_name=subject).credit
        subject_outcome = Subject.objects.get(subject_name=subject).outcome
        subject_description = Subject.objects.get(subject_name=subject).description
        #takyryp_opisanie = Takyryp.objects.get(takyryp_aty=takyryp).opisanie
        teacher_last = Teacher.objects.get(first_name=teacher).last_name
        teacher_email = Teacher.objects.get(first_name=teacher).email
        teacher_phone = Teacher.objects.get(first_name=teacher).phone_numbers
        teacher_account = Teacher.objects.get(first_name=teacher).account
        teacher_otch = Teacher.objects.get(first_name=teacher).patronymic

        prak_teacher_last = Teacher.objects.get(first_name=prak).last_name
        prak_teacher_email = Teacher.objects.get(first_name=prak).email
        prak_teacher_phone = Teacher.objects.get(first_name=prak).phone_numbers
        prak_teacher_account = Teacher.objects.get(first_name=prak).account
        prak_teacher_otch = Teacher.objects.get(first_name=prak).patronymic

        lab_teacher_last = Teacher.objects.get(first_name=lab).last_name
        lab_teacher_email = Teacher.objects.get(first_name=lab).email
        lab_teacher_phone = Teacher.objects.get(first_name=lab).phone_numbers
        lab_teacher_account = Teacher.objects.get(first_name=lab).account
        lab_teacher_otch = Teacher.objects.get(first_name=lab).patronymic


        literature_author = []
        literature_god = []
        literature_izdanie = []
        literature_stranica = []
        literature_nam = []

        if request.method == 'POST':
            for i in range(len(literature)):
                lit = Lit.objects.create()
                lit.literature_name = Literature.objects.get(literature_name=literature[i]).literature_name
                lit.author = Literature.objects.get(literature_name=literature[i]).author
                lit.izdanie = Literature.objects.get(literature_name=literature[i]).izdanie
                lit.stranica = Literature.objects.get(literature_name=literature[i]).stranica
                lit.god = Literature.objects.get(literature_name=literature[i]).god
                lit.typee = Literature.objects.get(literature_name=literature[i]).typee
                lit.save()



        context = {'kestes':kestes,'teacher': teacher, 'subject': subject, 'post': postrek, 'pre': pre,
                   'outcome': subject_outcome,
                   'description': subject_description,'ll': ll,
                   'kkm': kkm, 'pokab': pokab, 'subject_credit': subject_credit, 'teacher_last': teacher_last,
                   'teacher_email': teacher_email, 'teacher_phone': teacher_phone, 'teacher_account': teacher_account,
                   'teacher_otch': teacher_otch, 'prak_teacher_last': prak_teacher_last,
                   'prak_teacher_email': prak_teacher_email, 'prak_teacher_otch':
                       prak_teacher_otch, 'prak': prak, 'lab_teacher_last': lab_teacher_last,
                   'lab_teacher_email': lab_teacher_email, 'lab_teacher_otch': lab_teacher_otch, 'lab': lab}




    return render(
        request,
        'syll.html',

        context
    )


@login_required(login_url='/')
def zapol(request):
    teacherss = Teacher.objects.all()
    user = auth.get_user(request).username
    kestee = Keste.objects.all()
    teachers = Teacher.objects.filter(user__username=user)
    subjects = Subject.objects.filter(user__username=user)
    zertjumyss = Zert_jumys.objects.filter(user__username=user)
    takyryps = Takyryp.objects.filter(user__username=user)
    literaturas = Literature.objects.filter(user__username=user)
    rek = Subject.objects.all()
    if request.method == 'POST' and request.POST.get('sub_name')!=None:
        sub_tak = request.POST.getlist('sub_tak')
        sub_lit = request.POST.getlist('sub_lit')
        sub_name = request.POST.get('sub_name')
        sub_cred= request.POST.get('sub_cred')
        sub_desc = request.POST.get('sub_desk')
        sub_out = request.POST.get('sub_out')
        sub_post = request.POST.get('sub_post')
        subjectt = Subject.objects.create()
        #subjectt.user.create(Username=request.POST.get('uss'))
        subjectt.user = auth.get_user(request)
        subjectt.subject_name = sub_name
        subjectt.credit = sub_cred
        subjectt.description = sub_desc
        subjectt.outcome = sub_out
        subjectt.postrekvisit = sub_post
        for i in sub_tak:
            subjectt.takyryp.create(takyryp_aty=i)
        for j in sub_lit:
            subjectt.literature.create(literature_name=j)
        subjectt.save()
    if request.method == 'POST' and request.POST.get('tak_aty')!=None:
        takyrypp = Takyryp.objects.create()
        tak_zert = request.POST.get('tak_zert')
        takyrypp.user = auth.get_user(request)
        takyrypp.number = request.POST.get('tak_number')
        takyrypp.takyryp_aty = request.POST.get('tak_aty')
        takyrypp.opisanie = request.POST.get('tak_opisanie')
        takyrypp.zert_jumys=Zert_jumys.objects.get(opisanie=tak_zert)
        takyrypp.save()
    if request.method == 'POST' and request.POST.get('ad_name')!=None:
        liter = Literature.objects.create()
        liter.user = auth.get_user(request)
        liter.literature_name = request.POST.get('ad_name')
        liter.author = request.POST.get('ad_author')
        liter.izdanie = request.POST.get('ad_izdanie')
        liter.stranica = request.POST.get('ad_stranica')
        liter.god = request.POST.get('ad_god')
        liter.typee = request.POST.get('ad_tip')
        liter.save()

    if request.method == 'POST' and request.POST.get('zert_number') != None:
        zert = Zert_jumys.objects.create()
        zert.user = auth.get_user(request)
        zert.number = request.POST.get('zert_number')
        zert.opisanie = request.POST.get('zert_opisanie')
        zert.save()

    if request.method == 'POST' and request.POST.get('apta') != None:
        apta = Keste.objects.create()
        op = Takyryp.objects.get(takyryp_aty=request.POST.get('tak')).opisanie
        apta.apta = request.POST.get('apta')
        apta.lekcia = request.POST.get('tak')+'.'+op
        apta.zert = request.POST.get('zert')
        apta.save()


    return  render(request,'forma.html',{'teacherss':teacherss,'rek':rek,'kestee':kestee,'teachers':teachers, 'subjects': subjects, 'zertjumyss': zertjumyss, 'takyryps': takyryps,'literaturas': literaturas,'user':user})

def subform(request):
    user = auth.get_user(request).username
    takyryps = Takyryp.objects.all()
    literaturas = Literature.objects.all()
    return render(request,'subform.html',{'takyryps': takyryps,'literaturas': literaturas,'user':user},)

def takform(request):
    user = auth.get_user(request).username
    zertjumyss = Zert_jumys.objects.all()
    return render(request,'takform.html',{'zertjumyss':zertjumyss,'user':user},)

def adform(request):
    user = auth.get_user(request).username
    liter = Literature.objects.all()
    return render(request, 'adform.html', {'liters': liter,'user':user}, )

def kesteform(request):
    kestes = Keste.objects.all()
    zert = Zert_jumys.objects.filter(user__username=auth.get_user(request).username)
    tak = Takyryp.objects.filter(user__username=auth.get_user(request).username)
    if request.method == 'POST' and request.POST.get('apta') != None:
        apta = Keste.objects.create()
        op = Takyryp.objects.get(takyryp_aty=request.POST.get('tak')).opisanie
        apta.apta = request.POST.get('apta')
        apta.lekcia = request.POST.get('tak')+'.'+op
        apta.zert = request.POST.get('zert')
        apta.save()
    return render(request,'kesteform.html',{'takyryps':tak,'zertjumyss':zert,'kestes':kestes})

def zertform(request):
    user = auth.get_user(request).username
    liter = Literature.objects.all()
    return render(request, 'zertform.html', {'liters': liter,'user':user}, )


def signupform(request):
	#if form is submitted
	if request.method == 'POST':
		#will handle the request later
		form = SignupForm(request.POST)

		#checking the form is valid or not
		if form.is_valid():
			#if valid rendering new view with values
			#the form values contains in cleaned_data dictionary
			return render(request, 'result.html', {
					'name': form.cleaned_data['name'],
					'email': form.cleaned_data['email'],
				})

	else:
		#creating a new form
		form = SignupForm()

	#returning form
	return render(request, 'signupform.html', {'form':form});


