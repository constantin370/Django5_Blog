from django.views.generic import DetailView
from discontcard.models import DiscontCard


class DiscontManagerView(DetailView):
    """Класс представления дисконтной карты."""
    template_name = "discontcard/index.html"
    model = DiscontCard
    context_object_name = "discontcard"

    def get_object(self, queryset = None):
        return DiscontCard.objects.filter(
            number=str(self.request.user.discont_card)
            )[0]

    
