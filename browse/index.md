---
layout: default
title: Browse
---
# Browse Reports

<p class="report-desc">Select any number of categories and/or products, and/or search report SQL for a table or column name. Selections within a group are combined with OR; different groups (including SQL search) are combined with AND.</p>

<form id="browse-filters">
  <details id="browse-filters-details" class="browse-filters-details" open>
    <summary>Filters</summary>
    <div class="browse-filters">
      <fieldset>
        <legend>SQL Content</legend>
        <input type="search" id="filter-sql" placeholder="e.g. apt_v_nbu_job_detail or apt_v_%job_detail" autocomplete="off">
        <p class="meta">Use <code>%</code> to match any sequence of characters if you're not sure of the exact name (e.g. <code>apt_v_%job_detail</code>). <code>_</code> is matched literally, not as a wildcard.</p>
      </fieldset>

      <fieldset>
        <legend>Categories</legend>
        <ul class="filter-list">
          {% assign cats = site.categories | sort: "title" %}
          {% for c in cats %}
          <li><label><input type="checkbox" class="filter-category" value="{{ c.slug }}"> {{ c.title }}</label></li>
          {% endfor %}
        </ul>
      </fieldset>

      <fieldset>
        <legend>Products</legend>
        {% assign groups = site.products | group_by: "section" | sort: "name" %}
        {% for g in groups %}
        <h4>{{ g.name }}</h4>
        <ul class="filter-list">
          {% assign items = g.items | sort: "display_order" %}
          {% for p in items %}
          <li><label><input type="checkbox" class="filter-product" value="{{ p.slug }}"> {{ p.title }}</label></li>
          {% endfor %}
        </ul>
        {% endfor %}
      </fieldset>
    </div>
  </details>
</form>

<div class="browse-results-header">
  <p id="browse-count" class="report-desc"></p>
  <button type="button" id="browse-clear" class="btn">Clear filters</button>
</div>
<ul id="browse-results" class="report-list"></ul>
