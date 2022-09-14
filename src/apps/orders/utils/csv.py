import csv, datetime
from django.http import HttpResponse


def export_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = f'attachment; filename={opts.verbose_name}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not \
        field.many_to_many and not field.one_to_many] # Pega todos os campos excluindo Many to Many e One to Many
    writer.writerow([field.verbose_name for field in fields]) # Primeira linha, cabeçalho
    # Escreve as linhas de dados:
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_csv.short_description = 'Export to CSV'
