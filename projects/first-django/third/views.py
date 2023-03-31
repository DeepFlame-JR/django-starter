from django.shortcuts import render, get_object_or_404
from third.models import Restaurant
from django.core.paginator import Paginator
from third.forms import RestaurantForm
from django.http import HttpResponseRedirect

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

def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            new_item = form.save()  # pk가 없기 때문에 새롭게 저장됨
        return HttpResponseRedirect('/third/list/')

    form = RestaurantForm()
    return render(request, 'third/create.html', {'form':form})

def update(request):
    if request.method == 'POST' and 'id' in request.POST:  # 데이터 업데이트
        # item = Restaurant.objects.get(pk=request.POST.get('id'))
        item = get_object_or_404(Restaurant, pk=request.POST.get('id'))
        form = RestaurantForm(request.POST, instance=item)  # pk를 지정할 수 있음
        if form.is_valid():
            item = form.save()  # pk가 지정되어 있기 때문에 데이터 업데이트
    elif request.method == 'GET':  # 데이터 가져오기
        # item = Restaurant.objects.get(pk=request.GET.get('id'))  # third/update?id=2
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        form = RestaurantForm(instance=item)
        return render(request, 'third/update.html', {'form':form})
    return HttpResponseRedirect('/third/list/')