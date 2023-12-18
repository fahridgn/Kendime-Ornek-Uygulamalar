from django.shortcuts import redirect, render
from .models import Theme
from backend import deney
from django.http import HttpResponse

# Create your views here.


def themeview(request):
    """
    Bu görünüm, tüm temaları ID'ye göre ters sıralar ve bunları bir HTML şablonuna geçirir.
    """
    themes = Theme.objects.all().values()
    sorted_themes = sorted(themes, key=lambda x: x["id"], reverse=True)
    return render(request, "theme_list.html", {"themes": sorted_themes})


def deneyview(request):
    """
    Bu görünüm, bir dizi HTML etiketi oluşturur ve bunları bir HttpResponse nesnesine döndürür.
    """
    mylist = [i for i in range(1, 100)]
    result = deney.join("div", "class", "burası attrs value", "bu kısım içerik")
    for i in mylist:
        result += deney.join("h3", "class", f"deney{i}", "deney")
    return HttpResponse(result)


def theme_update(request, pk):
    """
    Bu görünüm, bir tema nesnesini günceller veya bir tema güncelleme formu döndürür.
    """
    theme = Theme.objects.get(pk=pk)
    if request.method == "POST":
        theme.name = request.POST.get("name")
        theme.save()
        return render(request, "theme_detail.html", {"theme": theme})
    else:
        return render(request, "theme_update.html", {"theme": theme})


def theme_detail(request, pk):
    theme = Theme.objects.get(pk=pk)
    return render(request, "theme_detail.html", {"theme": theme})


def theme_delete(request, pk):
    theme = Theme.objects.get(pk=pk)
    theme.delete()
    return redirect("theme")


def theme_add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        attrs = request.POST.get("attrs")
        value = request.POST.get("value")
        tag = request.POST.get("tag")
        theme = Theme(name=name, attrs=attrs, value=value, tag=tag)
        theme.save()
        return render(request, "theme_detail.html", {"theme": theme})
    else:
        return render(request, "theme_add.html")
