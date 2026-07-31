# Local-dev-only compatibility shim, not a GitHub Pages concern.
#
# Liquid 4.0.3 (pinned by the github-pages gem, matching what GitHub's own
# build servers run) calls Object#tainted? as part of its old taint-check
# security feature. Ruby fully removed object tainting in 3.2+, so on newer
# local Rubies (e.g. 4.0) this crashes on every template render. GitHub
# Pages' actual build servers run their own internally-consistent Ruby that
# still supports this, so production is unaffected either way - this only
# unblocks running Jekyll locally.
#
# Loaded via the RUBYOPT env var (see scripts/serve.ps1), not a Gemfile
# monkeypatch or a _plugins/ file: `bundle exec` reads the resolved
# Gemfile.lock at runtime rather than re-evaluating the Gemfile's Ruby code,
# and github-pages forces Jekyll's safe mode locally (mirroring GitHub's
# production behavior), which silently disables _plugins/. RUBYOPT's -r
# flag loads this before Bundler or Jekyll get involved at all.
class Object
  def tainted?
    false
  end unless method_defined?(:tainted?)

  def taint
    self
  end unless method_defined?(:taint)

  def untaint
    self
  end unless method_defined?(:untaint)
end
