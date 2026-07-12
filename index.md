---
layout: default
title: Catalog
---

# {{ site.title }}

{{ site.description }}

<input type="text" id="filter" placeholder="Filter by composer, title, or editor...">

<table id="catalog">
  <thead>
    <tr>
      <th>Composer</th>
      <th>Title</th>
      <th>Editor</th>
    </tr>
  </thead>
  <tbody>
    {% for row in site.data.metadata %}
    <tr>
      <td>{{ row.composer }}</td>
      <td><a href="{{ site.baseurl }}/works/{{ row.filename | split: '.' | first }}/">{{ row.title }}</a></td>
      <td>{{ row.editor }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

<script src="{{ site.baseurl }}/assets/js/catalog-filter.js"></script>
