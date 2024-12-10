from django.shortcuts import redirect, render,get_object_or_404

# Create your views here.

from produto.models import Produto

def ativos(request):
    ativo = Produto.objects.filter(ativo=True)

    return render(request,'ativos.html',{"ativo":ativo})

def inativos(request):
    inativo = Produto.objects.filter(ativo=False)

    return render(request,'inativos.html',{"inativo":inativo})

def reativos(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        produto.ativo = True  # reativar o produto
        produto.save()  # Salvar a alteração no banco de dados
        return redirect('inativo_list')
    return render(request, 'reativar.html', {'produto': produto})

def produto_inativo(request):

    # Filtrar apenas produtos inativos
    produtos = Produto.objects.filter(ativo=False)
    
    return render(request, 'inativos_list.html', {'produtos': produtos})