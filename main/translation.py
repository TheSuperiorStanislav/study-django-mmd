from modeltranslation.translator import translator, TranslationOptions
from main.models import MovieDetails

class MovieDetailsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
    required_languages = ('en-us', 'ru')

translator.register(MovieDetails, MovieDetailsTranslationOptions)