import csv
from django.http import HttpResponse
from tastypie.serializers import Serializer


class CSVSerializer(Serializer):
    formats = ['json', 'jsonp', 'csv']
    content_types = {
        'json': 'application/json',
        'jsonp': 'text/javascript',
        'csv': 'text/csv',
    }

    def to_csv(self, data, options=None):
        options = options or {}
        data = self.to_simple(data, options)
        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=somefilename.csv'

        writer = csv.writer(response)
        if 'objects' in data:
            for item in data['objects']:
                writer.writerow([unicode(item[key]).encode(
                            "utf-8", "replace") for key in item.keys()])
        else:
            writer.writerow([unicode(data[key]).encode(
                            "utf-8", "replace") for key in data.keys()])

        return response

    def from_csv(self, content):
        raise NotImplementedError
