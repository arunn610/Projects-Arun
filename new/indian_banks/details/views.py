import csv
from django.http import JsonResponse
from details.models import Bank
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist



class bankviewset(ViewSet): 
    def bank_list(self, request): 
        if request.method == 'GET':
            banks = Bank.objects.all()
            data = [{'name': bank.bank_name, 'branch': bank.branch} for bank in banks]
            return JsonResponse({'banks': data},status= 200)

    
    def bank_details(self,request,branch):
        if request.method == 'GET':
            try:
                bank = Bank.objects.get(branch=branch)
                data = [{'name': bank.bank_name, 'branch': bank.branch, 'ifsc':bank.ifsc, 'city':bank.city} ]
                return JsonResponse({'banks': data},status= 200)
            
            except ObjectDoesNotExist:
                return JsonResponse({'error': 'Bank not found'}, status= 404)


    def load_data():
        with open('banking_projects/bank_branches.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                Bank.objects.create(    
                    ifsc=row[0],
                    bank_id= row[1],
                    branch=row[2],
                    address=row[3],
                    city=row[4],
                    district=row[5],
                    state=row[6],
                    bank_name=row[7],
                )


