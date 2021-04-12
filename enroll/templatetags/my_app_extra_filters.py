from django import template
register = template.Library()


@register.filter
def add_class(modelform_input, css_class):
    if modelform_input.name=='is_superuser' or modelform_input.name=='is_staff' or modelform_input.name=='is_active':  # set the checkbox class
        return modelform_input.as_widget(attrs={'class': 'form-check-input'})
    # if modelform_input.name=='password':
    #     return modelform_input.as_widget(attrs={'class': css_class,'id':'disabledTextInput'})

    return modelform_input.as_widget(attrs={'class': css_class})


@register.filter
def add_class_label(field, class_name):
    print(field)
    return field.as_widget(attrs={
        "class": " ".join((field.css_classes(), class_name))
    })