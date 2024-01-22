from django.shortcuts import render
from django.views import View
from .models import VideoContent
from django.core.paginator import Paginator

# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        page = 1
        if request.GET.get("page"):
            page = int(request.GET.get("page"))
        videos = VideoContent.objects.all()
        paginator = Paginator(videos , 1)
        page_objects = paginator.get_page( page )  
        print()  
        print(page_objects.object_list)  
        print()  
        context = {'videos': page_objects.object_list ,"page_objects":page_objects, 'paginator': paginator}
        return render(request, "index.html", context )

