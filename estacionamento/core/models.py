from django.db import models
from django.utils import timezone

class Carro(models.Model):
    placa = models.CharField(max_length=10)
    entrada = models.DateTimeField(default=timezone.now)
    saida = models.DateTimeField(null=True, blank=True)

    def tempo_total(self):
        if self.saida:
            return self.saida - self.entrada
        return None

    def valor_pago(self):
        if not self.saida:
            return None

        total_minutos = (self.saida - self.entrada).total_seconds() / 60
        total_horas = int(total_minutos // 60)

        if total_minutos <= 10:
            return 0.0

        if total_minutos % 60 > 0:
            total_horas += 1

        if total_horas <= 1:
            return 5.0
        else:
            return 5.0 + (total_horas - 1) * 2.0

    def __str__(self):
        return self.placa
