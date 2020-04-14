from django.urls import path
from FoodBankManage import views

# SET THE NAMESPACE!
app_name = 'FoodBankManage'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('foodBankBeneficiary/',views.foodBankBeneficiary,name='foodBankBeneficiary'),
    path('foodBankInventory/',views.foodBankInventory,name='foodBankInventory'),
    path('user_login/',views.user_login,name='user_login'),
    path('Blockname/',views.Blockname,name='Blockname'),
    path('Blockname2/',views.Blockname2,name='Blockname2'),
    path('foodBankAdd/',views.foodBankAdd,name='foodBankAdd'),
    path('foodBankInventrydryAdd/',views.foodBankInventrydryAdd,name='foodBankInventrydryAdd'),
    path('foodBankInventrymidAdd/',views.foodBankInventrymidAdd,name='foodBankInventrymidAdd'),
    path('foodBankInventrycookAdd/',views.foodBankInventrycookAdd,name='foodBankInventrycookAdd'),
]
