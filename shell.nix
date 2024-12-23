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
    url = "https://github.com/nix-community/NUR/archive/1a4eeb934b09137c2978ef07b61ff31ee3a7e26e.tar.gz";
    sha256 = "16lnjfar08p5mrkk3r6dfl1wxp4h1cfkn4icvbzgq7h8yx4d0zwm";
  }) { inherit pkgs; };
  imager = nur.repos.smaret.imager;
in
pkgs.mkShell rec {
  buildInputs = [
    imager
  ];
}
