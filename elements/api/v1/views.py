from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q, QuerySet
from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from elements.models import ImageData


class ImagesApiMixin:
    model = ImageData
    http_method_names = ['get']

    def get_queryset(self) -> QuerySet:
        # return ImageData.objects.all()
        return ImageData.objects.all().values('id','title', 'description', 'image')


    def render_to_response(self, context, **response_kwargs):
        try:
            return JsonResponse(context)
        except:
            return HttpResponse(context)


class ImagesListApi(ImagesApiMixin, BaseListView):
    model = ImageData
    http_method_names = ['get']
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            queryset,
            self.paginate_by
        )
        page_num = self.request.GET.get('page', 1)
        if page_num == 'last':
            page_num = paginator.num_pages

        results = paginator.page(page_num)
        context = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': results.previous_page_number() if results.has_previous() else None,
            'next': results.next_page_number() if results.has_next() else None,
            'results': list(results.object_list),
        }
        return context


class ImagesDetailApi(ImagesApiMixin, BaseDetailView):
    def get_context_data(self, **kwargs) -> dict:
        image_id = kwargs['object'].get('id')
        queryset = self.get_queryset()
        result = queryset.filter(Q(id=image_id))
        return result.values()[0] if result else {}
