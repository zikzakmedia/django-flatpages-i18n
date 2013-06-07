from modeltranslation.translator import translator, TranslationOptions

from flatpages_i18n.models import FlatPage_i18n


class FlatPageTranslationOptions(TranslationOptions):
    fields = ('url', 'title', 'content', 'metatitle', 'metadescription', 'metakeyword')


translator.register(FlatPage_i18n, FlatPageTranslationOptions)
