import django_tables2 as tables
from .models import Suggestions


class SuggestionTable(tables.Table):

    class Meta:
        model = Suggestions
        template_name = "django_tables2/bootstrap4.html"
        fields = ("contributor_name", "suggestion_text", "completed_status")
        attrs = {"class": "suggestion-table"}

