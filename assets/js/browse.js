(function () {
  var form = document.getElementById('browse-filters');
  var results = document.getElementById('browse-results');
  var countEl = document.getElementById('browse-count');
  var clearBtn = document.getElementById('browse-clear');
  var sqlInput = document.getElementById('filter-sql');
  if (!form || !results) return;

  var index = null;
  fetch('/assets/search-index.json')
    .then(function (r) { return r.json(); })
    .then(function (data) { index = data; render(); });

  function checkedValues(selector) {
    return Array.prototype.map.call(form.querySelectorAll(selector + ':checked'), function (el) { return el.value; });
  }

  function escapeHtml(s) {
    return s.replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  // '%' is a wildcard for "any sequence of characters" (SQL LIKE-style,
  // since this is a SQL search box) - everything else, including '_', is
  // matched literally. '_' is deliberately NOT a wildcard even though real
  // SQL LIKE treats it as "any single character": these view/column names
  // (apt_v_nbu_job_detail, etc.) are full of literal underscores, so
  // treating them as wildcards would make every search far too loose.
  function buildSqlMatcher(pattern) {
    if (!pattern) return null;
    var escaped = pattern.replace(/[.*+?^${}()|[\]\\]/g, '\\$&').replace(/%/g, '.*');
    return new RegExp(escaped, 'i');
  }

  // Returns the SQL line containing the match, trimmed and length-capped,
  // so a match shows *where* it hit instead of dumping the whole query
  // into the results list.
  function sqlSnippet(sql, matcher) {
    var m = matcher.exec(sql);
    if (!m) return '';
    var idx = m.index;
    var lineStart = sql.lastIndexOf('\n', idx) + 1;
    var lineEnd = sql.indexOf('\n', idx);
    if (lineEnd === -1) lineEnd = sql.length;
    var line = sql.slice(lineStart, lineEnd).trim();
    return line.length > 140 ? line.slice(0, 140) + '…' : line;
  }

  function render() {
    if (!index) return;
    var cats = checkedValues('.filter-category');
    var prods = checkedValues('.filter-product');
    var sqlMatcher = sqlInput ? buildSqlMatcher(sqlInput.value.trim()) : null;
    var matches = index.filter(function (r) {
      var catOk = cats.length === 0 || (r.category_slugs || []).some(function (s) { return cats.indexOf(s) !== -1; });
      var prodOk = prods.length === 0 || (r.product_slugs || []).some(function (s) { return prods.indexOf(s) !== -1; });
      var sqlOk = !sqlMatcher || sqlMatcher.test(r.sql_query || '');
      return catOk && prodOk && sqlOk;
    }).sort(function (a, b) { return a.title.localeCompare(b.title); });

    countEl.textContent = matches.length + ' report' + (matches.length === 1 ? '' : 's');
    results.innerHTML = matches.map(function (r) {
      var snippet = sqlMatcher ? sqlSnippet(r.sql_query || '', sqlMatcher) : '';
      var snippetHtml = snippet ? '<div class="sql-snippet"><code>' + escapeHtml(snippet) + '</code></div>' : '';
      return '<li><a href="' + r.url + '">' + r.title + '</a>' + snippetHtml + '</li>';
    }).join('');
  }

  // This form has no real submit target - it's a pure client-side filter
  // panel. Without this, pressing Enter in the (sole) text field triggers
  // the browser's implicit form submission, reloading the page and wiping
  // out whatever was typed - exactly the "search has no effect" symptom.
  form.addEventListener('submit', function (e) { e.preventDefault(); });

  form.addEventListener('change', render);
  if (sqlInput) sqlInput.addEventListener('input', render);
  clearBtn.addEventListener('click', function () {
    Array.prototype.forEach.call(form.querySelectorAll('input[type=checkbox]'), function (el) { el.checked = false; });
    if (sqlInput) sqlInput.value = '';
    render();
  });
})();
