from django.shortcuts import render, get_object_or_404, redirect
from third.models import Restaurant, Review
from django.core.paginator import Paginator
from third.forms import RestaurantForm, ReviewForm, UpdateRestaurantForm
from django.http import HttpResponseRedirect
from django.db.models import Count, Avg

# Create your views here.
def list(request):
    # reviews_count 필드를 생성하고 계산한다
    # Restaurant에는 Review를 정의하지 않았지만, relation이 설정되어 인식이 가능하다
    restaurants = Restaurant.objects.all().annotate(reviews_count=Count('review')).annotate(average_point=Avg('review__point'))
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
        password = request.POST.get('password','')  # 사용자에게서 가져온 password 값
        form = UpdateRestaurantForm(request.POST, instance=item)  # pk를 지정할 수 있음
        if form.is_valid() and password == item.password:
            item = form.save()  # pk가 지정되어 있기 때문에 데이터 업데이트
    elif request.method == 'GET':  # 데이터 가져오기
        # item = Restaurant.objects.get(pk=request.GET.get('id'))  # third/update?id=2
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        form = RestaurantForm(instance=item)
        return render(request, 'third/update.html', {'form':form})
    return HttpResponseRedirect('/third/list/')

def detail(request, rid):
    if id is not None:
        item = get_object_or_404(Restaurant, pk=rid)
        reviews = Review.objects.filter(restaurant=item).all()
        return render(request, 'third/detail.html', {'item':item, 'reviews':reviews})
    return HttpResponseRedirect('/third/list/')

def delete(request, id):
    item = get_object_or_404(Restaurant, pk=id)
    if request.method=='POST' and 'password' in request.POST:
        if item.password == request.POST.get('password') or item.password is None:
            item.delete()
            return redirect('list')  # 삭제 성공
        return redirect('restaurant-detail', id=id)  # 비밀번호가 틀려서 삭제 실패
    return render(request, 'third/delete.html', {'item':item})  # GET

def review_create(request, restaurant_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return redirect('restaurant-detail', rid=restaurant_id)
    item = get_object_or_404(Restaurant, pk=restaurant_id)
    form = ReviewForm(initial={'restaurant':item})
    return render(request, 'third/review_create.html', {'form':form, 'item':item})

def review_delete(request, restaurant_id, review_id):
    item = get_object_or_404(Review, pk=review_id)
    item.delete()
    return redirect('restaurant-detail', rid=restaurant_id)
    
def review_list(request):
    # select_related(): 관련된 정보를 모두 가져옴 (fk의 모든 내용을 가져옴)
    # 따라서 쿼리를 여러번 실행할 것을 한번만 실행해 도됨
    reviews = Review.objects.all().select_related().order_by('-created_at')  # 최신 순으로
    paginator = Paginator(reviews, 10)
    
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'third/review_list.html', {'reviews':items})
    