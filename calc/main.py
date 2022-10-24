import user_interface as ui
import logger as log
import complex as cn
import rational as rn

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_menu = ui.load_menu_main()
    operations_menu = ui.load_menu_operation()
    select_main_menu = 1
    while select_main_menu != 0:
        ui.print_menu('ГЛАВНОЕ МЕНЮ', main_menu)
        select_main_menu = ui.get_select_menu(main_menu)
        if select_main_menu == 0:
            break

        ui.print_menu('Меню операций', operations_menu)
        select_operation_menu = ui.get_select_menu(operations_menu)
        if select_operation_menu == 0:
            continue

        # определение оператора вычисления
        operator = ''
        if select_operation_menu == 4:
            operator = 'div'
            if select_main_menu != 2:
                operations_menu_div = ui.load_menu_operation_div()
                ui.print_menu('Деление', operations_menu_div)
                select_operation_menu_div = ui.get_select_menu(operations_menu_div)
                operator = operations_menu_div[select_operation_menu_div][1]
        else:
            operator = operations_menu[select_operation_menu][1]

        # запуск выполнения выбранной операции
        if select_main_menu == 1:
            input_data = ui.input_operation_data(operator, 'rational')
            if input_data is None:
                res = None
                print('Выполнение операции прервано!')
            else:
                res = rn.calc(operator, input_data)
                print(f'Результат: {res}')
        else:
            input_data = ui.input_operation_data(operator, 'complex')
            if input_data is None:
                res = None
                print('Выполнение операции прервано!')
            else:
                res = cn.calc(operator, input_data)
                print(f'Результат: {res}')

        # логирование - запись результат в файл CSV
        if res is not None:
            input1 = input_data[0]
            input2 = None
            if len(input_data) > 1:
                input2 = input_data[1]
            log.operation_logger(input1, operator, input2, res)
