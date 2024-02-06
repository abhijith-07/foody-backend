from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    foodData = [
        {
            "name": "Boiled Egg",
            "price": 10,
            "text": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatum.",
            "image": "/images/egg.png",
            "type": "breakfast",
        },
        {
            "name": "RAMEN",
            "price": 25,
            "text": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatum.",
            "image": "/images/ramen.png",
            "type": "lunch",
        },
        {
            "name": "GRILLED CHICKEN",
            "price": 45,
            "text": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatum.",
            "image": "/images/chicken.png",
            "type": "dinner",
        },
        {
            "name": "CAKE",
            "price": 18,
            "text": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatum.",
            "image": "/images/cake.png",
            "type": "breakfast",
        },
        {
            "name": "BURGER",
            "price": 23,
            "text": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatum.",
            "image": "/images/burger.png",
            "type": "lunch",
        },
        {
            "name": "PANCAKE",
            "price": 25,
            "text": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatum.",
            "image": "/images/pancake.png",
            "type": "dinner",
        }
    ]
    
    return JsonResponse(foodData, safe=False)
