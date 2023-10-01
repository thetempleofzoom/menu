from django.shortcuts import render
from django.views import generic
from .models import Items

# can create class or function (def) views but class requires less code apparently.

#main menu (would work for main blog page)
class MenuList(generic.ListView):
    # note queryset and template_name are specific name variables in class views
    # pulls all inputs from Items database in one request
    queryset = Items.objects.order_by("-date_created")
    template_name = "index.html"

    # this name needs to be exactly so as it's a predefined function
    def get_context_data(self):
        context = {'meals':'hot cross bun'}
        return context

# detailed view when item clicked (or blog content)
class ItemDetail(generic.DetailView):
    model = Items
    template_name = "detail.html"
