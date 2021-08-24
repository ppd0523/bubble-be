from .serializers import *
from .models import *
from membership.models import User
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


# 권한 처리 필요
class ConditionView(viewsets.ViewSet):
    # 획득(GET)
    # GET /conditions?order=0,1,2,3
    def get(self, request, order=None, *args, **kwargs):
        # print(request.query_params)
        user_q = User.objects.get(username=request.user)
        if order:
            cond_qs = Condition.objects.get(cond_owner=user_q, cond_order=order)
            serializer = ConditionSerializer(cond_qs)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        order_str = request.query_params.get('order', None)
        if order_str:
            orders = list(map(int, order_str.strip(',').split(',')))
            cond_qs = Condition.objects.filter(cond_owner=user_q, cond_order__in=orders)

            serializer = ConditionSerializer(cond_qs, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            cond_qs = Condition.objects.filter(cond_owner=user_q)

        serializer = ConditionSerializer(cond_qs, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


    # 생성(POST)
    # Only admin
    def create(self, request, order=None, *args, **kwargs):
        user_q = User.objects.get(username=request.user)
        if order:
            # 생성할 객체 정보
            # request.FILES, request.data
            #serializer = ConditionSerializer(cond_qs)
            # return Response(status=status.HTTP_200_OK, data=serializer.data)
            pass

        if True:
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        # request.data['cond_order'] = cond_index
        # serializer = ConditionSerializer(data=request.data)  # cond_name
        #
        # if serializer.is_valid():
        #     serializer.save()
        #     res = Response(status=status.HTTP_201_CREATED)
        # else:
        #     print(serializer.errors)
        #     res = Response(status=status.HTTP_401_UNAUTHORIZED)
        #
        # return res


class ReportView(viewsets.ViewSet):
    def list(self, request, cond_index, create_date, *args, **kwargs):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def creates(self, request, cond_index, create_date, *args, **kwargs):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
