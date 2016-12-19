from django.shortcuts import render
from.forms import SignUpForm,ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import SignUp

# Create your views here.
def home(request):
	title="Subcribe for Newsletter"
	form=SignUpForm(request.POST or None)
	context={
		"template_title":title,
		"form":form
	}
	
	if form.is_valid() and request.POST.get('email'):
		form.save()
		form_email= form.cleaned_data.get('email')
		
		form_full_name= form.cleaned_data.get('full_name')
		subject = "Thanks for Joining"
		from_email = settings.EMAIL_HOST_USER
		some_html = """<link href="https://fonts.googleapis.com/css?family=Itim" rel="stylesheet"><table><tr><td width="600px"  style="background-color: red;padding-left: 30px; padding-right: 30px;padding-bottom: 30px;background-image: url('http://www.psdgraphics.com/wp-content/uploads/2012/04/light-wooden-background.jpg');"><h1 align="center" style="padding-top: 20px;font-family: 'Itim', cursive;font-size: 40px">Pandas International</h1><h2 align="center" style="padding-right: 40px;font-family: 'Trirong', serif;font-size: 30px">Welcome</h2>
<p>Dear """ + form_full_name + """, <br><br><br>Welcome to Pandas International. We are happy to have you as a member of our community. Your email address and interest preferences have been recorded in our database. In the future, you will receive periodic emails specific to your interests.</p>
<p>Privacy is important to us; therefore, we will not sell, rent, or give your name or address to anyone. At any point, you can select the link at the bottom of every email to unsubscribe, or to receive less or more information.</p>
<p>Thanks again for registering. If you have any questions or comments, feel free to contact us.Sincerely,</p><img src="https://cdn.shopify.com/s/files/1/0688/1645/t/11/assets/Panda.jpg?6526894982571469098" width="100%" height="400px" /><p>Pandas International<br><br><span>email: yash199649@gmail.com <br>phone: 8085029528 </span></p></td><td></td></tr></table>"""

		to_email=[from_email,form_email]
		contact_message=''
		send_mail(subject,contact_message,from_email,to_email,html_message=some_html,fail_silently=False,)
		context={
			"template_title":'  Thankyou',

		}
	if request.user.is_authenticated() and request.user.is_staff:
		queryset =  SignUp.objects.all().order_by('-timestamp')
		context={
			"queryset":queryset
		}
	return render(request,"home.html",context)
def contact(request):
	form=ContactForm(request.POST or None)

	context={
		"form":form,
	}
	if form.is_valid():
		form_email= form.cleaned_data.get('email')
		form_message= form.cleaned_data.get('message')
		form_full_name= form.cleaned_data.get('full_name')
		subject = "Site connect Form"
		from_email = settings.EMAIL_HOST_USER
		some_html = """ <h1> hi there   """ + form_full_name + """</h1>"""
		to_email=[from_email,'yash199649@gmail.com']
		contact_message="""
		%s:%s via %s 
		"""%(form_full_name,form_message,form_email)
		send_mail(subject,contact_message,from_email,to_email,html_message=some_html,fail_silently=False,)
	return render(request,"forms.html",context)
def about(request):
	return render(request,"about.html")
