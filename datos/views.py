from django.views import View
from .models import Company
from django.http import JsonResponse
import json

# Create your views here.


class companyListView(View):

    def get(self, request):
        Companylist = Company.objects.all()
        return JsonResponse(list(Companylist.values()), safe=False)

    def post(self, request):
        dicionario=json.loads(request.body)
        nombre = Company.objects.create(personaje=dicionario['personaje'],cc=dicionario['cc'],celular=dicionario['celular'])
       
        return self.get(nombre)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            company = Company.objects.get(id=id)
            company.personaje = jd['personaje']
            company.cc = jd['cc']
            company.celular = jd['celular']
            company.save()
            datos = {'message': "Success","datos":{"nombre":company.personaje,
                                                    "cc":company.cc,
                                                    "cedula":company.celular}}
        else:
            datos = {'message': "user not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            Company.objects.filter(id=id).delete()
            datos = {'message': "Success data delete"}
        else:
            datos = {'message': "user not found..."}
        return JsonResponse(datos)
        
    