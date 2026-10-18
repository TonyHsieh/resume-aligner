{
  pkgs,
  lib,
  config,
  inputs,
  ...
}:

{
  # Python toolchain for the resume-aligner factory.
  # Dependencies are declared in pyproject.toml and synced by uv on shell entry.
  languages.python = {
    enable = true;
    venv.enable = true;
    uv = {
      enable = true;
      sync.enable = true;
    };
  };

  packages = [ pkgs.git ];

  scripts.rf.exec = ''
    python -m resume_factory.cli "$@"
  '';

  enterShell = ''
    python --version
  '';

  enterTest = ''
    pytest -q
  '';

  # See full reference at https://devenv.sh/reference/options/
}
