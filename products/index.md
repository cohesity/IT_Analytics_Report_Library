---
layout: default
title: Products
---
# Browse by Product

{% assign groups = site.products | group_by: "section" | sort: "name" %}
{% for g in groups %}
## {{ g.name }}
<ul class="report-list">
  {% assign items = g.items | sort: "display_order" %}
  {% for p in items %}
  <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
  {% endfor %}
</ul>
{% endfor %}
