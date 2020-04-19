from django.db import models

# Create your models here.
#这是这个app的数据库
class Country(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):#返回一个对象的免俗信息，注意要用self.
        return self.name

class Data(models.Model):
    new_deaths = models.BigIntegerField()#BigIntegerField表示64位的正负整数，'new deaths'定义的人类可读的名字
    total_deaths = models.BigIntegerField()
    country = models.ForeignKey(Country,on_delete=models.CASCADE)#这是一个外部键
    def __str__(self):
        return "新增死亡是{0}人,总死亡是{1}人".format(self.new_deaths,self.total_deaths)
