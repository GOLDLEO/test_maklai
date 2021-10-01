from django import forms 

class MainForm(forms.Form):
	free_text_field = forms.CharField(label='Your text', widget=forms.Textarea)