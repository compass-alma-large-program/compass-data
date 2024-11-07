# Nix shell for COMPASS data reduction
# Type `nix-shell` in this directory to open a shell with IMAGER installed.
# See https://nixos.org for more information.

with import (fetchTarball {
  url = "https://github.com/nixos/nixpkgs/archive/refs/tags/24.05.tar.gz";
  sha256 = "1lr1h35prqkd1mkmzriwlpvxcb34kmhc9dnr48gkm8hh089hifmx";
}) { };
let
  nur = import (fetchTarball {
    # IMAGER 4.2-08
    url = "https://github.com/nix-community/NUR/archive/bfd50d178dff545abb87dbf0663a3bd7abfad92d.tar.gz";
    sha256 = "0wcjf0vm9f6himd1iy0p8r9sq2q7xi5qvmnd5zzwhnl422q7gylm";
  }) { inherit pkgs; };
  imager = nur.repos.smaret.imager;
in
pkgs.mkShell rec {
  buildInputs = [
    imager
  ];
}
