from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, View
from .models import Review
from .forms import ReviewForm


def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'review/upload.html', {'file_url': file_url})
    return render(request, 'review/upload.html')


class ReviewListView(ListView):
    template_name = "review/list.html"
    model = Review
    context_object_name = "reviews"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_favorites = self.request.session.get('favorite')
        context['my_favorite'] = my_favorites or []
        return context


class ReviewCreateView(View):
    def get(self, request):
        form = ReviewForm
        return render(request, "review/create.html", {"review_form": form})

    def post(self, request):
        form = ReviewForm(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            form.save()
            return redirect("/list")
        return render(request, "review/create.html")

class AddFavoriteView(View):
    def post(self, request):
        my_favorite = request.session.get("favorite")
        if my_favorite is None:
            my_favorite = []

        caracter_id = request.POST["review_id"]
        my_favorite.append(int(caracter_id))
        request.session["favorite"] = list(set(my_favorite))
        return redirect("/list")


def delete_favorite(request, id):
    my_favorite = request.session.get("favorite")
    my_favorite.remove(id)
    request.session["favorite"] = list(set(my_favorite))
    return redirect("/list")
