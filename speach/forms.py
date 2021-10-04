from django import forms
from django.core.exceptions import ValidationError
from langdetect import detect


class MainForm(forms.Form):
	free_text_field = forms.CharField(
		label='Your text',
		widget=forms.TextInput(
			attrs={'class': 'form-control', 'style': 'margin: 50px;'}
		)
	)

	def clean_free_text_field(self):
		cleaned_data = super(MainForm, self).clean()
		data = self.cleaned_data.get('free_text_field')
		if detect(data) != 'en':
			print('no eng')
			raise ValidationError(
				('Please use only English.'),
				code='invalid',
			)
		return data
