from django.shortcuts import render
from django.http import HttpResponse
from .models import Suggestions
from .models import Projects
from django_tables2 import SingleTableView
from .tables import SuggestionTable
from django.http import JsonResponse
import datetime

# Create your views here.

class PersonListView(SingleTableView):
    model = Suggestions
    table_class = SuggestionTable
    template_name = 'portfolio_site/index.html'


def index(request):
    """
    Index for site. Loads index.html
    :param request:
    :return: render
    """
    suggested_projects = Suggestions.objects.all()
    approved_projects = Projects.objects.all()
    table = SuggestionTable(Suggestions.objects.filter(approved=1))
    if len(table.rows) > 4:
        table.paginate(page=request.GET.get("page", 1), per_page=4)
    return render(
        request,
        'portfolio_site/index.html',
        {
            'table': table,
            'suggested_projects': suggested_projects,
            'approved_projects': approved_projects
        }
    )


def suggest(request):
    """
    View to process suggestions from Suggest Form.
    :param request:
    :return: JsonResponse
    """
    success = "Completed Successfully"
    time_now = datetime.datetime.now()
    suggest = Suggestions(contributor_name=request.POST.get('contributor'), created_date=time_now, suggestion_text=request.POST.get('suggestion'), completed_status=False)
    suggest.save()
    return JsonResponse({"success": success}, status=200)


def vote(request):
    """
    View to process votes on suggestions from Vote Form.
    :param request:
    :return: JsonResponse
    """
    id_selected = request.POST.get('myCheckboxes')
    id_selected = str(id_selected)
    ids = id_selected.split(",")
    for id in ids:
        selected_suggestion = Suggestions.objects.get(pk=id)
        selected_suggestion.vote_count += 1
        selected_suggestion.save()
    success = "Completed Successfully"
    return JsonResponse({"success": success}, status=200)
