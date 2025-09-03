from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import get_user_model


class SaveIpMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            ip = request.META.get('REMOTE_ADDR')
            user = request.user
            if user.last_login_ip != ip:
                user.last_login_ip = ip
                user.save(update_fields=['last_login_ip'])
