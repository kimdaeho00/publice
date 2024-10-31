from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transaction  # Transaction 모델이 정의되어 있어야 합니다.
from .serializers import TransactionSerializer  # Serializer도 정의되어 있어야 합니다.

class TransactionList(APIView): #
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class TransactionDetail(APIView):
    def get(self, request, pk):
        transaction = Transaction.objects.get(pk=pk)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, pk):
        transaction = Transaction.objects.get(pk=pk)
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        transaction = Transaction.objects.get(pk=pk)
        transaction.delete()
        return Response(status=204)
