from django.shortcuts import render
from third.models import Restaurant
from django.core.paginator import Paginator

# Create your views here.
def list(request):
    restaurants = Restaurant.objects.all()
    paginator = Paginator(restaurants, 5)
    
    # request에 페이지 이름이 부여됨 /third/list?page=1
    page = request.GET.get('page')
    # 해당 페이지의 아이템만 필터링해서 가져온다
    items = paginator.get_page(page)
    
    context = {
        'restaurants': items
    }
    return render(request, 'third/list.html', context)