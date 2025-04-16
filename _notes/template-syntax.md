<!--


{% extends 'core/layouts/core.layout.html' %}

{% block title %}{{ title }} | Home{% endblock %}

{% block content %}
  <h1 style="background: orange;">{{ welcome_message }}</h1>

  {% comment %} array index {% endcomment %}
  {{users.0.name}}

  {% comment %} generate link: with route name {% endcomment %}
  <a href="{% url 'about' %}">about page</a>

  {% comment %} filters

  Common Filters:
  |lower, |upper: Case conversion.
  |length: Length of a string or list.
  |default:"value": Fallback if variable is undefined.
  |date:"Y-m-d": Format dates (if you add datetime data).
  |truncatewords:5: Shorten text to 5 words.
  |add:10: Add a number (e.g., {{ user.age|add:10 }}).
  {% endcomment %}
  <p style="color: red;">
    {{users.0.name|upper}}
    *
    {{users.0.name|length}}
    *
    {{users.1.name|default:"no users found"}}
  </p>

  {% comment %}

  if statement

  {% if condition %} ... {% endif %}
  {% if condition %} ... {% else %} ... {% endif %}
  Operators: ==, !=, <, >, in, and, or, not.
    {% endcomment %}
  {% if products %}
    <div>{{products.0.name}}</div>
    {% else %}
      <div>no products</div>
  {% endif %}

  {% comment %}
  Syntax: (for loop)
    {% for item in iterable %} ... {% endfor %}
    {% empty %}: Displays if the iterable is empty.
    forloop variables:
    forloop.counter: 1-based index.
    forloop.counter0: 0-based index.
    forloop.first: True for the first iteration.
    forloop.last: True for the last iteration.

  {% endcomment %}
  <ul style="list-style: none; display: flex; flex-direction: column; gap: 10px;">
  {% for user in users %}
    {% include 'core/components/_user-card.co.html' with user=user %}

    {% empty %}
      <li>no users found</li>
  {% endfor %}
  </ul>

  {% comment %}
  include partials
  Usage: {% include 'path/to/partial.html' %}.
  {% endcomment %}
{% endblock %}


# method="post" for create and update

 -->
