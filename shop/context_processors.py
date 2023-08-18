from .models import Category, Subcategory

def category_list(request):
    return {
   
        'categories' : Category.objects.all(),
        'subcategories': Subcategory.objects.all()
    }

