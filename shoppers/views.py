from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProductDetails,Customer

class ProductViews(APIView):
    def post(self,request):
        print(request.data)
        product=request.data
        cus_obj = Customer.objects.get(id=product.get("customer_id"))
        if cus_obj:
            pd_obj = ProductDetails.objects.create(name=product.get('name'),price=product.get('price'),size=product.get('size'),category=product.get('category'),quantity=product.get('quantity'))
        cus_obj.product=pd_obj
        cus_obj.save()
        return Response({"status":200,"message":"product has been added","data":{}})

    def get(self,request):
        customer_id=request.GET.get('customer_id')
        print(customer_id)
        cus_obj = Customer.objects.get(id=customer_id)
        if cus_obj:
            data = ProductDetails.objects.filter(id=cus_obj.product.id).values()

        print(data)
        return Response({"status":200,"message":"success","data":data[0]})
