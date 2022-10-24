from django.utils.deprecation import MiddlewareMixin
from user.models import User
from lib.http import render_response
from common.error import SESSION_ERROR


class AuthMiddleware(MiddlewareMixin):
    White_list = [
        '/user/verify',
        '/user/login'
    ]

    def process_request(self, request):
        for white_path in self.White_list:
            if white_path.startswith(request.path):
                return
        uid = request.session.get('uid')
        if uid:
            try:
                request.user = User.objects.get(id=uid)
                return
            except User.DoesNotExist:
                request.session.flush()
        return render_response(None, SESSION_ERROR)
