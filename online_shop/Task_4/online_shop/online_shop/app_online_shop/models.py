from django.db import models
from django.db import migrations
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class advertisements(models.Model):
    # Заголовок
    title = models.CharField('Заголовок', max_length=128) # Символьное поле - для не больших текстов
    # Описание обьявления
    description = models.TextField('Описание') # Строковое поле - для больших размеров
    # Цена 
    # Decimal похоже на float, но Decimal с фиксируемой точкой
    price = models.DecimalField('Цена', max_digits=15, decimal_places=2) # max_digits - Максимальное кол-во чисел, decimal_places - кол-во чисел после запятой
    # Возможност торговаться
    # BooleanFiled - логический тип данных(True/False)
    auction = models.BooleanField('Возможность торга', help_text='Отметьте, уместен ли торг')
    # Дата размещения
    # DateTimeField - поле для даты и времени
    created_time = models.DateTimeField(auto_now_add=True) # auto_now_add - получение даты в момент создания обьявления
    # Дата обновления
    update_time = models.DateTimeField(auto_now=True) # auto_now - получение даты в момент обьявленияDateTimeField
    def __str__(self): 
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'
    # <Advertisement: Advertisement(id=1, title=Заголовок №1, price=100.00)>.
    # Поле для создателя обьявления(Пользователя)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    # Поле для изображения
    image = models.ImageField('Изображение', upload_to='online_shop/')

    class Meta: 
        db_table = 'advertisements'