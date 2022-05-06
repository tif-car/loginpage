from django.db import models

# Create your models here.

class Stocks(models.Model):
    stock_id = models.AutoField(primary_key=True)
    tradedate = models.DateField(db_column='TradeDate', blank=True, null=True)  # Field name made lowercase.
    aapl = models.CharField(db_column='AAPL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    msft = models.CharField(db_column='MSFT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    goog = models.CharField(db_column='GOOG', max_length=10, blank=True, null=True)  # Field name made lowercase.
    amzn = models.CharField(db_column='AMZN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tsla = models.CharField(db_column='TSLA', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stocks'
        