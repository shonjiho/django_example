
# Django Template

Remove hardcoded URLs in template

```html
<a href=/polls/{{question.id}}/">

```
Problem with this hardcoded, 
tightly-coupled approach is that it becomes challenging to change URLs on projects with a lot of templates

Use 'name' argument in path() functions in urls.py(URLconf)
```html
<a href="{% url "polls:detail" question.id %}">
```
this resolve coupling!


