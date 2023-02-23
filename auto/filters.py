from django_filters import FilterSet
from .models import Letter
import pdb

class LetterFilter(FilterSet):

    class Meta:
        model = Letter
        fields = [...]

    @property
    def qs(self):
        parent = super().qs
        author = getattr(self.request, 'user', None)
        pdb.set_trace()
        return parent.filter(sender=author) \
            | parent.filter(reciver=author)