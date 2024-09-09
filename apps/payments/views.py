from rest_framework import viewsets,permissions
from apps.payments.models import Payment
from apps.payments.serializers import PaymentSerializer, PaymentCreateSerializer, PaymentUpdateSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


    def get_serializer_class(self):
        if self.action == 'create':
            return PaymentCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return PaymentUpdateSerializer
        return PaymentSerializer