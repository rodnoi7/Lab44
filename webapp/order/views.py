from django.shortcuts import render, redirect, get_object_or_404
from order.models import Employee, Food, Order, OrderFood

# Create your views here.

def index_view(request):
	return render(request, 'index.html')


def foods_list(request):
	food = Food.objects.all()
	context = {
		'foods': food,
	}
	return render(request, 'foods_list.html', context)

def add_food(request):
	if request.method == 'GET':
		return redirect('add_food.html')
	elif request.method == 'POST':
		name = request.POST.get('name')
		description = request.POST.get('description')
		photo = request.POST.get('photo')
		price = request.POST.get('price')
		Food = create(name=name, description=description, photo=photo, price=price)
		Food.save()
		food = Food.objects.all()
		context = {
			'foods': food,
		}
		return render(request, 'foods', context)

def update_food(request):
	pass
