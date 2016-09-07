from django import template
register = template.Library()


@register.inclusion_tag('drivingtest/form_table_manager.html', takes_context=True)
def render_crispy_form_and_table(context,form,table):
    return {'form': form,'table':table}