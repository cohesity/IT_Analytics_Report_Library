(function () {
  var link = document.getElementById('download-link');
  var dialog = document.getElementById('download-ack-dialog');
  if (!link || !dialog) return;

  var supportsDialog = typeof dialog.showModal === 'function';

  // The visible link's href/download attributes are never touched - they
  // stay Liquid-resolved and baseurl-correct as rendered. On acknowledgment,
  // a synthetic, invisible anchor with the same href/download is clicked -
  // a genuine anchor click, so the browser's native `download` attribute
  // behavior (save, don't navigate) is fully preserved.
  function reallyDownload() {
    var a = document.createElement('a');
    a.href = link.href;
    a.download = link.getAttribute('download') || '';
    document.body.appendChild(a);
    a.click();
    a.remove();
  }

  link.addEventListener('click', function (e) {
    e.preventDefault();
    if (!supportsDialog) {
      if (window.confirm('This report template is provided AS-IS by the community and is not officially supported by Cohesity. Do not contact Cohesity Support with issues. Continue with download?')) reallyDownload();
      return;
    }
    dialog.showModal();
  });

  document.getElementById('download-ack-confirm').addEventListener('click', function () {
    dialog.close();
    reallyDownload();
  });
  document.getElementById('download-ack-cancel').addEventListener('click', function () {
    dialog.close();
  });
})();
