from django.shortcuts import render


def page_not_found(request, exception):
    """ Обработка ошибки 404 """
    return render(
        request=request,
        template_name='core/404.html',
        status=404,
        context={
            'title': 'Страница не найдена: 404',
            'error_message': 'К сожалению такая страница '
                             'была не найдена, или перемещена',
        })


def server_error(request):
    """ Обработка ошибки 500 """
    return render(
        request=request,
        template_name='core/500.html',
        status=500,
        context={
            'title': 'Ошибка сервера: 500',
            'error_message': 'Внутренняя ошибка сайта, '
                             'вернитесь на главную страницу, '
                             'отчет об ошибке мы направим '
                             'администрации сайта',
        })


def permission_denied(request, exception):
    """ Обработка ошибки 403 """
    return render(
        request=request,
        template_name='core/403.html',
        status=403,
        context={
            'title': 'Ошибка доступа: 403',
            'error_message': 'Доступ к этой странице ограничен',
        })
