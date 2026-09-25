from .models import Suggestions


def suggestion_counts(request):
    if not request.user.is_authenticated:
        return {
            'suggestion_count': 0,
            'other_suggestion_count': 0,
        }

    own_suggestions = Suggestions.objects.filter(
        submitted_by=request.user
    )
    other_suggestions = Suggestions.objects.none()

    if request.user.is_superuser:
        other_suggestions = Suggestions.objects.exclude(
            submitted_by=request.user
        )

    return {
        'suggestion_count': own_suggestions.count(),
        'other_suggestion_count': other_suggestions.count(),
    }
