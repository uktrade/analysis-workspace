from django import forms
from django.utils.safestring import mark_safe

from dataworkspace.forms import (
    GOVUKDesignSystemCheckboxesWidget,
    GOVUKDesignSystemForm,
    GOVUKDesignSystemMultipleChoiceField,
    GOVUKDesignSystemRadioField,
    GOVUKDesignSystemRadiosWidget,
    GOVUKDesignSystemTextareaField,
    GOVUKDesignSystemTextareaWidget,
)


class SupportForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label='Your email address',
        widget=forms.EmailInput(attrs={'class': 'govuk-input'}),
    )
    message = forms.CharField(
        required=True,
        label='Description',
        widget=forms.Textarea(attrs={'class': 'govuk-textarea'}),
        #
        # If you're here because you want to copy the help text (i.e. bullets as form hints), then please don't. If
        # this needs to be reused, we should probably do something else (e.g. convert it to markdown and add a markdown
        # filter that can output GOV.UK Design System-aware elements). So this HTML-in-code should either remain an
        # exception or eventually disappear.
        help_text=(
            mark_safe(
                """
<p class="govuk-hint">Please use this form to give us feedback or report a technical issue on Data Workspace.</p>
<p class="govuk-hint">If you had a technical issue, briefly explain:</p>
<ul class="govuk-list govuk-list--bullet govuk-hint">
  <li>what you did</li>
  <li>what happened</li>
  <li>what you expected to happen</li>
</ul>"""
            )
        ),
    )


HOW_SATISFIED_CHOICES = [
    'Very satisfied',
    'Satisfied',
    'Neither satisfied or dissatisfied',
    'Dissatisfied',
    'Very dissatisfied',
]

TRYING_TO_DO_CHOICES = [
    'Looking for data',
    'Trying to access data',
    'Analyse data',
    'Use a tool',
    'Create a data visualisation',
    'Share data',
    'Share a data visualisation',
    'View a data visualisation',
    'Other',
    'Don’t know',
]


class UserSatisfactionSurveyForm(GOVUKDesignSystemForm):
    how_satisfied = GOVUKDesignSystemRadioField(
        required=True,
        label='Overall how satisfied are you with the current Data Workspace?',
        widget=GOVUKDesignSystemRadiosWidget(label_size='m'),
        choices=tuple(zip(HOW_SATISFIED_CHOICES, HOW_SATISFIED_CHOICES)),
    )

    trying_to_do = GOVUKDesignSystemMultipleChoiceField(
        required=False,
        label='What were you trying to do today? (pick all that apply)',
        widget=GOVUKDesignSystemCheckboxesWidget(label_size='m'),
        choices=tuple(zip(TRYING_TO_DO_CHOICES, TRYING_TO_DO_CHOICES)),
    )

    improve_service = GOVUKDesignSystemTextareaField(
        required=False,
        label="""How could we improve the service? (Do not include any personal information,
                 like your name or email address. We'll delete any personal information you
                 do include""",
        widget=GOVUKDesignSystemTextareaWidget(label_size='m'),
    )
