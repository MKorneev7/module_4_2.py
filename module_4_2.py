def test_function( ):
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function() #здесь ничего не печатает

#inner_function() #здесь приводит к ошибке
#NameError: name 'inner_function' is not defined.


