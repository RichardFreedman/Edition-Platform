---
layout: default
title: Catalog
---

# {{ site.title }}

{{ site.description }}

<input type="text" id="filter" placeholder="Filter by composer, title, editor, date, or source...">

<table id="catalog">
  <thead>
    <tr>
      <th>Composer</th>
      <th>Title</th>
      <th>Editor</th>
      <th>Date</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    {% for row in site.data.metadata %}
    <tr>
      <td>{{ row.composer }}</td>
      <td><a href="{{ site.baseurl }}/works/{{ row.id }}/">{{ row.title }}</a></td>
      <td>{{ row.editor }}</td>
      <td>{{ row.date }}</td>
      <td>{{ row.source }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

<script src="{{ site.baseurl }}/assets/js/catalog-filter.js"></script>
