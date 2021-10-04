from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MainForm
from .models import Text, DetailText
import spacy 

# Create your views here.


def index(request):
	print(1)
	if request.method == 'POST':
		print(2)
		form = MainForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data.get('free_text_field',)
			nlp = spacy.load("en_core_web_sm")
			doc = nlp(str(text))
			field_to_db = Text(full_text=text)
			field_to_db.save()
			for token in doc:
				fields_to_db = DetailText(
					text=str(token.text),
					pos=str(token.pos_),
					tag=str(token.tag_),
					text_id=field_to_db)
				fields_to_db.save()
			return redirect(output_view)
		else:
			msg = form.errors.as_data()['free_text_field'][0]
			print(msg)
			return render(request, 'index.html', {'form': form, 'errors': msg})

	form = MainForm()
	return render(request, 'index.html', {'form': form})


def output_view(request):
	query = Text.objects.all()
	data = []
	for q in query:
		values=[]
		fields = DetailText.objects.all().filter(text_id=q.pk)
		for f in fields: 
			if f.pos == 'PUNCT':
				pass
			else:
				values.append(dict(text=f.text,pos=f.pos,tag=f.tag))

		data.append(dict(pk=q.pk, value=q.full_text, values=values))
	context={'query': data}
	print(context)
	return render(request, 'output.html', context=context)
