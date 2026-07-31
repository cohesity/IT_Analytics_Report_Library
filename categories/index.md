---
layout: default
title: Categories
---
# Browse by Category

<ul class="report-list">
{% assign cats = site.categories | sort: "title" %}
{% for c in cats %}
  <li><a href="{{ c.url | relative_url }}">{{ c.title }}</a></li>
{% endfor %}
</ul>
