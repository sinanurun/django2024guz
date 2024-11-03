from django.forms import ModelForm, TextInput, Textarea, EmailInput

from home.models import ContactFormMessage


class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        # versiyon bir form hali
        # widgets = {
        #     'name': TextInput(attrs={'class': 'input', 'placeholder': 'Enter your name'}),
        #     'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Enter Email'}),
        #     'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Enter Subject'}),
        #     'message': Textarea(attrs={'class': 'input', 'placeholder': 'Message', 'rows':'5'})
        # }

        # versiyon 2 css düzenlenmiş hali
        widgets = {
            'name': TextInput(
                attrs={'type': "text", 'class': "form-control", 'id': "name", 'placeholder': "Your Name",
                       'required': "required",
                       'data-validation-required-message ': "Please enter your name"}),
            'email': TextInput(
                attrs={'type': 'email', 'class': "form-control", 'id': "email", 'placeholder': "Your Email",
                       'required': "required", 'data-validation-required-message': "Please enter your email"}),
            'subject': TextInput(
                attrs={'type': "text", 'class': "form-control", 'id': "subject", 'placeholder': "Subject",
                       'required': "required", 'data-validation-required-message': "Please enter a subject"}),
            'message': Textarea(attrs={'class': "form-control", 'rows': "6", 'id': "message", 'placeholder': "Message",
                                       'required': "required",
                                       'data-validation-required-message': "Please enter your message"}),
        }