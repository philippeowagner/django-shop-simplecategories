from django import template

from classytags.helpers import InclusionTag

from ..models import Category

register = template.Library()


class RootCategoryTag(InclusionTag):
    template = 'shop_simplecategories/show_root_categories.html'
    name = 'show_root_categories'

    def get_context(self, context):
        return {'categories': Category.objects.root_categories(),}

register.tag(RootCategoryTag)



class RootWithChildCategoryTag(InclusionTag):
    template = 'shop_simplecategories/show_root_with_child_categories.html'
    name = 'show_root_with_child_categories'

    def get_context(self, context):
        return {'categories': Category.objects.root_categories(),}

register.tag(RootWithChildCategoryTag)


class RootWithChildCategoryTagShop(InclusionTag):
    template = 'shop_simplecategories/show_root_with_child_categories_shop.html'
    name = 'show_root_with_child_categories_shop'

    def get_context(self, context):
        return {'categories': Category.objects.root_categories(),}

register.tag(RootWithChildCategoryTagShop)
