from corsheaders.signals import check_request_enabled

from apps.flowers.models import MySite
from apps.carts.models import MySite
from apps.categories.models import MySite
from apps.feedback.models import MySite
from apps.orders.models import MySite
from apps.payments.models import MySite
from apps.posts.models import MySite
from apps.users.models import MySite
from corsheaders.signals import check_request_enabled



def cors_allow_mysites(sender, request, **kwargs):
    return MySite.objects.filter(host=request.headers["origin"]).exists()


check_request_enabled.connect(cors_allow_mysites)

def cors_allow_api_to_everyone(sender, request, **kwargs):
    return request.path.startswith("/api/")


check_request_enabled.connect(cors_allow_api_to_everyone)