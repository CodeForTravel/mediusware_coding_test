from django.db.models import Q


class SearchMixin(object):
    """
    e.g Add the properties below with the ClassBasedView:
    search_fields = ["user__username", "object_repr"]
    """

    search_fields = None

    def get_queryset(self, *args, **kwargs):
        qs = super(SearchMixin, self).get_queryset()

        q = self.request.GET.get("search", "")

        # Multi keyword search
        q_list = q.split("|")

        # strip string
        q_list = [q.strip() for q in q_list]

        # Remove empty
        q_list = filter(bool, q_list)

        search_fields = Q()

        for q in q_list:
            if isinstance(self.search_fields, dict):
                for k, v in self.search_fields.items():
                    q_dict = {
                        "{}__{}".format(k, v): q,
                    }
                    search_fields = search_fields | Q(**q_dict)

            elif isinstance(self.search_fields, (list, tuple)):
                for f in self.search_fields:
                    q_dict = {
                        "{}__icontains".format(f): q,
                    }
                    search_fields = search_fields | Q(**q_dict)

        qs = qs.filter(search_fields)
        return qs

    def get_context_data(self, **kwargs):
        context = super(SearchMixin, self).get_context_data(**kwargs)
        query = self.request.GET.get("search", "")
        context["search_query"] = query.replace("+", " ") if query else ""
        return context


class FilterMixin(object):
    """
    e.g Add the properties below with the ClassBasedView:
    filter_fields = ['user', 'action_flag']
    """

    filter_fields = ()

    def get_queryset(self, *args, **kwargs):
        qs = super(FilterMixin, self).get_queryset(*args, **kwargs)

        filter_dict = self.request.GET.dict()
        if filter_dict:
            params = {}
            for fieldname, value in filter_dict.items():
                if fieldname and fieldname in self.filter_fields:
                    # Multiple values handling for a single input among query parameters.
                    # (Eg. url's side: &partition=1,2,3,4
                    # backend's side: .filter(partition__in = [1, 2, 3, 4]) )
                    if value:
                        if "," in value:
                            value_list = []

                            seperated_values = value.split(",")
                            for value in seperated_values:
                                value_list.append(value)

                            params[fieldname + "__in"] = value_list
                        # Single value handling
                        else:
                            params[fieldname] = value

            qs = qs.filter(**params)

        return qs

    def get_context_data(self, **kwargs):
        context = super(FilterMixin, self).get_context_data(**kwargs)
        # Sticky Choices after page reload
        context["filter_feature_enabled"] = True
        context["filter_fields"] = self.filter_fields
        context["selected_option"] = {}
        context["multiple_selected_option"] = {}
        context["is_filter_enabled"] = False

        for field_name in list(self.filter_fields):
            value = self.request.GET.get(field_name)

            if value:
                context["is_filter_enabled"] = True

                # when multiple values available in a single parameter
                if "," in value:
                    value_list = []

                    seperated_values = value.split(",")
                    for value in seperated_values:
                        value_list.append(int(value))

                    context["multiple_selected_option"][field_name] = value_list
                else:
                    context["selected_option"][field_name] = int(value)

        return context
