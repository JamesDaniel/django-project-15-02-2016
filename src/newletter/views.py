from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render


from .forms import ContactForm, SignUpForm
# Create your views here.
def home(request):
	title = 'Welcome'
	# if request.user.is_authenticated():
	# 	title = 'My Title %s' % (request.user)

	#add a form here
	print (request)
	if request.method == 'POST':
		print (request.POST)
	form = SignUpForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		print (instance.timestamp)
	context = {
		'title': title,
		'form': form

	}
	return render(request, "base.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get('email')
		form_message = form.cleaned_data.get('message')
		form_full_name = form.cleaned_data.get
		# print (form.cleaned_data)
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]
		contact_message = '%s: %s via %s'%(form_full_name, form_message, form_email)

		send_mail(subject, 
			contact_message, 
			from_email, 
			to_email, 
			fail_silently=True)
	context = {
		'form': form,
	}
	return render(request, 'forms.html', context)