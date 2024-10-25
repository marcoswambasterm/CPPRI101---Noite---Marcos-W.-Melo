from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

def lista_vitimas(request):
    pessoas = Pessoa.objects.all()  # Pega todas as instâncias de Pessoa
    pets = PET.objects.all()        # Pega todas as instâncias de PET
    return render(request, 'vitimas/lista_vitimas.html', {'pessoas': pessoas, 'pets': pets})