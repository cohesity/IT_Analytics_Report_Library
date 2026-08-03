(function () {
  var input = document.getElementById('search-input');
  var results = document.getElementById('search-results');
  if (!input || !results) return;

  // GitHub Pages project sites are served under /<repo-name>/, not the
  // domain root, so every absolute path (the index fetch, and each
  // result's href, which comes from the index's own baseurl-less "url"
  // field) needs this prefix - read from <body data-baseurl="..."> rather
  // than hardcoded, so it's correct in both local dev (empty) and
  // production (the repo name).
  var baseurl = document.body.dataset.baseurl || '';

  var index = null;
  fetch(input.dataset.indexUrl || baseurl + '/assets/search-index.json')
    .then(function (r) { return r.json(); })
    .then(function (data) { index = data; });

  function render(matches) {
    if (!matches.length) {
      results.innerHTML = '<div class="meta" style="padding:0.5rem 0.75rem">No matches</div>';
      results.classList.add('open');
      return;
    }
    results.innerHTML = matches.slice(0, 20).map(function (r) {
      return '<a href="' + baseurl + r.url + '"><strong>' + r.title + '</strong>' +
        '<div class="meta">' + (r.products || []).concat(r.categories || []).join(' · ') + '</div></a>';
    }).join('');
    results.classList.add('open');
  }

  input.addEventListener('input', function () {
    var q = input.value.trim().toLowerCase();
    if (!index || q.length < 2) { results.classList.remove('open'); return; }
    var matches = index.filter(function (r) {
      return r.title.toLowerCase().indexOf(q) !== -1 ||
        (r.products || []).some(function (p) { return p.toLowerCase().indexOf(q) !== -1; }) ||
        (r.categories || []).some(function (c) { return c.toLowerCase().indexOf(q) !== -1; });
    });
    render(matches);
  });

  document.addEventListener('click', function (e) {
    if (!results.contains(e.target) && e.target !== input) results.classList.remove('open');
  });
})();
