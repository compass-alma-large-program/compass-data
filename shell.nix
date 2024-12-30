# Nix shell for COMPASS data reduction
# Type `nix-shell` in this directory to open a shell with IMAGER installed.
# See https://nixos.org for more information.

with import (fetchTarball {
  url = "https://github.com/nixos/nixpkgs/archive/refs/tags/24.05.tar.gz";
  sha256 = "1lr1h35prqkd1mkmzriwlpvxcb34kmhc9dnr48gkm8hh089hifmx";
}) { };
let
  nur = import (fetchTarball {
    # IMAGER 4.4-01
    url = "https://github.com/nix-community/NUR/archive/72e992f26b7c6b2bafce47b3be9625e772a7a6a3.tar.gz";
    sha256 = "0j9a8a9c316p70qlih1jckjlxlxc4rnif8c8j58cqm0sg25cbrbb";
  }) { inherit pkgs; };
  imager = nur.repos.smaret.imager;
in
pkgs.mkShell rec {
  buildInputs = [
    imager
  ];
}
