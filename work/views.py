from django.shortcuts import render , get_object_or_404
from django.utils import timezone
from work.models import Work , Album

def work_page(request):
    works = Work.objects.filter(status=1,publish_date__lte=timezone.now())
    albums = Album.objects.all()
    context = {'works':works ,'albums': albums}
    return render(request,'work/workpage.html', context)

def work_single(request , pid):
    works = Work.objects.filter(publish_date__lte=timezone.now(),status=1)
    work = get_object_or_404(works , pk=pid)
    return render(request,'work/work_single.html',{'work':work})