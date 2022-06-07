# coding=utf-8
import pytest
import calorias

# Realizar un test para comprobar que el número de calorias inicial es 0
def test_default_initial_amount():
    calory = calorias.Calorias()
    assert calory.quantity == 0


# Realizar un test que inicialice el número de calorias a 100 y compruebe que se ha añadido correctamente
def test_setting_initial_amount():
    calory = calorias.Calorias(100)
    assert calory.quantity == 100

# Realizar un test que inicialice el número de calorias a 10. Añada 90 calorias y finalmente que compruebe que se ha añadido correctamente
def test__add_calories():
    calory = calorias.Calorias(10)
    calory.add_calories(90)
    assert calory.quantity == 100

# Realizar un test que inicialice el número de calorias a 20. Que gaste 10 calorias y finalmente que compruebe que se han gastado correctamente
def test_spend_calories():
    calory = calorias.Calorias(20)
    calory.spend_calories(10)
    assert calory.quantity == 10


