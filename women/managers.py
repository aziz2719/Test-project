from django.db import models
from women import models as ca_models


class WomenManager(models.Manager):
    def get_or_new(self, request):
        user = request.user
        women_id = request.session.get('women_id', None)
        if user is not None and user.is_authenticated:
            if user.women:
                women_obj = request.user.cart
            else:
                women_obj = ca_models.Women.objects.get(pk=women_id)
                women_obj.user = user
                women_obj.save()
            return women_obj
        else:
            women_obj, created = ca_models.Women.objects.get_or_create(pk=women_id)
            women_id = request.session['women_id'] = women_obj.id
            return women_obj
