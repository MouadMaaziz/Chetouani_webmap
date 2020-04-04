from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Portfolio
from Map.models import About, Pied_de_page, Tete_de_page

# Create your views here.


def portfolio_view(request,*arg,**kwargs):
    portfolios = Portfolio.objects.all().order_by('-pk') #list portfolio objects by primary key
    abouts= About.objects.all()
    contacts= Pied_de_page.objects.all()
    tete=Tete_de_page.objects.all()
    paginator=Paginator(portfolios,12)
    page_request_var= 'page'
    page=request.GET.get(page_request_var)
    try:
        paginated_queryset=paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset=paginator.page(1)
    except EmptyPage:
        paginator= paginator.page(paginator.num_page)
    return render(request,"portfolio.html",{'portfolios': paginated_queryset,'list':portfolios[:5],'about':abouts[0],'page_request_var':page_request_var,'contact':contacts[0],'tete':tete[0]})

def detail_view(request, blog_id):
    portfolios = Portfolio.objects.all().order_by('-pk')
    detailblog= get_object_or_404(Portfolio, pk=blog_id)
    abouts= About.objects.all()
    contacts= Pied_de_page.objects.all()
    tete=Tete_de_page.objects.all()

    if detailblog.pk== 1:                                   #In case the blog pk is 1 the previous blog is not available
        prev= get_object_or_404(Portfolio, pk=blog_id)
    else:
        prev= get_object_or_404(Portfolio, pk=blog_id -1 )

    if detailblog.pk== len(portfolios):                     #In case the blog has the latest pk, the next blog is not available
        next= get_object_or_404(Portfolio, pk=blog_id  )
    else:
        next= get_object_or_404(Portfolio, pk=blog_id +1 )

    return render(request,'detail.html',{'blog':detailblog,'next':next,'prev':prev,'about':abouts[0],'contact':contacts[0],'tete':tete[0]})
