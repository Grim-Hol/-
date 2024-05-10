from .models import Articles

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        bod = Articles.objects.all()
        return context
