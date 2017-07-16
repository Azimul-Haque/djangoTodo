from .models import Category, Priority

def include_categories(request):
    categories = Category.objects.all()            
    return {'categories': categories}



def include_priorities(request):
    priorities = Priority.objects.all()            
    return {'priorities': priorities}